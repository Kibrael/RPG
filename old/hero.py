#Creates a hero for the game world
#v.1
#filename: Hero.py

#placeholder for item imports
#imports the d8 and d8 pool mechanics used in attribute tests
from DiceEngine import diceEngine
#create the dice engine object
dice = diceEngine()
from items import items


class hero(object):


#build a cross index of items to call them more easily IE A0 = 'robes', armor_keys = {'robes': 'AO'}
	
#using an index will also allow the typing of items by variable names
#because an item is typed only a single equip function will be required, pull the first letter of the variable name and run it against a 
#dictionary with all item types	

	#set starting values for the Hero object, often called toon
	hp = 0
	
	#holds all items that can be worn, how to handle helms?
	#armor = {'body':'none', 'head': 'none', 'hands': 'none', 'feet': 'none'}
	
	#inventory will be a multivariate array holding armor, weapons, backpack, etc.
	#inventory is the master array that holds all sub arrays
	#sub arrays show the location and/or type of gear carried
	backpack = {'torch': 3, 'rope': '50 feet'}
	carried_weapons = {'long sword': 1}
	carried_armor = {'robes': 1}
	coins = {'gold': 10, 'silver': 10, 'copper': 10}
	inventory = {}
	inventory['backpack'] = backpack
	inventory['weapons'] = carried_weapons
	inventory['carried_armor'] = carried_armor
	inventory['coins'] = coins
	#attributes refers to all the stats that can be called to resolve tests or track hero progress
	attributes = {"strength" : 4, "agility" : 0, "vitality" : 0, "intellect" : 0, "wisdom" : 0, "charisma" : 0,
	"hp": 0, "defense": 0, "dmgRedux": 0, "attack": 0, "reflex": 0, "fortitude": 0, "will": 0, 
	"level": 0, "time": 0, "status": 'none', "rHandFull": False, "lHandFull": False, 
	"armor": 'none', "helm": 'none', "gauntlets": 'none', "boots": 'none', 'weapon': 'none'
	}
	
	def print_inventory(self):
		print self.inventory
		print "You are carrying:  "
		for item in self.inventory:
			#print item
			for sub_item in  self.inventory[item]:
				print sub_item,": ", self.inventory[item][sub_item]

	
	def print_status(self):
		#prints the HP, status, accrued time, etc. of the hero
		print "\n\n", "-"*30, "\n"
		print "HP: %d, Status: %s, Def: %d, Level: %d, Time: %d" %(self.hp, self.attributes['status'], self.attributes['defense'], self.attributes['level'],
		self.attributes['time'])
		print "\n\n", "-"*30, "\n"
		
#character instantiation and hitpoint modification functions
	def __init__(self):
		hp = self.setHP(30)
		self.attributes['defense'] = 0
		
	def loseHP(self, damage):
		self.hp = self.hp - damage
		return self.hp
		
#transfers an inventory item from the target to the character inventory
#add sub segments to place it appropriately in the right inventory array IE weapons armor etc
	def take(self, target):
		stop = False
		thing = raw_input("take what? ")
	#check the item weight and compare to hero carry capacity
	
		print "The %s had: " %target.attributes['name']
#		for item in target.inventory:
#			for key in item:
#				print key, ": ", item[key]
		for item in target.inventory:
			for key in item:
				#print key #key is the name of items in different inventories
				if key == thing:
					amount = 1
					if item[key] > 1:
						amount = int(raw_input("How many do you take? :  "))
						while amount > item[key]:
							amount = int(raw_input("How many do you take? :  "))
						#substrings - string[startIndex:stopIndex]
					
					print "you took: ", key, " ", amount 
					#[item] is the number index, [key] is the item name, [item][key] is the quantity
					
					#this is where to build the matching for correct inventory placement and add item to hero's inventory
					#reference items.py for item index
					#find item in items.py, return index, split index, check first letter, assign to toon inv as appropriate
					if key == 'copper':
						print self.inventory['coins'][key]
						self.inventory['coins'][key] += amount #need to build index schema for assigning items to proper arrays
						print self.inventory['coins'][key]
						
					#print "you now have ",  self.inventory[item][stuff]," ", self.inventory[item]
					
					print "amount of item is ", item[key]
					#decrement the amount in the target inventory
					print "pre take amount is: ", item[key]
					item[key] -= amount
					print "post take amount is: ", item[key]
					
					#remove the item from inventory if it has 0 left
				
					for item in target.inventory:
						for key in item:
							if thing == key and item[key] < 1:
								print "**deletion line"
								del item[key]
								stop = True
								break	
					if stop == True:
						break
			#else:
			#	print "no such item"
#					if item[key] < 1:
#						print target.inventory[
#						print item, key, item[key], "should now be gone"
#						del key
#						#for index in target.inventory:
						#	print index[item]


							#print target.inventory
					#	print "it's all gone"
					#print self.inventory[item] #, self.inventory[item][stuff]
					
					#print self.inventory

		
	def gainHP(self, heal):
		self.hp = self.hp + heal
		return self.hp
		
	def setHP(self, health):
		self.hp = health
		return self.hp
		
