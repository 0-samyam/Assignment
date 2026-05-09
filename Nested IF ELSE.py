import math

# Q4. Student Resource Portal
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "ad123":
        print("Access Granted: Faculty Dashboard")
    else:
        print("Invalid Credentials. Please try again.")
elif username == "student":
    if password == "st2026":
        print("Access Granted: Notes and Practice Questions")
    else:
        print("Invalid Credentials. Please try again.")
else:
    print("Invalid Credentials. Please try again.")


# Q5. Traffic Light System
light = input("Enter light color (red/yellow/green): ").strip().lower()

if light == "red":
    print("Stop!")
elif light == "yellow":
    print("Get Ready / Slow Down!")
elif light == "green":
    print("Go!")
else:
    print("Error: Invalid color. Please enter red, yellow, or green.")


# Q6. Match statement for seasons
number = int(input("Enter a number (1-4): "))

match number:
    case 1:
        print("Spring")
    case 2:
        print("Summer")
    case 3:
        print("Autumn")
    case 4:
        print("Winter")
    case _:
        print("Unknown")


# Q7. Bank Loan Approval System
age = int(input("Enter age: "))
income = float(input("Enter monthly income: Rs. "))
credit_score = int(input("Enter credit score: "))

if age >= 21 and age <= 60:
    if income >= 30000:
        if credit_score >= 700:
            print("Loan Approved!")
        else:
            print("Loan Denied: Credit score must be at least 700.")
    else:
        print("Loan Denied: Monthly income must be at least Rs. 30,000.")
else:
    print("Loan Denied: Age must be between 21 and 60.")


# Q8. Movie Theatre Ticket Booking System
age = int(input("Enter your age: "))

if age < 12:
    print("Ticket Price: Free")
elif age >= 12 and age <= 60:
    membership = input("Do you have a membership card? (yes/no): ").strip().lower()
    if membership == "yes":
        print("Ticket Price: Rs. 150")
    else:
        print("Ticket Price: Rs. 200")
else:
    print("Ticket Price: Rs. 100 (Senior Citizen Discount)")


# Q9. Employee Bonus
salary = float(input("Enter your salary: Rs. "))
years = int(input("Enter years of service: "))

if years > 5:
    bonus = salary * 0.05
    print(f"Net Bonus Amount: Rs. {bonus:.2f}")
else:
    print("You are not eligible for a bonus (requires more than 5 years of service).")


# Q10. Compute the area of a circle
radius = float(input("Enter the radius of the circle: "))

if radius < 0:
    print("Error: Radius cannot be negative.")
else:
    area = math.pi * radius ** 2
    print(f"Area of Circle: {area:.2f}")


# Q11. Wage Calculation
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").strip().upper()
days = int(input("Enter number of days worked: "))

if age >= 18 and age < 30:
    if gender == "M":
        wage_per_day = 700
    elif gender == "F":
        wage_per_day = 750
    else:
        wage_per_day = 0
        print("Invalid gender entered.")
elif age >= 30 and age <= 40:
    if gender == "M":
        wage_per_day = 800
    elif gender == "F":
        wage_per_day = 850
    else:
        wage_per_day = 0
        print("Invalid gender entered.")
else:
    wage_per_day = 0
    print("Age is outside the valid range (18-40).")

if wage_per_day > 0:
    total_wages = wage_per_day * days
    print(f"Wage per day: Rs. {wage_per_day}")
    print(f"Total Wages for {days} day(s): Rs. {total_wages}")


# Q12. FizzBuzz
number = int(input("Enter a number: "))

if number % 3 == 0:
    if number % 5 == 0:
        print("Fizz Buzz")
    else:
        print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)


# Q13. Electricity Bill Calculator
units = float(input("Enter electricity usage (units): "))

if units < 0:
    print("Error: Units cannot be negative.")
elif units < 100:
    cost = units * 5
    print(f"Total Electricity Bill: Rs. {cost:.2f}")
elif units <= 300:
    cost = (100 * 5) + ((units - 100) * 8)
    print(f"Total Electricity Bill: Rs. {cost:.2f}")
else:
    cost = (100 * 5) + (200 * 8) + ((units - 300) * 10)
    print(f"Total Electricity Bill: Rs. {cost:.2f}")


# Q14. Rock Paper Scissors
p1 = input("Player 1 - Enter your move (rock/paper/scissors): ").strip().lower()
p2 = input("Player 2 - Enter your move (rock/paper/scissors): ").strip().lower()

valid_moves = ["rock", "paper", "scissors"]

if p1 in valid_moves and p2 in valid_moves:
    if p1 == p2:
        print("It's a Tie!")
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "scissors" and p2 == "paper") or \
         (p1 == "paper" and p2 == "rock"):
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")
else:
    print("Invalid move entered. Please enter rock, paper, or scissors.")


# Q15. Positive Even/Odd Check
number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("The number is Positive and Even.")
    else:
        print("The number is Positive and Odd.")
else:
    print("The number is not positive.")


# Q16. Store Discount
total_amount = float(input("Enter total purchase amount: Rs. "))

