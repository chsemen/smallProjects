import json
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

j = json.loads(stringOfJsonData)
print(j)

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
stringOfJsonData=json.dumps(pythonValue)
print(stringOfJsonData)