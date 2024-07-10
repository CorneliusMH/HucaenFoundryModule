import csv
import json
import hashlib
import random
import string

inputFile = './collating/actors.json'
creatureindexFile = './collating/creatureIndex.json'
itemindexFile = './collating/itemIndex.json'
spellindexFile = './collating/spellIndex.json'
template = './collating/templateActor.json'
outpath = './src/packs/actors-of-hucaen/'

inputData = {}
spellIds = {}
spellFiles = {}
critterIds = {}
critterFiles = {}
itemIds = {}
itemFiles = {}
actorArray = []

with open(inputFile, 'r', encoding='utf-8') as jsonf: 
	inputData = json.load(jsonf)

with open('./collating/creatureIndex.json', 'r', encoding='utf-8') as jsonz: 
	creatureIds = json.load(jsonz)

with open('./collating/creatureFileIndex.json', 'r', encoding='utf-8') as jsonz: 
	creatureFiles = json.load(jsonz)

with open('./collating/itemIndex.json', 'r', encoding='utf-8') as jsonz: 
	itemIds = json.load(jsonz)

with open('./collating/creatureFileIndex.json', 'r', encoding='utf-8') as jsonz: 
	critterFiles = json.load(jsonz)

with open('./collating/creatureFileIndex.json', 'r', encoding='utf-8') as jsonz: 
	spellFiles = json.load(jsonz)

with open('./collating/itemFileIndex.json', 'r', encoding='utf-8') as jsonz: 
	itemFiles = json.load(jsonz)

with open('./collating/map-pf2e.json', 'r', encoding='utf-8') as jsonz: 
	portraits = json.load(jsonz)

def input_actor_list(inputData):
	for row in inputData:
		actorArray.append(row)

def process_actor(inputBlob):
	person 			= inputBlob
	template 		= person['template']
	templateID 		= creatureIds[template]
	templateFile	= creatureFiles[templateID]
	with open(creatureFiles[template], 'r', encoding='utf-8') as jsonBase: 
		actorDict = json.load(jsonBase)
	filename 					= person['Name'].lower()+'.json'
	sysJson 					= actorDict['system']
	itemJson					= actorDict['items']
	actorDict['_id'] 			= person['id']
	actorDict['name']			= person['Name']
	sysJson['slug']				= person['Name'].lower()
	if person['img'] > 0:
		actorDict['img']		= portraits[person['id']]['token']
	else:
		actorDict['img']		= portaits[templateID]['token']
	actorDict['_key']			= "!actors!"+person['id']
	sysJson['details']['publicNotes'] = 
	#actorDict['flags']['scene-packer']['sourceId'] = 'Item.'+actorDict['_id']
	# We end here
	actorDict['system'] 	= sysJson
	actorDict['items'] 		= itemJson
	output_json(actorDict,filename)

def spellAdd(spell):
	with open(spellFiles[spell], 'r', encoding='utf-8') as jsonBase: 
		spellRet = json.load(jsonBase)
	return spellRet

def output_json(outData,fileName):
	towrite = json.dumps(outData, indent=4)
	with open(outpath+fileName, 'w') as jout: 
		jout.write(towrite)


input_actor_list(inputData)
for jsonBlob in actorArray:
	process_actor(jsonBlob)
