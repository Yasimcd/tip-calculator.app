print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
percentage = tip / 100
difference = bill * percentage
total = difference + bill
people = int(input("How many people to split the bill?"))
payment = total / people
new_payment = round(payment, 2)
new_payment = "{:.2f}".format(payment)
print(f"Each person should pay:${new_payment}")

