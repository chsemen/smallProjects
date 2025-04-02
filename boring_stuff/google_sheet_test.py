import ezsheets
ss = ezsheets.Spreadsheet('1EVhv3NZZA7O5PRso9Geee7hvIbsHdK46I4G1nNELqEM')
print(ss)

print(ss.title)
ss.title = 'Class data'
print(ss.spreadsheetId)
print(ss.url)
print(ss.sheetTitles)
print(ss.title)

print(ss[0])
print(ss['Students'])
# del ss[0]

print(ss.sheetTitles)

ss.title
print(ss.downloadAsExcel()) # Downloads the spreadsheet as an Excel file.
print(ss.downloadAsExcel('a_different_filename.xlsx'))
print(ss.downloadAsODS()) # Downloads the spreadsheet as an OpenOffice file.
print(ss.downloadAsCSV()) # Only downloads the first sheet as a CSV file.
# print(ss.downloadAsTSV()) # Only downloads the first sheet as a TSV file.
print(ss.downloadAsPDF()) # Downloads the spreadsheet as a PDF.
# Не работает
# print(ss.downloadAsHTML()) # Downloads the spreadsheet as a ZIP of HTML files.

# ss = ezsheets.createSpreadsheet('Title of My New Spreadsheet')
# print(ss.title)

# ss = ezsheets.upload('sampleChart.xlsx')
# print(ss.title)

# print(ezsheets.listSpreadsheets())