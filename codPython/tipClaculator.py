print ("Welcome to the tip calculator")
bill = float (input("What was the total bill? $"))
tip = int (input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int (input("How many people to split the bill? "))

tipP = tip / 100
totalBill = bill * tipP + bill

payment = totalBill/people
finalPayment = round(payment, 2)
finalPayment = "{:.2f}".format(payment) 
print (f"Each person should pay: ${finalPayment}")