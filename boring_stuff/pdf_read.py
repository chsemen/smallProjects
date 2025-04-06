import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')

# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader = PyPDF2.PdfReader(pdfFileObj)
pages = pdfReader.pages
print(len(pages))
pageObj = pdfReader.pages[0]
print(pageObj.extract_text())
pdfFileObj.close()