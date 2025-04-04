import csv
outputFile = open('output.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
outputDictWriter.writeheader()
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone':'555-1234'})
outputDictWriter.writerow({'Name': 'Bob', 'Phone':'555-9999'})
outputDictWriter.writerow({'Phone':'555-5555','Name': 'Carol', 'Pet': 'dog' })
outputFile.close()
