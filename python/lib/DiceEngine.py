#Creates a dice rolling object that uses groups of 8 sided dice
#v.1
#filename: DiceEngine.py
import random

class diceEngine(object):
	def __init__(self):
		"""
		"""

		self.att_roll_map = {
				9:{
				"dice": 4,
				"method": "high"
				},
				7:{
				"dice": 3,
				"method": "high"
				},
				5:{
				"dice": 2,
				"method": "high"
				},
				3:{
				"dice": 3,
				"method": "low"
				},
				1:{
				"dice": 4,
				"method": "low"
				}

			}
		
	def dice_roll(self, num_dice, die_size=8):
		"""
		num_dice: the number of dice to roll
		die_size: the size of the dice to roll for all dice
		return: list of roll outcomes
		"""
		die_rolls = []
		for die in range(0, num_dice):
			die_rolls.append(random.randrange(1, die_size))

		return die_rolls
		
	def map_att_to_dice(self, attribute, skill, boon):
		"""
		"""

		#calculate dice pool size and rolling method
		pool_total = attribute + boon + skill

		#use pool total to determine total dice and method
		dice_to_roll = self.att_roll_map[pool_total]["dice"]
		dice_method = self.att_roll_map[pool_total]["method"]

		#roll dice and return a list
		dice_results = self.dice_roll(num_dice=dice_to_roll)
		print(dice_results)
		#sort dice results for return
		if dice_method == "low":
			dice_results = sorted(dice_results)
		elif dice_method == "high":
			dice_results = sorted(dice_results, reverse=True)
		
		dice_sum = dice_results[0] + dice_results[1]

		return {"result":dice_sum, "method": dice_method, 
				"dice_results": dice_results, "pool_total":pool_total}
		#returns the dice pool chosen as text and the result, 
			#and the total including skill and boon bonuses
		#maps a passed attribute using self.
		#att_roll_map to determine which dice pool to use

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
