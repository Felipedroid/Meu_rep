
nterms= 10

# primeiros dois número da sequência

n1 = 0
n2 = 1
count = 0

print("Sequencia fibonacci vai até", nterms, ":")
while count < nterms:
	print (n1, end = ', ')
	ntm = n1 + n2
	
	#Atualização de valores
	n1 = n2
	n2 = ntm
	count += 1
print ()
