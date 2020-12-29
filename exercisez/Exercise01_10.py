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