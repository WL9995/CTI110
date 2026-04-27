#Lacey Warner
#04/27/2026
#P5LAB
#This program simulates a self-checkout machine. It generates a random total owed, accepts user payment, calculates change, and displays the breakdown of coins and dollars.





import random




#Convert to cents to avoid floating point issues
def disperse_change(change):
    #Handles zero change given
    cents = int(round(change * 100 ))
    if cents == 0:
        print("No Change owed.")
        
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
    print("\nChange to be returned:")
    if dollars > 0:
        print(f"Dollars: {dollars}")
    if quarters > 0:
        print(f"Quarters: {quarters}")
    if dimes > 0:
        print(f"Dimes: {dimes}")
    if nickels > 0:
        print(f"Nickels: {nickels}")
    if pennies > 0:
        print(f"Pennies: {pennies}")
    if change == 0:
        print("No change owed.")






#Function for generating random amount due
def main():
    #This generates random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${total_owed:.2f}")

    #User input for payment
    amount_paid = float(input("Enter amount of cash provided: $"))

    #Confirm payment amount
    if amount_paid < total_owed:
        print("Insufficient payment. Transaction cancelled.")
        return

    #Calculate change amount
    change = round(amount_paid - total_owed, 2)
    print(f"Change owed: ${change:.2f}")

    #Give change amount
    disperse_change(change)





#Call main function
main()