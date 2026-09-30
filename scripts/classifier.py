#!/usr/bin/env python3
from __future__ import annotations
import json, re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULES_PATH = ROOT / "config" / "classifier-rules.json"
CRITICAL_PATH = ROOT / "config" / "critical-services.txt"
ALLOWLIST_PATH = ROOT / "config" / "allowlist.txt"

@dataclass
class Evidence:
    category: str
    source_name: str = ""
    source_url: str = ""
    trust: str = "direct"

@dataclass
class Decision:
    domain: str
    category: str | None
    confidence: int
    status: str
    reason: str
    scores: dict[str, int] = field(default_factory=dict)
    vendor: str = "unknown"
    function: str = "unknown"


def _read_roots(path: Path) -> set[str]:
    if not path.exists(): return set()
    out=set()
    for line in path.read_text(encoding="utf-8",errors="ignore").splitlines():
        s=line.strip().lower().rstrip('.')
        if s and not s.startswith(('#','!')): out.add(s)
    return out


def suffix(domain: str, root: str) -> bool:
    root=root.lower().lstrip('.')
    return domain == root or domain.endswith('.'+root)


def load_rules() -> dict:
    return json.loads(RULES_PATH.read_text(encoding='utf-8'))


def classify(domain: str, evidences: list[Evidence], rules: dict | None=None) -> Decision:
    rules = rules or load_rules()
    d=domain.lower().rstrip('.')
    privacy=set(rules['privacy_categories'])
    ev_priv=[e for e in evidences if e.category in privacy]
    # Non-privacy lists (malware/phishing/family/etc.) intentionally keep their own semantics.
    if not ev_priv:
        cat=evidences[0].category if evidences else None
        return Decision(d,cat,100,'passthrough','non-privacy/security/content category')

    protected=_read_roots(ALLOWLIST_PATH)|_read_roots(CRITICAL_PATH)
    if any(suffix(d,r) for r in protected):
        return Decision(d,None,100,'quarantine','critical-or-allowlisted')

    # Critical-looking endpoints are conservative unless all evidence comes from an explicit security category.
    for token in rules.get('critical_tokens',[]):
        if token in d:
            return Decision(d,None,92,'quarantine',f'functional-endpoint:{token}')

    scores={c:0 for c in privacy}
    source_weights=rules.get('source_category_weights',{})
    for e in ev_priv:
        base=int(source_weights.get(e.category,50))
        trust_bonus=25 if e.trust=='direct' else 10
        scores[e.category]=scores.get(e.category,0)+base+trust_bonus
        sn=e.source_name.lower()
        for cat,tokens in rules.get('source_name_hints',{}).items():
            if cat in scores and any(t.lower() in sn for t in tokens):
                scores[cat]+=40

    vendor='unknown'
    vendor_categories=[]
    for cat,roots in rules.get('domain_hints',{}).items():
        matched=[r for r in roots if suffix(d,r)]
        if matched and cat in scores:
            scores[cat]+=65
            vendor_categories.append(cat)
            vendor=cat.replace('-telemetry','').replace('smart-tv','smart-tv').replace('iot','iot')

    func='unknown'
    telemetry_like=False
    for cat,tokens in rules.get('function_hints',{}).items():
        matches=sum(1 for t in tokens if t.lower() in d)
        if matches and cat in scores:
            scores[cat]+=30 + min(10,(matches-1)*5)
            if cat=='telemetry': telemetry_like=True
            if scores[cat] >= max(scores.values()): func=cat
    # A telemetry-looking endpoint on a recognised device/platform should prefer
    # that specific device category over the generic telemetry/tracker bucket.
    if telemetry_like:
        for cat in vendor_categories:
            scores[cat]+=25

    priority={c:i for i,c in enumerate(rules.get('category_priority',[]))}
    ranked=sorted(scores.items(), key=lambda kv:(kv[1], -priority.get(kv[0],999)), reverse=True)
    top_cat,top_score=ranked[0]
    second_score=ranked[1][1] if len(ranked)>1 else 0
    conf=min(100,top_score)
    threshold=int(rules.get('confidence',{}).get('auto_accept',75))
    review=int(rules.get('confidence',{}).get('review',55))
    margin=int(rules.get('confidence',{}).get('minimum_margin',10))

    # Device/platform-specific evidence wins a close tie over a broad privacy bucket.
    specific=set(rules.get('specific_categories',[]))
    tie_ok=top_cat in specific and top_score>=85
    if top_score>=threshold and (top_score-second_score>=margin or tie_ok):
        return Decision(d,top_cat,conf,'accepted',f'best-category score={top_score}, margin={top_score-second_score}',scores,vendor,func)
    if top_score>=review:
        return Decision(d,None,conf,'quarantine',f'ambiguous score={top_score}, margin={top_score-second_score}',scores,vendor,func)
    return Decision(d,None,conf,'rejected',f'low-confidence score={top_score}',scores,vendor,func)
