import json
import os
import re

critterIndexArray = {}
spellIndexArray = {}
itemIndexArray = {}
critterFileIndexArray = {}
spellFileIndexArray = {}
itemFileIndexArray = {}


# fvtt package unpack --out ~/github/HucaenFoundryModule/collating/AB/ -n abyssalbrews-vol-1-rare
# fvtt package unpack --out ~/github/HucaenFoundryModule/collating/AB/ -n abyssalbrews-vol-1-unique
# fvtt package unpack --out ~/github/HucaenFoundryModule/collating/AB/ -n abyssalbrews-vol-1-uncommon
# fvtt package unpack --out ~/github/HucaenFoundryModule/collating/AB/ -n abyssalbrews-vol-1-common
# fvtt package unpack --out ~/github/HucaenFoundryModule/collating/AB/ -n abyssalbrews-vol-1-actors

critterregex = re.compile(r"-")
spellregex = re.compile(r"spells")
itemregex = re.compile(r"equipment$")

directory = os.getcwd().split('/')[0:4]
gitdir = ''
for i in directory:
	if i == 'github':
		gitdir = gitdir+'/github'
		continue
	elif i == '':
		gitdir = gitdir
	else:
		gitdir = gitdir+'/'+i

print (gitdir)

for root, dirs, files in os.walk(gitdir+'/pf2e/packs'):
	print(root)
	if 'criticaldeck' not in root and 'rollable-tables' not in root and 'journals' not in root:
		for i in files:
			if 'json' in i and '_' not in i:
				with open(root+'/'+i, 'r', encoding='utf-8') as jsonf: 
					data = json.load(jsonf)
					if 'content' in data.keys():
						print (i)
					elif data['name'] in critterIndexArray.keys():
						if ('publication' in data['system'].keys() and data['system']['publication']['remaster']):
							if data['type'] == 'npc':
								critterIndexArray[data['name']] = data['_id']
								critterFileIndexArray[data['name']] = root+'/'+i
							if data['type'] == 'spell':
								spellIndexArray[data['name']] = data['_id']
								spellFileIndexArray[data['name']] = root+'/'+i
							if data['type'] in ['consumable','equipment']:
								itemIndexArray[data['name']] = data['_id']
								itemFileIndexArray[data['name']] = root+'/'+i
						elif 'publication' in data['system'].keys():
							print(i,data['name'],critterIndexArray[data['name']])
						elif data['system']['details']['publication']['remaster']:
							if data['type'] == 'npc':
								critterIndexArray[data['name']] = data['_id']
								critterFileIndexArray[data['name']] = root+'/'+i
							if data['type'] == 'spell':
								spellIndexArray[data['name']] = data['_id']
								spellFileIndexArray[data['name']] = root+'/'+i
							if data['type'] in ['consumable','equipment']:
								itemIndexArray[data['name']] = data['_id']
								itemFileIndexArray[data['name']] = root+'/'+i
					else:
						if data['type'] == 'npc':
							critterIndexArray[data['name']] = data['_id']
							critterFileIndexArray[data['name']] = root+'/'+i
						if data['type'] == 'spell':
							spellIndexArray[data['name']] = data['_id']
							spellFileIndexArray[data['name']] = root+'/'+i
						if data['type'] in ['consumable','equipment']:
							itemIndexArray[data['name']] = data['_id']
							itemFileIndexArray[data['name']] = root+'/'+i

for root, dirs, files in os.walk(gitdir+'/HucaenFoundryModule/collating/premiumContent'):
	print(root)
	for i in files:
		if 'json' in i and '_' not in i:
			with open(root+'/'+i, 'r', encoding='utf-8') as jsonf: 
				data = json.load(jsonf)
				if data['type'] == 'npc':
					critterIndexArray[data['name']] = data['_id']
					critterFileIndexArray[data['name']] = root+'/'+i
				if data['type'] == 'spell':
					spellIndexArray[data['name']] = data['_id']
					spellFileIndexArray[data['name']] = root+'/'+i
				if data['type'] in ['consumable','equipment']:
					itemIndexArray[data['name']] = data['_id']
					itemFileIndexArray[data['name']] = root+'/'+i


with open('creatureIndex.json', 'w') as jsonout:
	jsonout.write(json.dumps(critterIndexArray, indent=4))

with open('creatureFileIndex.json', 'w') as jsonout:
	jsonout.write(json.dumps(critterFileIndexArray, indent=4))

with open('spellIndex.json', 'w') as jsonout:
	jsonout.write(json.dumps(spellIndexArray, indent=4))

with open('spellFileIndex.json', 'w') as jsonout:
	jsonout.write(json.dumps(spellFileIndexArray, indent=4))

with open('itemIndex.json', 'w') as jsonout:
	jsonout.write(json.dumps(itemIndexArray, indent=4))

with open('itemFileIndex.json', 'w') as jsonout:
	jsonout.write(json.dumps(itemFileIndexArray, indent=4))
