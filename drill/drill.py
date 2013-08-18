import csv


def size_type(name):
    if '/' in name:
        return 'fractional'
    elif len(name) == 1 and name[0] > '9':
        return 'letter'
    else:
        return 'number'

def imperial_drill(filename):
    raw_sizes = {}

    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            for i in range(0,min(2, len(line) / 2)): # only take first six rows
                raw_sizes[line[2*i].strip()] = line[2*i + 1].strip()

    sizes = {}
    for name, size in raw_sizes.iteritems():
        dtype = size_type(name)
        if dtype == 'number':
            name = "#" + name
        sizes[name] = {"nominal" : size, "type" : dtype, "diameter" : 25400 * float(size)}
    # Add various other sizes - 1" 
    sizes["1"] = {"nominal" : "1.000", "type" : 'fractional', "diameter" : 25400}
        
    return sizes

print imperial_drill('imperial.csv')
