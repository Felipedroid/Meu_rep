year = int (input('Digite um ano:'))

if (year % 4) == 0:
	if (year % 100) == 0:
		if (year % 400) == 0:
			print(year, 'É um ano bissexto')
		else:
			print(year, 'Não é um ano bissexto')
	else:
		print (year, 'É um ano bissexto')
else:
	print(year, 'não é um ano bissexto')
	
