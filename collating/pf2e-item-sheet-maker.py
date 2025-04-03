import json
import os
import re
import csv
from pprint import pprint

ItemList = {}
ItemListColumns = [
	'Name','PFS','Source',
	'SrcType','Rarity','Trait',
	'Type','Item category','Item subcategory',
	'Level','Value','Min Bulk',
	'Price','Bulk','Usage'
]
currency = {
	'gp':1,
	'pp':10,
	'sp':0.1,
	'cp':0.01
}

def getDeets(itemName):
	with open(itemFiles[itemName]) as item:
		itemDeets = json.load(item)
	itemDict = {}
	itemDict['name'] = itemDeets['name'].title()
	pfs = ''
	itemDict['source'] = itemDeets['system']['publication']['title'].title()
	itemDict['rarity'] = itemDeets['system']['traits']['rarity'].title()
	traitlist = itemDeets['system']['traits']['value']
	traitlist.append(itemDict['rarity'])
	itemDict['trait'] = ', '.join(traitlist)
	iType = ''
	try:
		itemDict['category'] = itemDeets['system']['category'].title()
	except:
		pass
	itemDict['subcategory'] = ''
	itemDict['level'] = itemDeets['system']['level']['value']
	itemDict['minBulk'] = itemDeets['system']['usage']['value']*1
	itemDict['bulk'] = itemDeets['system']['usage']['value']
	itemDict['usage'] = itemDeets['system']['usage']['value']
	price = ''
	value = 0

	for i in itemDeets['system']['price']['value'].keys():
		price = price + str(itemDeets['system']['price']['value'][i]) + i
		value = value + (itemDeets['system']['price']['value'][i] * currency[i])

	itemDict['price'] = price
	itemDict['value'] = value

	return (itemDict)



with open('itemFileIndex.json') as f:
    itemFiles = json.load(f)

testnum = 20
while testnum > 0:
	for i in itemFiles.keys():
		print(i)
		ItemList[i] = getDeets(i)
	testnum -= 1


# 	['Name'
# 'PFS'
# 'Source'
# 'SrcType'
# 'Rarity'
# 'Trait'
# 'Type'
# 'Item category'
# 'Item subcategory'
# 'Level'
# 'Value'
# 'Min Bulk'
# 'Price'
# 'Bulk'
# 'Usage'
# 'Spoilers']


# 	print(itemFiles[i])




# {'_id': 'eKpL2j1JA92wndO6',
#  'img': 'systems/pf2e/icons/equipment/alchemical-items/drugs/zerk.webp',
#  'name': 'Zerk',
#  'system': {'baseItem': None,
#             'bulk': {'value': 0.1},
#             'category': 'drug',
#             'containerId': None,
#             'damage': None,
#             'description': {'value': '<p>This bitter paste is used among some '
#                                      'gladiatorial rings for its short-term '
#                                      'benefits in a fight.</p>\n'
#                                      '<hr />\n'
#                                      '<p><strong>Activate</strong> <span '
#                                      'class="action-glyph">A</span> Interact '
#                                      '(Injury)</p>\n'
#                                      '<p><strong>Saving Throw</strong> '
#                                      '@Check[fortitude|dc:20]</p>\n'
#                                      '<p><strong>Maximum Duration</strong> 1 '
#                                      'hour</p>\n'
#                                      '<p><strong>Stage 1</strong> +2 item '
#                                      'bonus to Perception rolls for '
#                                      'initiative, and if you have an addiction '
#                                      'to zerk, your melee weapon and unarmed '
#                                      'attacks deal an extra 2 damage during '
#                                      'the first round of a combat encounter (1 '
#                                      'minute)</p>\n'
#                                      '<p><strong>Stage 2</strong> '
#                                      '@UUID[Compendium.pf2e.conditionitems.Item.Drained]{Drained '
#                                      '1} (1 hour)</p>'},
#             'hardness': 0,
#             'hp': {'max': 0, 'value': 0},
#             'level': {'value': 4},
#             'material': {'grade': None, 'type': None},
#             'price': {'value': {'gp': 20}},
#             'publication': {'license': 'OGL',
#                             'remaster': False,
#                             'title': 'Pathfinder Gamemastery Guide'},
#             'quantity': 1,
#             'rules': [],
#             'size': 'med',
#             'traits': {'rarity': 'common',
#                        'value': ['alchemical',
#                                  'consumable',
#                                  'drug',
#                                  'injury',
#                                  'poison']},
#             'usage': {'value': 'held-in-one-hand'},
#             'uses': {'autoDestroy': True, 'max': 1, 'value': 1}},
#  'type': 'consumable'}