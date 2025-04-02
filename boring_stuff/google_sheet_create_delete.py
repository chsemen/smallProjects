import ezsheets

ss = ezsheets.createSpreadsheet('Multiple Sheets')
print(ss.sheetTitles)
print(ss.createSheet('Spam'))
print(ss.createSheet('Eggs'))

print(ss.sheetTitles)

print(ss.createSheet('Bacon', 0))
print(ss.sheetTitles)

ss[0].delete()
print(ss.sheetTitles)

ss['Spam'].delete()
print(ss.sheetTitles)

sheet=ss['Eggs']
sheet.delete()
print(ss.sheetTitles)

ss[0].clear()
print(ss.sheetTitles)
