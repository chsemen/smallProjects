# This script runs in Windows only, and you must have Word installed
# Не работает

import win32com.client
import docx
from pathlib import Path

cwd=Path.cwd()

wordFileName = 'test.docx'
pdfFileName = 'test.pdf'

doc = docx.Document()
doc.add_paragraph('This is on the first page!')
for i in range(10):
    doc.add_heading(f'Header {i}', i)

doc.paragraphs[0].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)
doc.add_paragraph('This is on the second page!')
doc.add_picture('zophie.png', width=docx.shared.Inches(1), height = docx.shared.Cm(4))

doc.save(wordFileName)

wdFormatPDF = 17
# wordObj = win32com.client.Dispatch('Word.Application')
# docObj = wordObj.Documents.Open(str(s))
wordObj = win32com.client.Dispatch('Writer.Application')
s =cwd / wordFileName
docObj = wordObj.Documents().Open(str(s))
docObj.SaveAs(pdfFileName, FileFormat = wdFormatPDF)
docObj.Close()

wordObj.Quit()