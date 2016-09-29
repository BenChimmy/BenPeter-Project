from sys import exit

def final_room():
	print "This is the final room."
	print "Befor you stands Dr.Monty."
	print "What do you do?"
	
	choice = raw_input("> ")
	
	if "attack" in choice or "kill" in choice:
		print "You have defeated Dr.Monty!"
		print "You are rewarded with more treasure than you could spend in 1000 lifetimes!"
		exit(0)
	else:
		dead("The boss grabs you and swollows you whole.")
		
	

def golem_room():
	print "There is a large stone golem sleeping in front of the door."
	print "How do you plan on getting past the golem?"
	
	choice = raw_input("> ")
	
	if "sneak past" in choice or "tip-toe past" in choice:
		print "You sneak past the golem. Good job!"
		final_room()
	else:
		dead("%d was not a good choice. The golem crushes you with his fist." % choice)
	
	
def riddle_room():
	print "So, you chose door #2."
	print "There is a cloaked figure standing by the door."
	print "The figure asks you a riddle: \nWhat is something poor people have and rich people need?"
	
	answer = raw_input("> ")
	
	if answer == "nothing":
		print "That is correct. You may pass."
		final_room()
	else:
		dead("That is incorrect. You are killed by the cloaked figure.")
		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of the other door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			final_room()
		else: 
			print "I got no idea what that means."
			
def decision_room():
	print "You have made it past your first challenge."
	print "There is a small sum of gold in the room you are in."
	print "Do you take the gold or keep going?"
	
	choice = raw_input("> ")
	
	if "keep going" in choice or "continue" in choice:
		print "Good choice."
		print "There are three doors before you. which do you choose?"
		
		door = raw_input("> ")
		
		if door == "1":
			bear_room()
		elif door == "2":
			riddle_room()
		else:
			golem_room()
	else:
		dead("On your way to the gold pile you trip and fall on a pointy rock and die.")

def cyclops_room():
	print "There is a very ugly cyclops in front of you."
	print "What do you do?"
	
	choice = raw_input("> ")
	
	if "kill the cyclops" in choice or "fight the cyclops":
		print "Because the cyclops has terrible deapth perception you are able to kill it."
	else:
		dead("The cyclops kicks you. You die.")
		
def puzzle_room():
	print "The floor is covered in letters."
	print "On the far wall it says: \nI cover cities and destory mountains,\nI make men blind,\nyet help them see."
	print "..."
	print "The row off letters directly infront of you has the letters 's', 'g', 'm', and 'f'..."
	
	choice = raw_input("> ")
	
	if choice == "s":
		print "You step on the tile with an 's'. \nNothing happens."
		print "The letters now in front of you are 'o', 's, 'a', 'z'..."
		
		choice = raw_input("> ")
		
		if choice == "a":
			print "You jump onto the 'a' tile."
			print "Nothing happens."
			print "The next letters are 'q', 'r', 'f', 'n'..."
			
			choice = raw_input("> ")
			
			if choice == "n":
				print "You leap onto the 'n' tile."
				print "Nothing happens."
				print "The final row is 'k', 'd', 'y', 't'..."
				
				choice = raw_input("> ")
				
				if choice == "d":
					print "You make the jump to the 'd' tile."
					print "Nothing happens."
					print "You jump to the tile in front of the door."
					decision_room()
				else:
					dead("As you land on the %r square it crumbles under your feet. \nYou fall onto the spikes below." % choice)
			else:
				dead("You land on the %r tile. \nNothing happens for a second but then the floor falls out from under you and you plumet to your death." % choice)
		else:
			dead("You jump to the %r tile and fall through on impact. \nYou survive the fall but you are stuck in a hole with a broken leg. \nYou starve to death." % choice)
	else:
		dead("You jump onto the %r tile. Once you land yoou hear a lound rumbling noise. \nA large portion of the ceiling falls and crushes you alive." % choice)
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a small room."
	print "There is a door to your right and one to your left."
	print "Which do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		cyclops_room()
	elif choice == "right":
		puzzle_room()
	else:
		dead("You stumble aroundin the dark until you starve.")
		
start()