import json
import os

spellIndexArray = {}

mypath = './'
files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
for i in files:
	with open(i, 'r', encoding='utf-8') as jsonf: 
		print(i)
		data = json.load(jsonf)
		spellIndexArray[data['name']] = data['_id']

jsonString = json.dumps(spellIndexArray, indent=4)
print(jsonString)
with open('spellIndex.json', 'w') as jsonout:
    jsonout.write(jsonString)

