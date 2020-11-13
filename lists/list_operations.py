motorbikes = ["honda" , "yamaha" , "suzuki"]
print (motorbikes)

# changing the element by index.
motorbikes[1] = "ducati"
print (motorbikes)

# adding an element to the list by the append   #method#
motorbikes.append("yamaha")
print (motorbikes)

# adding an element to a particular position in a list with insert method
motorbikes.insert(0, "java")
print (motorbikes)

# Removing an item using the del keyword.
del motorbikes[0]
print (motorbikes)

# Removing items using the pop method
motorbikes.insert(0, "java") # java inserted again
print (motorbikes)

# pop() method default removes the last item
removed_item = motorbikes.pop()
print (removed_item)
print (motorbikes)
duplicated_list = [1 , 1 , 1 , 1]

# we can define which item to be popped.
removed_item = motorbikes.pop(0)
print (removed_item)
print (motorbikes)

# Empty lists
my_empty_list = []
my_empty_list.append("Paris")

