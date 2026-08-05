# while condition is true:
#     execute this block of code

i = 1 
while i < 6 :
    print(i)
    if i == 3 : 
        break #exit the loop when i is equal to 3
    i += 1

print("---------------------------------------")

y = 0
while y < 6 :
    y += 1
    if y ==3 : 
        continue #continue to the next iteration if i is equal to 3
    print(y)