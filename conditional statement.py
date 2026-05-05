# 1. Check whether the given number is in between 1 and 100 or not.
def problem1():
    number = int(input("Enter a number: "))
    if 1 <= number <= 100:
        print(f"{number} is between 1 and 100")
    else:
        print(f"{number} is NOT between 1 and 100")

# 2. Check whether the user input number is even or odd and display it to user.
def problem2():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is EVEN")
    else:
        print(f"{number} is ODD")

# 3. Write a program that asks the user for a number in the range of 1 to 12 and display the corresponding month.
def problem3():
    months = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    
    month_num = int(input("Enter a month number (1-12): "))
    
    if month_num in months:
        print(f"Month: {months[month_num]}")
    else:
        print("Error: Please enter a number between 1 and 12")

# 4. A school has following rules for grading system. Ask user to enter marks and print the corresponding grade.
def problem4():
    marks = int(input("Enter marks: "))
    
    if marks < 25:
        grade = "F"
    elif marks < 45:
        grade = "E"
    elif marks < 50:
        grade = "D"
    elif marks < 60:
        grade = "C"
    elif marks < 80:
        grade = "B"
    else:
        grade = "A"
    
    print(f"Marks: {marks}, Grade: {grade}")

# 5. Write a program to check whether a number is divisible by 7 or not.
def problem5():
    number = int(input("Enter a number: "))
    if number % 7 == 0:
        print(f"{number} is divisible by 7")
    else:
        print(f"{number} is NOT divisible by 7")

# 6. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
def problem6():
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    operator = input("Enter operator (+, -, *, /): ")
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero")
            return
    else:
        print("Error: Invalid operator")
        return
    
    print(f"Your Answer is: {result}")

# 7. Write a Python program to check car loan eligibility: Salary >= 50,000 and Credit Score >= 700.
def problem7():
    salary = float(input("Enter your salary: "))
    credit_score = int(input("Enter your credit score: "))
    
    if salary >= 50000 and credit_score >= 700:
        print("Eligible")
    else:
        print("Not Eligible")

# 8. Write a Python program that checks if a number is divisible by 3 and 5 (FizzBuzz).
def problem8():
    n = int(input("Enter a number: "))
    
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)

# 9. Write a Python program that takes a character input and checks whether it is a vowel or consonant.
def problem9():
    char = input("Enter a character: ").lower()
    
    if char.isalpha():
        if char in "aeiou":
            print(f"{char} is a VOWEL")
        else:
            print(f"{char} is a CONSONANT")
    else:
        print("Error: Please enter a valid character")

# 10. Write a Python program to input marks and determine the grade based on the following conditions.
def problem10():
    marks = int(input("Enter marks: "))
    
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    else:
        grade = "Fail"
    
    print(f"Grade: {grade}")

# 11. Write a Python program to categorize a person's age: Child, Teenager, or Adult.
def problem11():
    age = int(input("Enter age: "))
    
    if age < 13:
        category = "Child"
    elif age <= 19:
        category = "Teenager"
    else:
        category = "Adult"
    
    print(f"Category: {category}")

# 12. Write a Python program to check if a given character is uppercase, lowercase, or a digit.
def problem12():
    char = input("Enter a character: ")
    
    if char.isupper():
        print(f"{char} is UPPERCASE")
    elif char.islower():
        print(f"{char} is LOWERCASE")
    elif char.isdigit():
        print(f"{char} is a DIGIT")
    else:
        print(f"{char} is a special character")

# 13. Write a Python program that takes a color as input and outputs the corresponding action.
def problem13():
    color = input("Enter color (Red, Yellow, Green): ").capitalize()
    
    if color == "Red":
        action = "Stop"
    elif color == "Yellow":
        action = "Get Ready"
    elif color == "Green":
        action = "Go"
    else:
        print("Error: Invalid color")
        return
    
    print(f"Action: {action}")

# 14. Write a Python program to check eligibility for a job based on age and experience.
def problem14():
    age = int(input("Enter your age: "))
    experience = int(input("Enter years of experience: "))
    
    if age > 18 and experience >= 2:
        print("Eligible")
    else:
        print("Not Eligible")

# 15. Write a Python program to give advice based on the temperature.
def problem15():
    temp = float(input("Enter temperature in °C: "))
    
    if temp > 30:
        advice = "It's hot, stay hydrated!"
    elif temp >= 15:
        advice = "Enjoy the weather!"
    else:
        advice = "It's cold, wear warm clothes!"
    
    print(advice)

# 16. Write a Python program that takes a menu option and prints its price.
def problem16():
    item = input("Enter item (Pizza, Burger, Pasta): ").capitalize()
    
    menu = {
        "Pizza": 10,
        "Burger": 7,
        "Pasta": 8
    }
    
    if item in menu:
        print(f"{item}: ${menu[item]}")
    else:
        print("Error: Item not in menu")

# 17. Write a Python program to select players based on height.
def problem17():
    height = float(input("Enter height in feet: "))
    
    if height >= 6:
        print("Selected")
    else:
        print("Not Selected")

# 18. Write a Python program to check if a person is eligible to watch a movie based on their age.
def problem18():
    age = int(input("Enter your age: "))
    
    if age >= 18:
        print("Allowed")
    else:
        print("Not Allowed")

# 19. Write a Python program to check login credentials.
def problem19():
    correct_username = "admin"
    correct_password = "password123"
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Access Granted")
    else:
        print("Access Denied")

# 20. Write a Python program that takes a month number (1–12) and outputs the corresponding season.
def problem20():
    month_num = int(input("Enter month number (1-12): "))
    
    if month_num in [12, 1, 2]:
        season = "Winter"
    elif month_num in [3, 4, 5]:
        season = "Spring"
    elif month_num in [6, 7, 8]:
        season = "Summer"
    elif month_num in [9, 10, 11]:
        season = "Autumn"
    else:
        print("Error: Please enter a number between 1 and 12")
        return
    
    print(f"Season: {season}")