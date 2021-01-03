  
# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your 8% rate when computing the amount of tax owing.
# Compute the tip as %18 of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places and € currency.

while True:
    try:
        cost_meal = float(input ("How much did the meal cost?(!!in euros pls!!)"))
        break

    except ValueError:
        print("please give a number!(!!in euros pls!!)")
        continue
    


tax = 8 / 100 * cost_meal
tax = ("%.2f" % tax)

tip = 18 / 100 * cost_meal
tip = ("%.2f" % tip)

total = float(tax) + cost_meal + float(tip)
total = ("%.2f" % total)

print ("Tax: ", "€", tax)
print ("Tip: ", "€", tip)
print ("Total: ", "€", total)
