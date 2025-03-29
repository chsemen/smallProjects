import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(type(res))
print(res.status_code == requests.codes.ok)

print(len(res.text))

print(res.text[:250])

# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# res.raise_for_status()

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()    