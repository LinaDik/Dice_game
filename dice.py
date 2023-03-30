from random import randint



print("Привет! Добро пожаловать в игру в кости! У кого выпадет большее число тот и выиграл. Максимальное число - 6.\n  Участвовать можно двум игрокам.")

amount_win_p1 = 0
amount_win_p2 = 0

ready = str(input("Вы готовы? Введите 'да'. После ввода слова готовности будут кинуты кубики и вы узнаете их значения: "))




while ready=="да":
	fpn=randint(1, 6)
	spn=randint(1, 6)
	print("Первому игроку выпало число", fpn)
	print("Второму игроку выпало число", spn)
	if fpn>spn:
		print("Первый игрок победил!")
		amount_win_p1+=1
		print("Победы первого игрока: ", amount_win_p1)
		print("Победы второго игрока: ", amount_win_p2)
		ready = str(input("\n\n\nПродолжить? Введите да: "))
		continue
	elif spn>fpn:
		print("Второй игрок победил!")
		amount_win_p2+=1
		print("Победы первого игрока: ", amount_win_p1)
		print("Победы второго игрока: ", amount_win_p2)
		ready = str(input("\n\n\nПродолжить? Введите да: "))
	elif fpn==spn:
		print("Ничья!")
		print("Победы первого игрока: ", amount_win_p1)
		print("Победы второго игрока: ", amount_win_p2)
		ready = str(input("\n\n\nПродолжить? Введите да: "))


