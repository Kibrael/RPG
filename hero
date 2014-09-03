#Creates a hero for the game world
#v.1
#filename: Hero.py
from items import armor
from DiceEngine import diceEngine
dice = diceEngine()


class hero(object):
#armor items. these should be stored in another file, hopefully a file that is read in as needed
	robes = {'type': 'armor', 'name': 'Robe', 'material': 'cloth', 'defense': 1, 'speed': 0}
	leather = {'type': 'armor', 'name': 'Leather', 'material': 'leather', 'defense': 3, 'speed': -2}
	scale = {'type': 'armor', 'name': 'scale', 'material': 'metal', 'defense': 7, 'speed': -2}
	chain_shirt = {'type': 'armor','name': 'Chain', 'material': 'metal', 'defense': 7, 'speed': -2}
	full_chain = {'type': 'armor','name': 'Chain Maille', 'material': 'metal', 'defense': 7, 'speed': -2}
	plate_mail = {'type': 'armor', 'name': 'Plate', 'material': 'metal', 'defense': 7, 'speed': -2}

		
	
	def print_status(self):
		#prints the HP, status, etc of the hero
		print "\n\n--------------------------\n"
		print "HP: %d, Status: %s, Def: %d, Level: %d, Time: %d" %(self.hp, self.attributes['status'], self.attributes['defense'], self.attributes['level'],
		self.attributes['time'])
		print "\n----------------------------\n"

#character hitpoint functions
	
	hp = 0
	equipment = {}
	weapon = {}
	armor = {}
	attributes = {"Strength" : 3, "Agility" : 0, "Vitality" : 0, "Intellect" : 0, "Will" : 0, "Charisma" : 0,
	"hp": 0, "defense": 0, "dmgRedux": 0, "attack": 0, "reflex": 0, "fortitude": 0, "will": 0, "level": 0, "time": 0, "status": 'none', "armor": 'none',
	}
	
	def __init__(self):
		hp = self.setHP(10)
		
	def loseHP(self, damage):
		self.hp = self.hp - damage
		return self.hp
		
	def gainHP(self, heal):
		self.hp = self.hp + heal
		return self.hp
		
	def setHP(self, health):
		self.hp = health
		return self.hp
		
	def attack(self, enemy):
	 #use a while loop for combat
	 #if weapon used is a missile weapon, subtract ammo on attack
	 #if melee weapon and thrown, remove weapon from toon and add it to room inventory
	 #move roll inside the function
		roll = dice.rollDice(self.attributes['Strength'])
		print "your attack roll is %d" % roll
		if roll > 9: #this will need to be the enemy defence
			roll = dice.dEight() + self.attributes['Strength']
			print "You smite your foe doing %d damage!" % roll
			enemy.loseHP(roll)
			print "the skeleton has %d hit points left\n\n\n" % enemy.hp
			
		else:
			print "You missed! \n\n\n"

	def equip(self, item):
		#check to see if toon has the item being equipped
		#check to see if the item is armor, weapon or other, equip as appropriate
		#remove old defense modifier
		#how do I pass a string and pull a dictionary tuple/hash?
		#armors = {'scale': self.scale, 'plate': self.plate_mail}
		
		if item == 'scale':
			#self.attributes['armor'] = self.scale['name']
			#self.attributes['defense'] += self.scale['defense']
			
			#remove_armor(self)
			equip_scale(self)
			print self.attributes['defense']
			print "You equipped %s armour" % self.attributes['armor']
		else:
			print "fail to equip, that's probably not armour."
			
			
	def battle(self, enemy):
		print "Battle is joined!"
		
		while enemy.hp > 0 and self.hp > 0:
		
			choice = raw_input("1> attack  2> run:  \n--------> ")
			print "\n"
			if choice == "1":
				#add an initiative phase
				self.attack(enemy)
				enemy.attack(dice.rollDice(enemy.attributes['Strength']), self)
				
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
		
	#passing arguments....?
	#action_list = {"attack": attack()}
