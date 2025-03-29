import os
import census2020

print()
print(census2020.allData['AK']['Anchorage'])
anchoragePop = census2020.allData['AK']['Anchorage']['pop']
print(f'The 2010 population of Anchorage was {anchoragePop}')