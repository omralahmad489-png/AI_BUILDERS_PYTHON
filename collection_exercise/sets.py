#sets: unchangeable, unordered, no duplicate values

set1 = {1, 2, 3, 4, 5}

print(type(set1))
print(len(set1))
print(set1)

print("---------------------------------------")

#add new item to the set
set1.add(6)
print(set1)

print("---------------------------------------")

#add sets to another set
set2 = {'bannana', 'cherry', 'kiwi'}
set1.update(set2)
print(set1)

print("---------------------------------------")

#remove item from the set

set1.remove('cherry')
print(set1)

print("---------------------------------------")

#discard item from the set
set1.discard('kiwi')
print(f"Discards_Items : {set1}")