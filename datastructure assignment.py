#1
students = {
    "Ram": "ram@example.com",
    "Sita": "sita@example.com",
    "Laxman": "laxman@example.com"
}

name = input("Enter student name: ").strip().title()
if name in students:
    print(students[name])
else:
    print("contact not found")
#2
shopping_list = {"Milk", "Bread", "Eggs"}
bought = {"Bread", "Eggs"}

unbought = shopping_list - bought

if not unbought:
    print("Shopping complete")
else:
    print("Items remaining:", unbought)
#3
class_list = ["ram", "sita", "laxman"]
new_student = input("Enter new student name: ").strip().lower()

if new_student in class_list:
    print("Already present message")
else:
    class_list.append(new_student)
    print("Student added successfully") 
#4
votes = ["Blue", "Red", "Blue", "Green", "Blue"]
blue_count = votes.count("Blue")

if blue_count >= 3:
    print("Blue wins")
else:
    print("Blue did not win")
#5
grades = {"Ram": 92, "Sita": 88}
name = input("Enter student name: ").strip().title()

if name in grades:
    print(grades[name])
else:
    print("Grade is not available")
#6
applicant = {
    "name": "Priya",
    "skills": ["Java", "SQL"],
    "experience_years": 1
}

required_skills = {"Python", "Java"}

if (any(skill in applicant["skills"] for skill in required_skills) and 
    applicant["experience_years"] >= 2):
    print("priya qualifies")
else:
    print("priya does not qualify")
#7
banned_items = {"scissors", "knife", "lighter"}
item = input("Enter item name: ").strip().lower()
weight = float(input("Enter weight in kg: "))

if weight <= 7 and item not in banned_items:
    print("Bag allowed")
else:
    print("Bag not allowed")
#8
emp = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Shyam', 'salary': 500}
}

emp['emp3']['salary'] = 8500
print(emp)
#9
ram_items = {"apple", "banana", "rice"}
laxman_items = {"banana", "mango", "rice"}

common = ram_items & laxman_items

if not common:
    print("they picked completely different items")
else:
    print("they have some common items")
#10
data = [10, 20, 30]
zone_b = 20
val = 25  # Example value

if val in data:  # Step 1: Universal Validity Check
    if 'b' in {'a': 1, 'b': 2} and val != zone_b:  # Step 2 & 3
        print("Path A")
    else:
        print("Path B")
else:
    print("Path C")
#11
data = {'a': 10, 'b': 20, 'a': 30}
print(data)  # {'a': 30, 'b': 20} → Last value wins
#16
menu = {"Pizza": 15, "Burger": 10, "Salad": 8}
order = input("Enter item: ").strip().title()

if order in menu:
    print(menu[order])
else:
    print("item not found")
#17
student_data = {"name": "Sam", "score": 85}

if student_data["score"] >= 80:
    student_data["status"] = "Pass"
else:
    student_data["status"] = "Review"

print(student_data)
#18
database = {"admin": "1234", "user": "abcd"}

user_input = "admin"
user_pass = "1234"

if user_input in database and database[user_input] == user_pass:
    print("Login Successful")
else:
    print("Login Failed")
#19
emails = ["ram123@gmail.com", "hari77@gmail.com"]
blacklisted_emails = {"hari77@gmail.com"}
current_email = "hari77@test.com"

if current_email in emails and current_email not in blacklisted_emails:
    print("Email Sent")
elif current_email in blacklisted_emails:
    print("Blocked")
else:
    print("safe")
#20
inventory = {'A1': 50, 'B2': 0, 'C3': 10}
restricted_zones = {'B2', 'Z9'}
target = 'B2'

if target in inventory:
    if target not in restricted_zones and inventory[target] > 0:
        print("dispatch item")
    else:
        print("invalid zone")
else:
    print("stock error")
#21
valid_courses = {"python", "robotics", "java"}
hs_grades = list(range(9, 13))  # 9 to 12

name = input("Enter name: ")
course = input("Enter course: ").lower()
grade = int(input("Enter grade: "))

if course not in valid_courses:
    print("selected an invalid course")
elif grade not in hs_grades:
    if grade < 9:
        print(f"{name} is not eligible for {course} grade too low")
    else:
        print(f"{name} is not eligible for {course} grade too high")
elif course == "robotics" and grade == 9:
    print(f"{name} is not eligible for {course}")
else:
    print(f"{name} is approved for {course}")
    