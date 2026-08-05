mylist =[1, 2, 3 ,4 ,4]
print(type(mylist)) # list data type
print(mylist[0])
print(len(mylist)) # length of the list

#add item to the list
mylist.append(5)
print(mylist)

#remove item from the list
mylist.remove(4)
print(mylist)

#remove at last index
mylist.pop()
print(mylist)

#remove a specific index
# mylist.pop(2)
# print(mylist)

#clear the list
# mylist.clear()
# print(mylist)

#add list to another list
fruit_list = ["apple", "banana", "cherry"]
mylist.extend(fruit_list)
print(mylist)