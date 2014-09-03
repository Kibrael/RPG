#holds all the item tables
#build a section to red in a set of items from a file/database
#filename: items.py

class items(object):

	attributes = {'name': 'blank', 'type': '', 'defense': 0, 'damage': 0}
	
		
	def stuff(self):
		print "this is stuff"
		
class armor(items):
	robes = {'type': 'armor', 'name': 'Robe', 'material': 'cloth', 'defense': 1, 'speed': 0}
	leather = {'type': 'armor', 'name': 'Leather', 'material': 'leather', 'defense': 3, 'speed': -2}
	scale = {'type': 'armor', 'name': 'scale', 'material': 'metal', 'defense': 7, 'speed': -2}
	chain_shirt = {'type': 'armor','name': 'Chain', 'material': 'metal', 'defense': 7, 'speed': -2}
	full_chain = {'type': 'armor','name': 'Chain Maille', 'material': 'metal', 'defense': 7, 'speed': -2}
	plate_mail = {'type': 'armor', 'name': 'Plate', 'material': 'metal', 'defense': 7, 'speed': -2}
	
		
class weapons(items):
	long_sword = {'name': 'Long Sword', 'damage_type': 'slashing', 'damage': 4, 'speed': -1, 'range': 10, 'reload': 0, 'type': 'melee'}
	short_sword = {'name': 'Long Sword', 'damage_type': 'slashing', 'damage': 3, 'speed': 0, 'range': 10, 'reload': 0, 'type': 'melee'}
	dagger = {'name': 'Long Sword', 'damage_type': 'slashing', 'damage': 2, 'speed': 1, 'range': 10, 'reload': 0, 'type': 'melee'}
	knife = {'name': 'Long Sword', 'damage_type': 'slashing', 'damage': 1, 'speed': 1, 'range': 10, 'reload': 0, 'type': 'melee'}
	short_bow = {'name': 'Long Sword', 'damage_type': 'slashing', 'damage': 4, 'speed': 1, 'range': 15, 'reload': 1, 'type': 'missile'}
	long_bow = {'name': 'Long Sword', 'damage_type': 'slashing', 'damage': 4, 'speed': 0, 'range': 20, 'reload': 2, 'type': 'missile'}
	crossbow = {'name': 'Long Sword', 'damage_type': 'slashing', 'damage': 4, 'speed': 3, 'range': 20, 'reload': 3, 'type': 'missile'}
	
class potions(items):
	pass
	
class scrolls(items):
	pass
	
	
class magic(object):
	pass
	
