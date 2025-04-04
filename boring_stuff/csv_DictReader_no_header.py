import csv
exampleFile = open('example.csv')
exampleDictReader = csv.DictReader(exampleFile, ['time', 'name', 'amount'])
for row in exampleDictReader:
    print(row['time'], row['name'], row['amount'])
