import PyPDF2

pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFile)
page0 = pdfReader.pages[0]
pdfFileWatermark = open('watermark.pdf', 'rb')
pdfReaderWatermark = PyPDF2.PdfReader(pdfFileWatermark)
page0.merge_page(pdfReaderWatermark.pages[0])
pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(page0)

for iPage in range(1, len(pdfReader.pages)):
    page = pdfReader.pages[iPage]
    pdfWriter.add_page(page)

pdfOutputFile = open('minutesWithWatermark.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()

pdfFile.close()
