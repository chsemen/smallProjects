import docx

doc = docx.Document()
# doc.add_paragraph('Hello world!')
para1 = doc.add_paragraph('This is a second paragraph.')
para2 = doc.add_paragraph('This is a yet another paragraph.')
para1.add_run(' This text is being added to the second paragraph.')
doc.add_paragraph('Hello world!', 'Title')
doc.save('multipleParagraphs.docx')
