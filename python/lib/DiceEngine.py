#Creates a dice rolling object that uses groups of 8 sided dice
#v.1
#filename: DiceEngine.py
import random

class diceEngine(object):
	def __init__(self):
		"""
		"""

		self.att_roll_map = 
			{
				:
			}
		
	def dice_roll(self, num_dice, die_size=8):
		"""
		num_dice: the number of dice to roll
		die_size: the size of the dice to roll for all dice
		return: list of roll outcomes
		"""
		die_rolls = []
		for die in num_dice:
			die_rolls.append(random.randrange(1, die_size))

		return die_rolls
		

	def rollDice(self, attribute): #number range must be 1 to 5
		if attribute == 1:
			lst = []
			result = 0
			for n in range(0,4):
				lst.append(self.dEight())
			lst = sorted(lst)
			return lst[0] + lst[1]
			
		elif attribute == 2:
			lst = []
			result = 0
			for n in range(0,3):
				lst.append(self.dEight())
			lst = sorted(lst)
			return lst[0] + lst[1]
			
		elif attribute == 3:
			result = self.dEight() + self.dEight()
			return result
		elif attribute == 4:
			lst = []
			result = 0
			for n in range(0,3):
				lst.append(self.dEight())
			lst = sorted(lst)
			return lst[2] + lst[1]
			
		elif attribute == 5:
			lst = []
			result = 0
			for n in range(0,4):
				lst.append(self.dEight())
			lst = sorted(lst)
			return lst[2] + lst[3]
			
		else:
			print("must be in range 1 to 5")
