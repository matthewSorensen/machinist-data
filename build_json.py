import drill
import tap


import json
from os.path import basename,splitext
from glob import glob

blob = {}

blob['drill'] = {"imperial" : drill.imperial_drill("imperial_drill.tsv")}
blob['tap']   = {"imperial" : tap.imperial_thread("imperial_thread.tsv"), 
                 "metric" : tap.metric_thread("metric_thread.csv")}
blob['speed'] = {}

for filename in glob("speeds/*.json"):
    with open(filename, 'rb') as fd:
        blob['speed'][splitext(basename(filename))[0]] = json.load(fd)

print json.dumps(blob)
