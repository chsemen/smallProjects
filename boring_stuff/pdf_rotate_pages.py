import PyPDF2

pdfFile1 = open('meetingminutes.pdf', 'rb')
pdfReader1 = PyPDF2.PdfReader(pdfFile1)

pdfWriter = PyPDF2.PdfWriter()

for page in pdfReader1.pages:
    page.rotate(-90)
    pdfWriter.add_page(page)

pdfOutputFile = open('meetingminutes-90.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFile1.close()