if total_amount > 1000:
    is_member_input = input("Are you a member? (yes/no): ").strip().lower()
    if is_member_input == "yes":
        discount = total_amount * 0.20
        print("20% discount applied!")
    else:
        discount = total_amount * 0.10
        print("10% discount applied!")
    final_amount = total_amount - discount
    print(f"Discount Amount: Rs. {discount:.2f}")
    print(f"Final Amount to Pay: Rs. {final_amount:.2f}")
else:
    print("No discount applicable.")
    print(f"Final Amount to Pay: Rs. {total_amount:.2f}")


# Q17. Weight Conversion (Updated Gravity values from PDF)
print("Planets: 1=Mercury  2=Venus  3=Mars  4=Jupiter  5=Saturn  6=Uranus  7=Neptune")
earth_weight = float(input("Enter your Earth weight (kg): "))
planet = int(input("Enter planet number (1-7): "))

if planet == 1:
    planet_name, gravity = "Mercury", 0.38
elif planet == 2:
    planet_name, gravity = "Venus", 0.91
elif planet == 3:
    planet_name, gravity = "Mars", 0.38
elif planet == 4:
    planet_name, gravity = "Jupiter", 2.53
elif planet == 5:
    planet_name, gravity = "Saturn", 1.07
elif planet == 6:
    planet_name, gravity = "Uranus", 0.89
elif planet == 7:
    planet_name, gravity = "Neptune", 1.14
else:
    planet_name = None
    print("Invalid planet number.")

if planet_name:
    weight_on_planet = earth_weight * gravity
    print(f"Your weight on {planet_name}: {weight_on_planet:.2f} kg")


# Q18. Marks and Grade
s1 = float(input("Enter marks of Subject 1: "))
s2 = float(input("Enter marks of Subject 2: "))
s3 = float(input("Enter marks of Subject 3: "))
s4 = float(input("Enter marks of Subject 4: "))

total = s1 + s2 + s3 + s4
percentage = total / 4

print(f"Total Marks : {total} / 400")
print(f"Percentage  : {percentage:.2f}%")

if percentage > 70:
    print("Grade: Distinction")
elif percentage > 60:
    print("Grade: First Class")
elif percentage > 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")


# Q19. ATM Simulation
balance = 5000.0
correct_pin = 123
is_valid = True # Assuming card is valid as per PDF

if is_valid:
    pin = int(input("Enter your PIN: "))
    if pin == correct_pin:
        print("PIN accepted. Welcome!")
        while True:
            print("\n1. Withdraw\n2. Check Balance\n3. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                amount = float(input("Enter amount to withdraw: Rs. "))
                if amount <= balance:
                    balance -= amount
                    print(f"Rs. {amount:.2f} withdrawn successfully.")
                else:
                    print("Insufficient balance.")
            elif choice == 2:
                print(f"Current Balance: Rs. {balance:.2f}")
            elif choice == 3:
                print("Thank you for visiting!")
                break
            else:
                print("Invalid option.")
    else:
        print("Wrong PIN. Access denied.")
else:
    print("Invalid card.")


# Q20. Magic Forest (Updated to follow PDF Flowchart)
print("Welcome to the Magic Forest!")
direction = input("1. GO NORTH OR SOUTH? ").strip().upper()

if direction == "NORTH":
    path_choice = input("2. CROSS THE RIVER OR FOLLOW THE PATH? ").strip().upper()
    if path_choice == "FOLLOW THE PATH":
        creature = input("3. CHOOSE: FAIRY, OGRE, OR ELF? ").strip().upper()
        if creature == "ELF":
            print("YOU WIN")
        elif creature == "FAIRY" or creature == "OGRE":
            print("GAME OVER")
        else:
            print("DISPLAY: INVALID CHOICE. END.")
    elif path_choice == "CROSS THE RIVER":
        print("DISPLAY: CROSS THE RIVER. END. GAME OVER")
    else:
        print("Invalid choice.")
elif direction == "SOUTH":
    print("DISPLAY: SOUTH. END. GAME OVER")
else:
    print("Invalid direction.")


# Q21. Smart Elevator (Updated to follow PDF Flowchart)
floor = int(input("Enter floor number (0-10): "))

if 0 <= floor <= 10:
    weight = float(input("Enter weight (kg): "))
    if weight <= 500:
        door_status = input("Is the door closed? (yes/no): ").strip().lower()
        if door_status == "yes":
            print("ACTIVATE ELEVATOR MOTION.")
        else:
            print("DISPLAY: WARNING: CLOSE THE DOOR.")
    else:
        print("DISPLAY: OVERWEIGHT: LIFT CANNOT MOVE.")
else:
    print("DISPLAY: INVALID FLOOR.")


# Q22. Facebook Account Creation (New based on PDF Page 9)
print("--- Facebook: Create a New Account ---")
first_name = input("First name: ").strip()
last_name = input("Last name: ").strip()

if first_name != "" and first_name.isalpha() and last_name != "" and last_name.isalpha():
    email = input("Email address: ").strip()
    if "@" in email and "." in email:
        re_email = input("Re-enter email address: ").strip()
        if re_email == email:
            password = input("New password: ").strip()
            if len(password) >= 6:
                print("Sign Up Successful!")
            else:
                print("Error: Password must be at least 6 characters.")
        else:
            print("Error: Emails do not match.")
    else:
        print("Error: Invalid email format.")
else:
    print("Error: Names must not be empty and should contain letters only.")
