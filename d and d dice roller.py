import random

print('D&D Dice Roller v1.0\n')

#Fucntion for getting dice name and number

def choose_dice(name, amount):
	lowest = int(input('How many?'))
	highest = lowest * amount
	dice_list = []
	dice_list.append(name)
	dice_list.append(lowest)
	dice_list.append(highest)
	return dice_list
	
#Start the dice selection loop

select_dice = True

dice_selection = {}

while select_dice == True:
	
#Get the key from the dictionary and the items in the list at index 0
#index 1, the name of the dice and how many dice chosen
	
	for k, v in sorted(dice_selection.items()):
		print('(' + str(k)+ ') ' + str(v[1]) + str(v[0]))


	dice = int(input('''Select dice:  (1)d4  (2)d6  (3)d8  (4)d10 5)d12
	      (6)d20  (10)Finished \n'''))

#Select dice from a predefined list
	
	if dice == 1:
 
		d4 = choose_dice('d4', 4)		
		dice_selection[1] = d4
		
	if dice == 2:
		
		d6 = choose_dice('d6', 6)		
		dice_selection[2] = d6
		
	if dice == 3:
		
		d8 = choose_dice('d8', 8)		
		dice_selection[3] = d8
		
	if dice == 4:
		
		d10 = choose_dice('d10', 10)		
		dice_selection[4] = d10
		
	if dice == 5:
		
		d12 = choose_dice('d12', 12)		
		dice_selection[5] = d12
		
	if dice == 6:
		
		d20 = choose_dice('d20', 20)		
		dice_selection[6] = d20
		
	if dice == 10:
		print('Finished adding dice!')
		break
		
#Start the dice rolling loop
		
roll_dice = True

while roll_dice == True:
	
#Dynamically build the selected dice from the dictionary
	
	for k, v in sorted(dice_selection.items()):
		print('(' + str(k)+ ') ' + str(v[1]) + str(v[0]))
		
	print('(10)Exit')
	
#Roll the dice the user selects
	
	try:
		roll = int(input('\nRoll dice:'))	

	except ValueError:
		print('Enter a valid number')
		
	else:
		for k, v in dice_selection.items():

			if roll == k:
				result = random.randint(dice_selection[k][1],
				dice_selection[k][2])
					
				print('You rolled ' + str(result) + ' on a ' +
				str(dice_selection[k][1]) +  str(dice_selection[k][0]))
				
			elif roll == 10:
				roll_dice = False
	
	

