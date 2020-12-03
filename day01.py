import csv

with open('inputs/day01.csv') as csvfile:
    data_iter = csv.reader(csvfile, delimiter='\n')
    data = [int(entry[0]) for entry in data_iter]

for i1, d1 in enumerate(data):
    for i2 in range(i1+1, len(data)):
        d2 = data[i2]
        for i3 in range(i2+1, len(data)):
            d3 = data[i3]
            if d1 + d2 + d3 == 2020:
                print(d1*d2*d3)