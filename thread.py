import csv


def imperial_thread(filename):
    raw_threads = {}

    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            raw_threads[line[0].strip()+'-'+line[2].strip()] = line
    threads = {}
    for name, cells in raw_threads.iteritems():
        threads[name] = {"major" : 25400 * float(cells[1].strip()),
                         "minor" : 25400 * float(cells[3].strip()),
                         "tpi" : int(cells[2].strip()),
                         "75%-thread" : 25400 * float(cells[5].strip()),
                         "50%-thread" : 25400 * float(cells[7].strip())
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
        for p in pitches:
            name = 'M' + diameter + 'x' + p
            threads[name] = {'major' : 1000 * float(diameter), 'drill' : 1000 * (float(diameter) - float(p)), 'pitch' : 1000 * float(p)}

    return threads

print metric_thread("metric_thread.csv")
