import csv

def size_type(name):
    if '/' in name:
        return 'fractional'
    elif len(name) == 1 and name[0] > '9':
        return 'letter'
    else:
        return 'number'

def imperial_drill(filename):
    sizes = {}

    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            name = line[0].strip()
            size = line[1].strip()
            dtype = size_type(name)

            if dtype == 'number':
                name = "#" + name

            sizes[name] = {"nominal" : size, "type" : dtype, "diameter" : 25400 * float(size)}
  
    # Add various other sizes - 1" 
    sizes["1"] = {"nominal" : "1.000", "type" : 'fractional', "diameter" : 25400}
        
    return sizes

print imperial_drill('imperial_drill.csv')
