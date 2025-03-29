# Не работает
#! python3
# searchpypi.py - Opens several search results.


import requests, sys, webbrowser, bs4
print('Searching...') # display text while downloading the search result page
# res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
s = 'https://pypi.org/search/?q=' + "boring stuff"
print(s)
s = 'https://pypi.org/search/?q=boring%20stuff'
s='https://www.google.com/search?q=boring+stuff'
s='https://ya.ru/search/?text=boring+stuff'
webbrowser.open(s)
webbrowser.sa
res = requests.get(s)
res.raise_for_status()

htmlFile = open('test.html', 'w', encoding="utf-8")
htmlFile.write(res.text)
htmlFile.close()



soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
# linkElems = soup.select('.package-snippet')
linkElems = soup.select('#content > div > div > div.left-layout__main > form > div:nth-child(3) > ul')
print(type(linkElems))
print(len(linkElems))

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'http://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)