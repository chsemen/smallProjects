import PyPDF2

pdfFileObj = open('encrypted.pdf', 'rb')

# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader = PyPDF2.PdfReader(pdfFileObj)
print()
print(pdfReader.is_encrypted)
pdfReader.decrypt('rosebud')
page = pdfReader.pages[0]
print(page)

pdfFileObj.close()