import random
start = input('請決定隨機數字開始值: ')
end = input('請決定隨機數字結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count = count + 1 # count += 1 為快寫法
	r_input = input('請輸入一個介於{}與{}之間的數字: '.format(start, end))
	r_input = int(r_input)
	if r == r_input:
		print('恭喜!你答對了,這是你猜的第', count, '次呦')
		break
	elif r != r_input:
		if r_input < r:
			print(r_input, '比答案還小')
		elif r_input > r:
			print(r_input, '比答案還大')
	print('這是你猜的第', count, '次呦')