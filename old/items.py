#holds all the item tables
#build a section to red in a set of items from a file/database
#filename: items.py

class items(object):

	attributes = {'name': 'blank', 'type': '', 'defense': 0, 'damage': 0}
	all_armor = {}
	melee_weapons = {}
	ranged_weapons = {}
	all_misc = {}
	coins = {'gold': 0, 'silver': 0, 'copper': 0}
	
	#Armor items, all have an index beginning with A followed by a number 
	A0 = {'name': 'robes', 'type': 'armor', 'material': 'cloth', 'defense': 1, 'speed': 0}
	A1 = {'name': 'leather', 'type': 'armor', 'material': 'leather', 'defense': 2, 'speed': -2}
	A2 = {'name': 'scale', 'type': 'armor', 'material': 'metal', 'defense': 6, 'speed': -2}
	A3 = {'name': 'chain shirt', 'type': 'armor', 'material': 'metal', 'defense': 4, 'speed': -2}
	A4 = {'name': 'chain maille', 'type': 'armor', 'material': 'metal', 'defense': 8, 'speed': -2}
	A5 = {'name': 'plate mail', 'type': 'armor', 'material': 'metal', 'defense': 12, 'speed': -2}
	armor_list = [A0, A1, A2, A3, A4, A5]
	
	#weapons items, indexed by W and then a number
	W0 = {'name': 'shield', 'damage': 1, 'weight': 5, 'defense': 3, 'hands': 'one', 'type': 'melee', 'reload': 0, 'range': 10, 'speed': 1}
	W1 = {'name': 'dagger', 'damage': 2, 'weight': 1, 'defense': 0, 'hands': 'one', 'speed': 1, 'range': 10, 'reload': 0, 'type': 'melee'}
	W2 = {'name': 'short sword', 'damage': 3, 'weight': 2, 'defense': 0, 'hands': 'one', 'speed': 0, 'range': 10, 'reload': 0, 'type': 'melee'}
	W3 = {'name': 'long sword', 'damage': 4, 'weight': 4, 'defense': 0, 'hands': 'one', 'speed': -1, 'range': 10, 'reload': 0, 'type': 'melee'}
	W4 = {'name': 'zweihander', 'damage': 6, 'weight': 10, 'defense': 0, 'hands': 'both', 'speed': -1, 'range': 10, 'reload': 0, 'type': 'melee'}
	W5 = {'name': 'fists', 'damage': 1, 'weight': 0, 'defense': 0, 'hands': 'both', 'speed': -1, 'range': 10, 'reload': 0, 'type': 'melee'}
	melee_list = [W0, W1, W2, W3, W4, W5]
	

	
	
	#add items into master dictionary using loops
	#set counter 
	n = 0
	while n < 6:
		all_armor["A"+str(n)] = armor_list[n]
		n+=1
		
	#reset counter
	n = 0
	while n < 6:
		melee_weapons["W"+str(n)] = melee_list[n]
		n+=1
	

	# this was test code: below
	#for item in melee_weapons:
	#	melee_weapons[item] = "W"+item
	
	#use this loop function to make the index for items, do not use an index of numbers it is duplicative
	#index = {}
	#n=0
	#while n < 4:
	#	index["A"+str(n)] = all_armor[str(n)]['name']
	#	n += 1
		#could use this loop to fill all index lists simultaneously, might have to pad with blanks or use
		#an if statement to cut some item types out of the loop if there are not the same amount.
		
