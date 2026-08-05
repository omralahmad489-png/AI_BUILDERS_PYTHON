#dictionaries : ordered, changeable, does not allow duplicates

my_dic = {
    "name" : "Omar" ,
    "age" : 20,
}

print(my_dic)
print(type(my_dic))
print(len(my_dic))

#accessing items in the dictionary
print(my_dic["age"])
print(my_dic["name"])

#change item in the dictionary
my_dic["name"] = "Ali"
print(my_dic)

#add new item to the dictionary
my_dic.update({"gender" : "male"})
print(my_dic)

my_dic.update({"gender" : "female"})
print(my_dic)

my_dic["age"] = 21
print(my_dic)

#remove item from the dictionary

my_dic.pop("age")
print(my_dic)

print(my_dic["gender"])