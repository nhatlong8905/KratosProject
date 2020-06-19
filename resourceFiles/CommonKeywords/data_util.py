import csv
from golem.core.utils import load_json_from_file

def read_csv_file(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print (row)
            data.append(row)
            
    return data

def read_json_file (filename):
    return load_json_from_file(filename)
    
def intake_data (filename):
    extension = filename[-4:]
    if extension == '.csv':
        return read_csv_file(filename)
    elif extension == 'json':
        return read_json_file (filename)
    else:
        raise Exception ('{} extension has not supported'.format(extension))