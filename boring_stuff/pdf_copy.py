import PyPDF2

pdfFile1 = open('meetingminutes.pdf', 'rb')
pdfFile2 = open('meetingminutes2.pdf', 'rb')

pdfReader1 = PyPDF2.PdfReader(pdfFile1)
pdfReader2 = PyPDF2.PdfReader(pdfFile2)

pdfWriter = PyPDF2.PdfWriter()

for page in pdfReader1.pages:
    pdfWriter.add_page(page)

for page in pdfReader2.pages:
    pdfWriter.add_page(page)

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

pdfFile1.close()
pdfFile2.close()