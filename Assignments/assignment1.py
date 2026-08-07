students =[
    {"name":"Lara","age":23,"track":"AI","hours_studied":40,"scores":[85,90,78]},
    {"name":"Omar","age":31,"track":"Data","hours_studied":12,"scores":[60,55,70]},
    {"name":"Rim","age":27,"track":"AI","hours_studied":55,"scores":[95,88,92]},
    {"name":"Karim","age":19,"track":"Web","hours_studied":8,"scores":[50,65,40]},
    {"name":"Nour","age":25,"track":"AI","hours_studied":30,"scores":[75,80,85]},
    {"name":"Sami","age":35,"track":"Data","hours_studied":48,"scores":[88,91,79]},
    ]

print("---------------------------------------")
print("Part 1")
print("--------")
#print the first name and last name student 

# First and Last student names
print(f"First Name : {students[0]['name']}") 
print(f"Last Name : {students[5]['name']}\n") 


# scores
print(f"Rims Scores : {students[2]['scores']}\n")

#loop
for student in students:
    print(f"{student['name']} is {student['age']} years old and studies {student['track']}")
    
print("---------------------------------------")  
print("Part 2")
print("--------")

#filtering
ai_tracking_list = []
for student in students:
    if student["track"] == "AI" :
        ai_tracking_list.append(student)
        
print(f"The AI Tracking Student is about : {len(ai_tracking_list)} students\n")

        
ai_tracking_list = [student for student in students if student["track"] == "AI"]
print(f"The AI Tracking Student is about : {len(ai_tracking_list)} students\n")


#names of students who study more than 30 hour

studies_hour_list =[student["name"] for student in students if student["hours_studied"] > 30] 
print(f"Students who study more than 30 hours : {studies_hour_list}\n")

#student who is older older than 24 AND in the AI track

student_24old_AI = [student["name"] for student in students if student["age"] > 24 and student["track"] == "AI" ]
print(f"Students who are older than 24 and in the AI track : {student_24old_AI}")

print("---------------------------------------")
print("Part 3")
print("--------")

#average age of all student
average_age = sum([student["age"] for student in students]) / len(students)
print(f"The average age of all students is : {average_age}\n")

#total hours studied across the whole cohort
total_hours = sum(student["hours_studied"] for student in students)
print(f"The total hours studied across the whole cohort is : {total_hours}\n")

#study the most hours
max_hours = [student["name"] for student in students if student["hours_studied"] == max(student["hours_studied"] for student in students)]

print(f"The student who studies the most hours is : {max_hours}\nHours studied : {max(student['hours_studied'] for student in students)}\n")

# Final grade for each student is the average of their scores
for student in students:
    average_score = sum(student['scores']) / len(student['scores'])
    print(f"{student['name']} : {average_score : .1f}")

print("---------------------------------------")
print("Part 4")
print("--------")

#new list for only two keys "name" and "average_score"

new_list = [{"name": student["name"], "average_score": sum(student["scores"]) / len(student["scores"]) } for student in students]
print(f"New List : {new_list}\n")

#maps each track to the number of students

new_dict = {}
for student in students:
    track = student["track"]
    if track in new_dict:
        new_dict[track] += 1
    else:
        new_dict[track] = 1
print(f"New Dictionary : {new_dict}\n")



# Since sets is unchangeable, unordered, no duplicate values
# so it make the data safer because values cannot be accidentally modified.

#set of all unique track

set1 = {student["track"] for student in students}
print(f"Set of all unique track : {set1}\n")

print("---------------------------------------")
print("Part 5")
print("--------")


#reusable functions
def  filter_by_track(students, track) :
    result = [student["name"] for student in students if student["track"] == track]
    return result

print(filter_by_track(students, "AI"))
print(filter_by_track(students, "Data"))

print()

#average score function
def average_score(name):
    for student in students :
        if student["name"] == name :
            average = sum(student["scores"]) / len(student["scores"])
            return average
print(average_score("Sami"))

print()

#function calling function
def top_student(students):
    max_score = max(sum(student["scores"]) / len(student["scores"]) for student in students) 
    top_student = [student["name"] for student in students if sum(student["scores"]) / len(student["scores"]) == max_score]
    return top_student , max_score
print(top_student(students))


 
print()



#summary
def summary(students):
    total_student = len(students)
    average_age = sum(student["age"] for student in students) / total_student
    track = {student["track"] for student in students}
    return total_student, average_age, track
print(summary(students))
    
   




