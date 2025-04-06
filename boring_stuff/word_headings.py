import docx

doc = docx.Document()
for i in range(10):
    doc.add_heading(f'Header {i}', i)
doc.save('headings.docx')
