import csv
exampleFile = open('exampleWithHeader.csv')
exampleDictReader = csv.DictReader(exampleFile)
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
