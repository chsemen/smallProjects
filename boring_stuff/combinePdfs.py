#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into
# into a single PDF.

import PyPDF2, os
pdfFiles = []
for fn in os.listdir('.'):
    if fn.endswith('.pdf') and fn in ['meetingminutes.pdf', 'meetingminutes2.pdf']:
        pdfFiles.append(fn)

pdfFiles.sort()        

pdfWriter = PyPDF2.PdfWriter()

for filename in pdfFiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    for pageNum in range(1, len(pdfReader.pages)):
        page = pdfReader.pages[pageNum]
        pdfWriter.add_page(page)
    pdfFile.close()



pdfOutputFile = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()