import csv
import json
import hashlib
import random
import string

inputFilePath = '../../../collating/deities.json'
spellindexPath = '../../../collating/spellIndex.json'
template = '../../../collating/templateDeity.json'

inputData = {}
spellIndex = {}
deityArray = []

with open(inputFilePath, 'r', encoding='utf-8') as jsonf: 
	inputData = json.load(jsonf)

with open(spellindexPath, 'r', encoding='utf-8') as jsonz: 
	spellIndex = json.load(jsonz)

def input_deity_list(inputData):
	for row in inputData:
		if "Hucaen Pantheon" in row['Source']:
			deityArray.append(row)

def process_deity(inputBlob):
	god = inputBlob
	with open(template, 'r', encoding='utf-8') as jsonBase: 
		deityWhole = json.load(jsonBase)
	filename 					= god['Deity'].lower()+'.json'
	deityJson 					= deityWhole['system']
	deityJson['weapons'] 		= [god['Favored Weapon']]
	deityJson['attribute'] 		= attr(god['Divine Attribute'])
	deityJson['spells'] 		= spells(god['Cleric Spells'])
	if len(god['Divine Font']) > 6:
		deityJson['font'] 		= ['harm','heal']
	else:
		deityJson['font'] 		= [god['Divine Font'].lower()]
	deityJson['domains']		= get_domains(god['Domains'])
	deityWhole['_id'] 			= get_id(god['Deity'])
	deityWhole['name']			= god['Deity']
	deityJson['skill']			= [god['Divine Skill'].lower()]
	deityJson['description'] 	= get_desc(god)
	deityJson['sanctification'] = get_sanc(god['Divine Sanctification'])
	deityJson['slug']			= god['Deity'].lower()
	deityWhole['img']			= "modules/hucaen-module/static/deities/"+god['Deity'].lower()+'.svg'
	#deityWhole['flags']['scene-packer']['sourceId'] = 'Item.'+deityWhole['_id']
	# We end here
	deityWhole['system'] = deityJson
	output_json(deityWhole,filename)

def spellLookup(spell):
	tag = spellIndex[spell]
	spellRef = "Compendium.pf2e.spells-srd.Item." + tag
	return spellRef

def get_domains(domainStr):
	primary = domainStr.split(", ")
	alternate = []
	wholeDomain = {
		'alertnate' : alternate,
		'primary'	: primary
	}
	return wholeDomain

def get_id(name):
	characters = string.ascii_letters + string.digits
	random_string = ''.join(random.choice(characters) for _ in range(15))
	deityid = name.title()+'0'+random_string
	print(deityid,deityid[:16])
	return deityid[:16]

def spells(spellStr):
	spellBlob = {}
	spellSplits = spellStr.split(",")
	for i in spellSplits:
		parts = i.split(':')
		lvl = parts[0].strip().strip("ndsthr")
		spelltag = spellLookup(parts[1].strip().title())
		spellBlob[lvl] = spelltag
	return spellBlob

def attr(attrString):
	attrs = []
	poss = ['str','dex','con','int','wis','cha']
	for i in poss:
		if i in attrString.lower():
			attrs.append(i)
	return attrs

def output_json(outData,fileName):
	towrite = json.dumps(outData, indent=4)
	with open(fileName, 'w') as jout: 
		jout.write(towrite)

def get_desc(row):
	descstr = '<p>'+row['Description']+'</p>\n<p><strong>Edicts</strong> '+row['Edicts']+'</p>\n<p><strong>Anathema</strong> '+row['Anathema']+'</p>\n<p><strong>Areas of Concern</strong> '+row['Areas of Concern']+'</p>'
	return {"value": descstr}

def get_sanc(sanctify):
	print(sanctify)
	sanctiBlob = {}
	if 'must' in sanctify:
		sanctiBlob['modal'] = 'must'
	elif 'can' in sanctify:
		sanctiBlob['modal'] = 'can'
	else:
		return Null
	sanctiwords = sanctify.split(' ')
	sanctigroup = []
	sanctigroup.append(sanctiwords[2])
	if len(sanctiwords) > 3:
		sanctigroup.append(sanctiwords[4])
	sanctiBlob['what'] = sanctigroup
	return sanctiBlob


input_deity_list(inputData)
for jsonBlob in deityArray:
	process_deity(jsonBlob)
