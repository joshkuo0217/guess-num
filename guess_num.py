import random
r = random.randint(1, 100)
while True:
	r_input = input('請輸入一個0到100之間的數字: ')
	r_input = int(r_input)
	if r == r_input:
		print('恭喜!答對了')
		break
	elif r != r_input:
		if r_input < r:
			print(r_input, '比答案還小')
		elif r_input > r:
			print(r_input, '比答案還大')