temp1 = 32
celsius1 = (temp1 - 32) * 5/9
print(celsius1)

temp2 = 77
celsius2 = (temp2 - 32) * 5/9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5/9
print(celsius3)

print("---------------------------------------")

def feherenit_to_celsius(temp):
    celsius = (temp - 32) * 5/9
    return celsius

print(feherenit_to_celsius(32))
print(feherenit_to_celsius(77))
print(feherenit_to_celsius(50)) 