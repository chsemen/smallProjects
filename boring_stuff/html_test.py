import requests, bs4

#detailed-forecast-body > div:nth-child(1) > div.col-sm-10.forecast-text

# res = requests.get('https://nostarch.com/automatestuff2/')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(noStarchSoup))

# elems = noStarchSoup.select('#author')
exampleFile = open('example.html')
#block-system-main > div > div > div.field.field-name-field-author.field-type-text.field-label-hidden

# <div class="field field-name-field-author field-type-text field-label-hidden"><div class="field-items"><div class="field-item even">by Al Sweigart</div></div></div>
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
# elems = exampleSoup.select('#author')
elems = exampleSoup.select('#block-system-main > div > div > div.field.field-name-field-author.field-type-text.field-label-hidden')
print(type(elems))
print(len(elems))

print(type(elems[0]))
print(str(elems[0]))
print(elems[0].getText())
print(elems[0].attrs)

pElems = exampleSoup.select('p')
print(str(pElems[0]))

spanElem = exampleSoup.select('span')[0]
print(str(spanElem))