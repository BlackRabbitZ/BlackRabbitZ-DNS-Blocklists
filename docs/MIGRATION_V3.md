# Migration auf v3-Profilteile

**🌐 Sprache / Language:** 🇩🇪 **Deutsch** · [🇬🇧 English](MIGRATION_V3_EN.md)

BlackRabbitZ v3 verallgemeinert die Aufteilung großer Listen und ändert die veröffentlichten URLs für Security, Family und Ultimate.

## Für den Repository-Maintainer

1. Ersetze bzw. ergänze die Dateien aus dem v3-Upgrade-Paket.
2. Committe und pushe sie nach `main`.
3. Der Workflow **Update blocklists** baut alle kombinierten Profile automatisch neu.
4. Der Workflow entfernt alte erzeugte Security-/Family-/Ultimate-Ausgaben, erstellt die neuen `*-part-NN.txt`-Dateien, erzeugt Metadaten/Prüfsummen und aktualisiert die README-Dateien mit den exakten Raw-URLs.
5. Prüfe, ob der Workflow erfolgreich abgeschlossen wurde, bevor du die neuen URLs veröffentlichst.

Für die Migration müssen keine Kategorie-Domaindateien manuell bearbeitet werden.

## Für Pi-hole-/DNS-Filter-Nutzer

Alte Abonnements mit einem dieser Pfade müssen ersetzt werden:

```text
lists/combined/security.txt
lists/combined/family.txt
lists/combined/ultimate-1.txt
lists/combined/ultimate-2.txt
...
```

Öffne nach dem v3-Neuaufbau die Repository-README und füge **alle Raw-Teile** des gewünschten gesplitteten Profils hinzu:

```text
security-part-01.txt
security-part-02.txt
...

family-part-01.txt
family-part-02.txt
...

ultimate-part-01.txt
ultimate-part-02.txt
...
```

Entferne anschließend die veralteten URLs und aktualisiere Gravity.

## Verhaltensänderungen

- Balanced enthält kein Affiliate Tracking mehr. Affiliate-/Referral-Blocking beginnt ab Strict.
- Consent/CMP ist nicht mehr in Ultimate enthalten. Die separate Consent/CMP-Kategorie bleibt für Nutzer verfügbar, die das höhere Risiko von Website-Fehlfunktionen bewusst akzeptieren.
- Security und Family werden als optionale Schutzmodule dokumentiert und nicht mehr als aufeinanderfolgende Datenschutzstufen dargestellt.
