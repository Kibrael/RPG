#Contains the classes to make different monsters. Rawr
#v.1
#filename: Monsters.py

#Holds monster classes and creates them 
#v.1
#Filename: Monsters.py
#make an inventory generating function
from DiceEngine import diceEngine
from Hero import hero
from items import items
dice = diceEngine()
items = items()

class monster(object):
	toon = hero()
	alive = True
	attributes = {"strength" : 0, "agility" : 0, "vitality" : 0, "intellect" : 0, "wisdom" : 0, "charisma" : 0,
	"hp": 0, "defense": 0, "dmgRedux": 0, "attack": 0, "reflex": 0, "fortitude": 0, "will": 0, 'name': 'skeleton', 'type': 'undead', 
	'XP_value': 50,
	}
	#when searching inventory, type and quantity are important, define the item elsewhere
	#build the inventory from the item class
	M1 = {'name':'skeleton teeth'}
	M2 = {'name': 'broken bits of bone'}
	
	misc = {'skeleton teeth': 5, 'broken bits of bone': 3}
	carried_weapons = {'long sword': 1}
	armor = {'scale': 1}
	coins = {'copper': 6, 'silver': 1}
	carried_armor = {'robes': 1}
	weapons = {'long sword': 1}
	
	inventory = [coins, armor, weapons, misc]
	
class skeleton(monster):

	def __init__(self):
		self.hp = 20
		self.attributes['strength'] = 3
		self.attributes['agility'] = 3
		self.attributes['vitality'] = 2
		self.attributes['dmgRedux'] = 2
		self.attributes['reflex'] = 3
		self.attributes['defense'] = 8
		
	def gainHP(self, health):
		self.hp = self.hp + health
		
	def loseHP(self, health):
		self.hp = self.hp - health
		
	def attack(self, roll, toon):
	 #use a while loop for combat
		
		print "the skeleton's attack roll is %d" % roll
		print toon.attributes['defense']
		if roll > toon.attributes['defense']: #this will need to be the enemy defense
			roll = dice.dEight() 
			print "The skeleton smites you doing %d damage!" % roll
			toon.loseHP(roll)
			#print "you have %d hit points left\n\n\n" % toon.hp
			
		else:
			print "You dodged!\n\n\n"
