##### MAILING #####
print ("Sayın Köksal Berkay Denktaş \n ayak sokağı 89 \n N: 5 \n Didim 7896 \n Türkiye")
##### MAILING #####


##### ASKING NAME #####
name = input ("What is your name?")
print ("Hello! " + name)
##### ASKING NAME #####


##### AREA #####
width = float(input("Please enter the width of the room in decimals and meters."))
length = float(input("Please enter the length of the room in decimals and meters."))
area = length * width 
area = ("%.2f" % area) # limiting the numbers after the decimal
print ("The area of the room is " + str(area) + " square meters")
##### AREA #####


##### CONTAINER BOTTLE #####
number_big_bottles = int(input("How many big containers do you have?"))
number_small_bottles = int(input("How many small containers do you have?"))

money_for_small_bottles = number_small_bottles * 0.10
money_for_big_bottles = number_big_bottles * 0.25

total_deposit = money_for_small_bottles + money_for_big_bottles
total_deposit = ("%.2f" % total_deposit)
print ("your deposit is ", "$", total_deposit)
##### CONTAINER BOTTLE #####


##### N stuff #####
# n * (n + 1) / 2
n = int (input ("Please give a positive number"))
output = n * (n+1) / 2
print (int(output))
##### N stuff #####


##### widgets and gizmos #####
number_of_gizmos = int(input("How many gizmos did you buy?"))
number_of_widgets = int(input("How many widgets did you buy?"))

weight_gizmos = 112
weight_widgets = 75

total_weight_gizmos = weight_gizmos * number_of_gizmos
total_weight_widgets = number_of_widgets * weight_widgets

total_weight = total_weight_gizmos + total_weight_widgets
print ("The total weight is", total_weight, "grams")
##### widgets and gizmos #####


##### Money #####
money_deposited = float(input("How much money did you deposit?"))

the_interest = 4 / 100 * money_deposited
money_after_1_year = money_deposited + the_interest

the_interest_2 = 4 / 100 * money_after_1_year
money_after_2_years = money_after_1_year + the_interest_2

the_interest_3 = 4 / 100 * money_after_2_years
money_after_3_years = money_after_2_years + the_interest_3

money_after_1_year = ("%.2f" % money_after_1_year)
money_after_2_years = ("%.2f" % money_after_2_years)
money_after_3_years = ("%.2f" % money_after_3_years)

print(float(money_after_1_year))
print(float(money_after_2_years))
print(float(money_after_3_years))
##### Money #####
 