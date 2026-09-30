#!/usr/bin/env python3
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from classifier import Evidence,classify,load_rules
r=load_rules()
def cat(d,ev):return classify(d,ev,r)
# Critical services must never enter privacy lists.
x=cat('download.windowsupdate.com',[Evidence('telemetry','generic telemetry','','filtered')]);assert x.status=='quarantine',x
x=cat('login.microsoftonline.com',[Evidence('trackers','generic tracking','','direct')]);assert x.status=='quarantine',x
# Specific source evidence should beat generic/native buckets.
x=cat('vortex.data.microsoft.com',[Evidence('telemetry','generic telemetry','','filtered'),Evidence('windows-telemetry','NextDNS Windows Native Tracking','','direct')]);assert x.category=='windows-telemetry' and x.status=='accepted',x
x=cat('metrics.apple.com',[Evidence('telemetry','generic telemetry','','filtered'),Evidence('apple-telemetry','NextDNS Apple Native Tracking','','direct')]);assert x.category=='apple-telemetry' and x.status=='accepted',x
x=cat('analytics.example.com',[Evidence('telemetry','tracking telemetry subset','','filtered')]);assert x.category=='telemetry' and x.status=='accepted',x
x=cat('graph.facebook.com',[Evidence('social-trackers','social subset','','filtered')]);assert x.category=='social-trackers' and x.status=='accepted',x
print('classifier tests: OK')
x=cat('metrics.samsungtv.com',[Evidence('trackers','generic tracking','','direct')]);assert x.category=='smart-tv' and x.status=='accepted',x
