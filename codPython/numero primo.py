num = int(input("Digite um número:"))

flag = 1
for i in range (2, num):
	if (num % i) == 0:
		print (num, "não é um numero primo.")
		print (i, "multiplicado por", num//i, "é", num)
		flag = 0
		break
if flag == 1:
	print(num, "é um numero primo.")
