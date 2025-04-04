#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current

import csv, os
destDir = 'headerRemoved'
os.makedirs(destDir, exist_ok=True)

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue
    print(f'Removing header from {csvFilename}...')
    csvRows = []
    csvFile = open(csvFilename, encoding='utf-8')
    reader = csv.reader(csvFile)
    for row in reader:
        if reader.line_num == 1:
            continue
        csvRows.append(row)
    csvFile.close()
    outputFile = open(os.path.join(destDir, csvFilename), 'w', newline='')
    writer = csv.writer(outputFile)
    for row in csvRows:
        writer.writerow(row)
    outputFile.close()



