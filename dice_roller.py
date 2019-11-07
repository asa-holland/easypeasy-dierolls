import random

ON = True
print('\nWelcome to the simple die roller! Type a die size to receive a random result.\n')
while ON:
	try:
		dice_size = int(input('Die size: '))
		result = str(random.randint(1, dice_size))
		print (f'Result: {result}\n')
	except:
		print('Error! Die size is an integer.\n')
		
		