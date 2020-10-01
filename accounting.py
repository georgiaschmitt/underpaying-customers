


#Add comments explaining what your code is doing.

#Read over the solution and see how it compairs to your answer.


melon_cost = 1.00 # This sets the melon cost to one dollar

def customer_pay(file): # this establishes a new function that takes in a file
"""This calculates from a text file the customers who did not pay the expected amount and prints
what they paid and what they were expected to pay"""
    the_file = open(file) # This opens the the file and stores it to a variable
    for line in the_file: # For each line in this file
        line = line.rstrip() # This eliminates the extra white space at the end of each line.
        words = line.split('|') # Creates a list of each line in the file, separated by "|"
        custnum, custname, nummelons, custpaid = words # This unpacks the list and creates 4 variables
        custpaid = float(custpaid) # This type changes the amount that the customer paid into a float
        custexp = int(nummelons) * float(melon_cost) # This calculates the expected customer payment
        if custexp != custpaid: # This figures out if the customer didn't pay the expected amount
            print(f"{custname} paid ${custpaid:.2f},", # This prints the customer's name,
            f"expected ${custexp:.2f}" #how much they paid, and how much they were expected to pay


# If customer overpaid, print that they've overpaid for their melons. If
        # customer underpaid, print that they've underpaid for their melons.
        if custexp < custpaid:
            print(f"{custname} has overpaid for their melons.")

        elif custexp > custpaid:
            print(f"{custname} has underpaid for their melons.")

    # Close the file
    payment_data.close()

customer_pay("customer-orders.txt") # This calls the function

