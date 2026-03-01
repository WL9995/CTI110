#Lacey Warner
#26Feb2026
#P1HW2
#This program calculates and displays travel expenses





#User Information
budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas: "))
accomodation = int(input("Approximately, how much do you expect to spend on accomodation/hotel? "))
food = int(input("How much do you expect to spend on food? "))
print(" ")


#Time delay to make it look like the program is calculating expenses.
print("Calculating expenses...")
import time
time.sleep(3)
print("Calculations complete!")


#This is what we call a sneaky joke
if"hawaii" in destination.lower():
    print("You can't drive to Hawaii silly goose!")
    exit()

#Calculations
total_expenses = gas + accomodation + food
remaining_budget = budget - total_expenses


#Output Budget
print("This program calculates and displays travel expenses")
print(f"Budget: {budget}")
print(f"Travel Destination: {destination}")
print(f"Gas Expenses: {gas}")
print(f"Accomodation Expenses: {accomodation}")
print(f"Food Expenses: {food}")
print(" ")


#Output Final
print("------------Travel Expenses------------")
print("Location: " + destination)
print(f"Initial Budget: {budget}")
print(" ")
print("Fuel: " + str(gas))
print("Accomodation: " + str(accomodation))
print("Food: " + str(food))
print(" ")
print("Remaining balance: " + str(remaining_budget))




#Start program

#Ask user for budget
#store budget as a variable
#Ask user for travel destination
#store destination as a variable
#Ask user for estimated gas expenses
#store gas expenses as a variable
#Ask user for estimated accomodation expenses
#store accomodation expenses as a variable
#Ask user for estimated food expenses
#store food expenses as a variable

#Print "calculating expenses" statement
#Run 3 second time delay to make program look to be functioning
#Print "Calculations complete!" statement

#Check user input for desination
#If hawaii print "You can't drive to Hawaii silly goose!" and exit program

#Calculate total expenses
#Gas + Accomodation + Food = Total Expenses
#Budget - total expenses = remaining budget

#Print "This program calculates and displays travel expenses"
#Print budget, destination, gas expenses, accomodation expenses, food expenses on new lines each

#Print "------------Travel Expenses------------"
#Print "Location: " + destination name
#Print "Initial Budget: " + budget amount
#Print "Fuel: " + gas cost
#Print "Accomodation: " + accomodation cost
#Print "Food: " + food cost
#Print "Remaining balance: " + remaining budget amount






