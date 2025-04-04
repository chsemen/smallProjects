import PyPDF2

pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFile)

pdfWriter = PyPDF2.PdfWriter()

for iPage in range(0, len(pdfReader.pages)):
    page = pdfReader.pages[iPage]
    pdfWriter.add_page(page)

pdfWriter.encrypt('swordfish')

pdfOutputFile = open('minutesEncrypted.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()

pdfFile.close()
