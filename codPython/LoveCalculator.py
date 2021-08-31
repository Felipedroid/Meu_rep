print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

mixName = name1 + name2
lowerCase = mixName.lower()

true = lowerCase.count('t') + lowerCase.count('r') + lowerCase.count('u') + lowerCase.count('e')
love = lowerCase.count('l') + lowerCase.count('o') + lowerCase.count('v') + lowerCase.count('e')

x = str(true) + str(love)
final = int(x)

if final < 10 or final > 90:
  print (f"Your score is {final}, you go together like coke and mentos.")
elif final > 40 and final < 50:
  print(f"Your score is {final}, you are alright together.")
else:
  print(f"Your score is {final}.")
  