import csv
import os
from url_parsing import URLParsing
from pathlib import Path

def get_data(path_file):
    urls = []
    path = os.path.abspath(path_file)
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        next(csv_reader)
        i=1
        for row in csv_reader:
            urls.append(row[0])       
    array =  [URLParsing(x) for x in urls]
    return array

