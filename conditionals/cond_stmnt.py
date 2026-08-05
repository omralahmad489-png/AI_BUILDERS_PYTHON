a = 10
b = 20

if a < b:
    print("a is less than b")
elif a > b : 
    print ("a greater than b")
else :
    print("a is equal to b")
    
print("---------------------------------------")       

#nested if 

x = 13

if x > 10 :
    print("x is greater than 10")
    if x > 20 :
        print("also x is greater than 20")
    else : 
        print("but it not greater than 20")
else:
    print("x is not greater thant 10")