#猜数字游戏
#wang daka

from random import randint

def start():
	print('Welcome to the game')



#得到随机数
def get(numbers):
	i = 0
	while i < 3 :
		get_number = randint(0,21)
		if get_number not in numbers:
			numbers.append(get_number)
			i = i + 1
	numbers.sort()
def show():
	next = 1      #循环控制
	while next == 1:
		numbers =[]
		get(numbers)
		while True:
			print('The number is bigger than :' +str(numbers[0]))
			print('The number is small than :' + str(numbers[-1]))
			inp = int(input('Please enter the number you guess: '))
			if inp > numbers[1]:
				print('Too big')
				if inp < numbers[-1]:
					numbers[-1] = inp
					print('You are the way to succeed!')
				continue
			if inp == numbers[1]:
				print('You win')
				print('Enter Y to get a new game')
				print('Enter N to ending')
				next = input()
				if next == 'y' or next == 'Y':
					next = 1
					break
				else:
					next = 0
					break	
			if inp < numbers[1]:
				print('Too small')
				if inp > numbers[0]:
					numbers[0] = inp
					print('You are the way to succeed!')
show()