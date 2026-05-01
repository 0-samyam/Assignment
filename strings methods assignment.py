# Q1. Display patient name in title format
name = input("Enter patient name: ")
print(name.title())

# Q2. Convert password to lowercase for comparison
password = input("Enter password: ")
print(password.lower())

# Q3. Display movie name in title case
movie = "spider-man no way home"
print(movie.title())

# Q4. Display heading in ALL CAPS
heading = "annual sports day"
print(heading.upper())

# Q5. Swap every letter's case
sentence = "hELLO wORLD"
print(sentence.swapcase())


# Q6. Find first position of word 'error' in log message
log = "System error detected, error code 404"
print(log.find("error"))

# Q7. Check if email ends with '@gmail.com'
email = input("Enter email: ")
print(email.endswith("@gmail.com"))

# Q8. Count how many times 'free' appears in message
message = input("Enter message: ")
print(message.count("free"))

# Q9. Check if URL starts with 'https'
url = input("Enter URL: ")
print(url.startswith("https"))

# Q10. Check if 'Python' is present in resume text
resume = input("Enter resume text: ")
print("Python" in resume)

# Q11. Find exact position of 'FAILED' using index()
transaction = "Transaction FAILED due to low balance"
print(transaction.index("FAILED"))

# Q12. Check if file is a PDF using endswith()
filename = input("Enter filename: ")
print(filename.endswith(".pdf"))

# Q13. Check if phone number starts with Nepal code '+977'
phone = input("Enter phone number (numbers only, min 10 digits): ")
if phone.isdigit() and len(phone) >= 10:
    print(phone.startswith("977"))
else:
    print("Invalid phone number. Enter numbers only with at least 10 digits.")

# Q14. Check if URL belongs to government website
url = input("Enter URL: ")
print(url.endswith(".gov.np/"))


# Q15. Clean customer feedback with extra spaces
feedback = "   Great service!   "
print(feedback.strip())

# Q16. Replace banned word 'hate' with '****'
chat = "I hate this, hate it completely"
print(chat.replace("hate", "****"))

# Q17. Remove leading slashes from filename
filename = "///student_records.pdf "
print(filename.lstrip("/"))

# Q18. Clean trailing spaces and symbols from price
price = "Price: $120.33 "
print(price.rstrip(" ").rstrip())

# Q19. Remove dashes from phone number
phone = "+977 984-123-4567"
print(phone.replace("-", ""))


# Q20. Split CSV student data into individual fields
data = input("Enter student data (Name,Age,Address,Studying): ")
fields = data.split(",")
field_names = ["Name", "Age", "Address", "Studying"]
for i in range(len(fields)):
    print(field_names[i] + ": " + fields[i])

# Q21. Join hashtags with # prefix
tags = "Python, Coding, Nepal, Tech"
tag_list = tags.split(", ")
print(" ".join("#" + tag for tag in tag_list))

# Q22. Split passenger names and count total
passengers = "Ram, Shyam, Hari, Sita"
passenger_list = passengers.split(", ")
print(len(passenger_list))

# Q23. Join words to form a sentence
words = ["The", "flight", "departs", "at", "6AM"]
print(" ".join(words))


# Q24. Validate age contains only digits
age = input("Enter age: ")
print(age.isdigit())

# Q25. Check username contains only letters and numbers
username = input("Enter username: ")
print(username.isalnum())

# Q26. Check student name contains only alphabets
student_name = input("Enter name: ")
print(student_name.isalpha())

# Q27. Check if PIN is all uppercase letters
pin = input("Enter PIN: ")
print(pin.isupper())

# Q28. Check if user entered only spaces
field = input("Enter value: ")
print(field.isspace())