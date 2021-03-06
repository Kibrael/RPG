import random #for dice engine
from sys import exit # to quit the game on death

from DiceEngine import diceEngine #for random rolls by d8 distribution
from Monsters import monster #holds the monster classes and their action functions and equipment/attribute dictionaries
from Monsters import skeleton #specific monster import
from Hero import hero #hero class and its actions, equipment and attributes

#from items import items



attributes = {1: "low4d8",
			2: "low3d8",
			3: "2d8",
			4: "high3d8",
			5: "high4d8",
}
def print_actions():
	print "\n\nActions:\n(f)orward, (b)ack, (a)ttack, (w)ear, (s)earch, (t)ake, (r)eady weapon (i)nventory, (q)uit, (help)print actions"

def action_calls(action, scene, forward, back):
	
	#print actions
	if action == "help":
		print_actions()
		return scene
		
	#move forward
	elif action == "f":
		return forward
	
	#move back one room
	elif action == "b":
		return back
	
	#print inventory
	elif action == "i" or action == "inv" or action == "inventory":
		toon.print_inventory()
		return scene
		
	#wear armor
	elif action == "w":
		toon.equip_armor()
		return scene
		
	#ready a weapon	
	elif action == "r":
		toon.equip_weapon()
		return scene
		
	#quit playing	
	elif action == "q":
		return 'death'
	
	#take something
	#fix targeting to message if invalid object
	elif action == "t":
		target = raw_input("take from where?  ")
		toon.take(game_objects[target])
		return scene
		
	#fight!
	#fix messaging if target is invalid
	elif action == "a":
		enemy = raw_input("who is your enemy?  ")
		toon.battle(game_objects[enemy])
		#print scene
		return scene
		
	
	elif action == "s":
		#need a way to show what can be searched
		target = raw_input("search what? ")
		toon.search(game_objects[target])
		return scene
		
	else:
		print "not a valid action"
		return scene
		
class Scene(object):
	#this is the base scene that all other scenes pull basic properties from. 
	#add in stuff to communicate with hero class here
	#each room scene will need its own inventory
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)


	
#The Engine class runs the game with a while loop
class Engine(object):

    def __init__(self, scene_map):
        #print "Engine has scene_map", scene_map
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        #print "Play's first scene", current_scene
	

        while True:
            toon.print_status()
            next_scene_name = current_scene.enter()
            #print "next scene", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
            #print "map returns new scene", current_scene
			

	
class Death(Scene):
	
	def enter(self):
		print "Well, you died. That sucks for you, but someone else lived."
		exit(1)


class Meadow(Scene):
	#first entrance

	def enter(self):
		"""Needs two cases, one for the first entrance, another for coming back"""
		entry_string = """\r\rThe meadow is sun dappled and smells of orange blossoms. \nThere is a cave entrance nearby. You can hear a low keening coming from the mouth of the cave"""
		
		#these are the movement control variables for the scene
		forward = 'cave_entrance'
		back = 'meadow'
		scene = 'meadow'
		
		print entry_string
		#toon.print_status()
		#print_actions()
		action = 0
		while action <> 'q':
			#"f)forward, b)back, w)wear, s)search, t)take, r)ready weapon q)Quit, help)print actions"
			action = raw_input("What do you do? ")
			return action_calls(action, scene, forward, back)
			
class CaveEntrance(Scene):
	#need a way to flag if skeleton is gone

	
	def enter(self):
		forward = 'win'
		back = 'meadow'
		scene = 'cave_entrance'
		
		if skeleton.alive == True:
			
			entry_string = """As you enter the cave, a skeleton confronts you. It brandishes its sword and gnashes its terrible teeth"""
			print entry_string
			
			
			action = 0
			while action <> 'q':
			#"f)forward, b)back, w)wear, s)search, t)take, r)ready weapon q)Quit, help)print actions"
				action = raw_input("What do you do? ")
				return action_calls(action, scene, forward, back)
		

		else:
			entry_string = """The shattered bones of a skeleton lie on the cavern floor"""
			print entry_string, "Do you proceed deeper into the cave?"
			action = 0
			#print_actions()
			
			while action <> 'q':
			#"f)forward, b)back, w)wear, s)search, t)take, r)ready weapon q)Quit, help)print actions"
				action = raw_input("What do you do? ")
				return action_calls(action, scene, forward, back)
				
			else:
				print "you need to lock user inputs better"
				return 'meadow'
		print "pass through of cave entrance"
		return cave_entrance
		
class Win(Scene):
	def enter(self):
		print "You are so intrepid"
		exit(1)
	
#The map class contains a list of all the scenes in the game
#Scenes are held in a dictionary that passes them to functions based on return values in other classes

class Map(object):
	#scenes: meadow - test scene for new functions, cave entrance tests battle, search - must add search function, read inventory of 
	#object referenced by passed string
	#add a town scene to test talk, steal, buy functions
	#death prints death lines
	scenes = {
		'meadow': Meadow(), 
		'cave_entrance': CaveEntrance(), 
		'win': Win(),
		'death': Death(),
		
	}
		
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)		

cave_entrance_visited = False
#armor = armor()

skeleton = skeleton()

#syntax or reading the keys and values from a dictionary
#for key, value in armor.scale:
#	print key, value
#	#print armor.scale.get(key)

#stuff = 'name'
#print armor.scale[stuff]	
toon = hero()
game_objects = {}
game_objects['skeleton'] = skeleton
#print "armor type is: ", toon.scale.get('name')

dice = diceEngine()	
a_map = Map('meadow')
a_game = Engine(a_map)
a_game.play()

