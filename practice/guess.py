#猜数字游戏
#wang daka

from random import randint

def start():
	while True:
		global begin
		print('Welcome to the game')
		begin = input('1.文艺版\n2.傻逼版\n3.文明版\n')
		if begin == '1' or begin == '2' or begin == '3':
			begin == 1
			break
		else:
			print("你是不是瞎？")


#得到随机数
def get(numbers):
	i = 0
	while i < 3 :
		get_number = randint(0,21)
		if get_number not in numbers:
			numbers.append(get_number)
			i = i + 1
	numbers.sort()


def show(next):      #循环控制
	while int(next) == 1:
		numbers =[]
		get(numbers)
		i = 0
		while i < 3:
			print('The number is bigger than :' +str(numbers[0]))
			print('The number is small than :' + str(numbers[-1]))
			try:
				inp = int(input('Please enter the number you guess: '))
			if inp > numbers[1]:
				print('Too big')
				if inp < numbers[-1]:
					numbers[-1] = inp
					print('You are the way to succeed!')
				i = i + 1
				continue
			if inp == numbers[1]:
				print('赢了xie,憋嚣张')
				print('来啊，按Y啊，牛逼的人都继续！！！')
				print('怂逼按N')
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
				i = i + 1
		if i > 2:
			print("你输了，骚年！")
			print("给你机会，再来一局！")
			next = input()
			if next == 'y' or next == 'Y':
				next = 1
			else:
				next = 0
start()
show(begin)