#search action takes an object and returns the contents of the object's inventory	
	def search(self, target):
		
		print "The %s had: " %target.attributes['name']
		for item in target.inventory:
			for key in item:
				print key, ": ", item[key]
				#print key, ": ", target.inventory[item][key]
	def drop(self, room):
	#remove from self inventory and add to 'room' inventory
		pass
				
#add equip weapon function
	def check_hands(self):
		print self.attributes['rHandFull']
		print self.attributes['lHandFull']
		
	def sheath_weapon(self):
		#sheathing a weapon puts it back in the inventory array from the 'held' array
		#and changes the weapon attribute of the hero, which is referenced when dealing damage
		print "sheathing ", self.attributes['weapon']
		self.attributes['weapon'] == 'none'
			
	def equip_weapon(self): #getting a string name that is in a sub array
		#only one weapon at a time for now
		#sheath weapon before equipping
		weapon = raw_input("which weapon? >>")
		self.sheath_weapon()
		#use a for loop to check the name against all weapons in the master dictionary and select the right oen
		for key in items.melee_weapons:
			#print self.weapons[key]['name']
			if items.melee_weapons[key]['name'] == weapon:
				self.attributes['weapon'] = weapon
				print self.attributes['weapon'], " ready"
				if self.attributes['weapon'] == 'fists':
					print "\nlet me \n\tshow you \n\t\t   how \n\t\t\tit's done!\n"
				return
		else:
			print "no weapon found of such name"
		
#These functions should be available at all times
	def remove_armor(self):
		#removes the currently equipped armor, changing both armor name an defense attributes
		if self.attributes['armor'] == "none":
			print "not wearing any armor"
		else:
			print "removing ", self.attributes['armor']
		for key in items.all_armor:
			if items.all_armor[key]['name'] == self.attributes['armor']:
				self.attributes['defense'] -= items.all_armor[key]['defense']
		#else:
		#	print "no previous armor equipped"

		self.attributes['armor'] = 'none'

	def equip_armor(self):
	#is it better to have a separate function for each item type or to classify them in their 
	#dictionaries and equip where appropriate?
		new_armor = raw_input(">What armor?  ")
		for key in items.all_armor:
			
			if items.all_armor[key]['name'] == new_armor:
			#	print items.all_armor[key]['name']
				self.remove_armor()
				self.attributes['armor'] = new_armor
				self.attributes['defense'] = items.all_armor[key]['defense']
				print "Now wearing ", self.attributes['armor']
				self.print_status()
				#print "\n printed from equip function"
				return
		else:
			print "not a valid armor"
			print self.attributes['armor']
			print self.attributes['defense']	
	
	
	#character actions to add: print inventory, move, wait, sleep, talk, flee, drink, steal, search
	#this might be better in the main file as a general reference action for all objects
	def attack(self, enemy):
	 #use a while loop for combat
	 #if weapon used is a missile weapon, subtract ammo on attack
	 #if melee weapon and thrown, remove weapon from toon and add it to room inventory
	 #move roll inside the function
		roll = dice.rollDice(self.attributes['strength'])
		print "your attack roll is %d" % roll
		print enemy.attributes['defense']
		if roll > enemy.attributes['defense']: #this will need to be the enemy defence
			roll = dice.dEight() + self.attributes['strength']
			print "You smite your foe doing %d damage!" % roll
			enemy.loseHP(roll)
			print "the skeleton has %d hit points left\n\n\n" % enemy.hp
			
		else:
			print "You missed! \n\n\n"

	def battle(self, enemy):
		
		print "Battle is joined!"
		
		while enemy.hp > 0 and self.hp > 0:
		
			choice = raw_input("1> attack  2> run:  \n--------> ")
			print "\n"
			if choice == "1" or choice == 'attack':
				#add an initiative phase
				self.attack(enemy)
				if enemy.hp < 1:
					print "Your enemy is slain!! \n\n\n"
					enemy.alive = False
					return 'cave_entrance'
				enemy.attack(dice.rollDice(enemy.attributes['strength']), self)
				
				if self.hp < 1 and enemy.hp < 1:
					print "Two have entered, none will leave"
					return 'death'
				if self.hp < 1:
					#make death quips by type of monster
					print "You are slain \n\n\n"  
					return 'death'
						
				if enemy.hp < 1:
					#print the 'type' attribute of the monster
					print "Your enemy is slain \n\n\n"
					enemy.alive = False
					return 'cave_entrance'
			elif choice == "2":
				return 'meadow'
			else:
				print "You quake in fear. Act fool!!"
	
	#Place holder for room specific functions, how would this work if the game will be modular?
	#passing arguments....?
	#action_list = {"attack": attack()}
