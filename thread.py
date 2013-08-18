 # -*- coding: utf-8
import csv

# All screw JSON records have the following attributes:
# * standard name
# * pitch (µm)
# * major diameter
# * minor diameter
# Some are optional:
# * tpi

def imperial_thread(filename):
    raw_threads = {}

    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            raw_threads[line[0].strip()+'-'+line[2].strip()] = line
    threads = {}
    for name, cells in raw_threads.iteritems():
        tpi = int(cells[2].strip())
        threads[name] = {"major" : 25400 * float(cells[1].strip()),
                         "minor" : 25400 * float(cells[3].strip()),
                         "tpi" : tpi,
                         "pitch" : 25400.0 / (1.0 * tpi),
                         "name" : name,
                         }
    return threads

def metric_thread(filename):
    raw_threads = {}
    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for line in reader:
            raw_threads[line[0].strip()] = [s.strip() for s in line[1:]]

    threads = {}

    for diameter, pitches in raw_threads.iteritems():
        for i,pitch in enumerate(pitches):
            name = 'M' + diameter + 'x' + pitch
            udiameter = 1000 * float(diameter)
            upitch = 1000 * float(pitch)

            record = {'major' : udiameter, 
                      'minor' : udiameter - 1.082532 * upitch,
                      'pitch' : upitch,
                      'name'  : name}
            threads[name] = record
            if i == 0: # Also insert the default large thread pitch
                threads['M' + diameter] = record

    return threads

print metric_thread("metric_thread.csv")
