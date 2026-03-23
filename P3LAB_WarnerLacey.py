#Lacey Warner
#P3LAB
#21Mar2026
#This program converts a dollar amount into the number of dollars, quarters, dimes, nickels, and pennies.







#This is the amount the user wants to convert
amount = float(input("Enter amount of money: "))

#Convert to cents to make math easier
cents = int(round(amount * 100))

#Calculate denominations for each unit
dollars = cents // 100
cents %= 100

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

#This is the output results
if dollars > 0:
    print(f"{dollars} dollar" if dollars == 1 else f"{dollars} dollars")
if quarters > 0:
    print(f"{quarters} quarter" if quarters == 1 else f"{quarters} quarters")
if dimes > 0:
    print(f"{dimes} dime" if dimes == 1 else f"{dimes} dimes")
if nickels > 0:
    print(f"{nickels} nickel" if nickels == 1 else f"{nickels} nickels")
if pennies > 0:
    print(f"{pennies} penny" if pennies == 1 else f"{pennies} pennies")
if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
    print("No change given.")