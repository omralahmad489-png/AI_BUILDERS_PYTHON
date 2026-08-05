numbers = [1, 2, 3, 4 ,5 ,6 ,7, 8, 9, 10]
even_numbers = [number for number in numbers if number % 2 ==0]
print(even_numbers)

odd_numbers = [number for number in numbers if number %2 !=0]
print(odd_numbers)

print("---------------------------------------")
#taking the item that contains the letter "n" in the list
fruit_list = ["apple", "banana", "cherry", "kiwi", "mango"]
new_fruitlist = [x for x in fruit_list if "n" in x]
print(new_fruitlist)


print("---------------------------------------")

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#greater than 5 list
new_list5=[x for x in numbers_list if x>5]
print(new_list5)

squared_list = [x**2 for x in numbers_list if x % 2 ==0] 
print(squared_list)


print("---------------------------------------")

ranging_list =[x for x in range(11)]
print(ranging_list)

#slicing 
print(ranging_list[0:5]) # first 5 elements
print(ranging_list[5:]) # elements from index 5 to end