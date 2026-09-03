# 1. Create and write student information

'''file = open("student.txt", "w")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")
file.write("Branch: " + branch + "\n")
file.write("Semester: " + semester + "\n")

file.close()

print("Student information saved successfully.")'''


#2. Display complete contents of a text file
file = open("student.txt", "r")

content = file.read()

print("File Contents:")
print(content)

file.close()

#3. Append Information in file
'''file = open("student.txt", "a")

name = input("Enter additional student name: ")
roll = input("Enter roll number: ")

file.write("\nName: " + name)
file.write("\nRoll Number: " + roll)

file.close()'''

print("Information appended successfully.")

#4. Read file line by line
file = open("student.txt", "r")

for line in file:
    print(line.strip())

file.close()

#5.  count and display the total number of lines present in a text file. 
file = open("student.txt", "r")

lines = file.readlines()

print("Total number of lines:", len(lines))

file.close()

#6. Count total number of words

file = open("student.txt", "r")

content = file.read()
words = content.split()

print("Total number of words:", len(words))

file.close()

#7.  count the total number of characters in a text file, including spaces

file = open("student.txt", "r")

content = file.read()

print("Total number of characters:", len(content))

file.close()

#8. Display lines in reverse order
file = open("student.txt", "r")

lines = file.readlines()

print("Lines in reverse order:")

for line in reversed(lines):
    print(line.strip())

file.close()

#9. Count vowels and consonants
file = open("student.txt", "r")

content = file.read()

vowels = 0
consonants = 0

for ch in content:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)

file.close()

#10. Count alphabets, digits, spaces and special characters

file = open("student.txt", "r")

content = file.read()

alphabets = 0
digits = 0
spaces = 0
special = 0

for ch in content:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    elif ch != "\n":
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

file.close()

#11. Find the longest word
file = open("student.txt", "r")

content = file.read()
words = content.split()

longest = max(words, key=len)

print("Longest word:", longest)
print("Length:", len(longest))

file.close()

#12. Count occurrence of each word using dictionary

file = open("student.txt", "r")

content = file.read().lower()
words = content.split()

word_count = {}

for word in words:
    word = word.strip(".,!?")
    
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Occurrences:")

for word, count in word_count.items():
    print(word, ":", count)

file.close()


#13. Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears. 

file = open("student.txt", "r")

search_word = input("Enter word to search: ").lower()

count = 0
line_numbers = []

for line_number, line in enumerate(file, start=1):
    words = line.lower().split()
    
    for word in words:
        word = word.strip(".,!?")
        
        if word == search_word:
            count += 1
            line_numbers.append(line_number)

file.close()

print("Number of occurrences:", count)
print("Line numbers:", line_numbers)

#14. Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file
'''file = open("student.txt", "r")

content = file.read()

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

content = content.replace(old_word, new_word)

file.close()

file = open("student_new.txt", "w")
file.write(content)
file.close()

print("Word replaced successfully.")
print("Modified content saved in student_new.txt")'''

#15.  Read a Python source file and create another file after removing single-line comments. 
file = open("sample.py", "r")

lines = file.readlines()

file.close()

output = open("program-without-comments.py", "w")

for line in lines:
    if not line.strip().startswith("#"):
        output.write(line)

output.close()

print("Comments removed successfully.")

#16. Create another file containing uppercase text
file = open("student.txt", "r")

content = file.read()

file.close()

output = open("uppercase.txt", "w")

output.write(content.upper())

output.close()

print("Uppercase file created successfully.")

#17. Student record
'''
file = open("student.txt", "r")

lines = file.readlines()

file.close()

students = []

for line in lines[1:]:
    data = line.strip().split(",")

    roll = data[0]
    name = data[1]
    marks = int(data[2])

    students.append([roll, name, marks])

# Display all records
print("All Student Records:")

for student in students:
    print(student)

# Highest marks
highest = max(students, key=lambda x: x[2])

print("\nStudent with highest marks:")
print(highest)

# Average marks
total = sum(student[2] for student in students)
average = total / len(students)

print("\nAverage marks:", average)

# Students scoring more than 80
print("\nStudents scoring more than 80:")

for student in students:
    if student[2] > 80:
        print(student)
'''
#18. Employee record with function
def read_employees():
    file = open("employees.txt", "r")

    employees = []

    for line in file:
        data = line.strip().split(",")

        emp_id = data[0]
        name = data[1]
        department = data[2]
        salary = float(data[3])

        employees.append([emp_id, name, department, salary])

    file.close()

    return employees


def display_employees(employees):
    print("\nAll Employees:")

    for emp in employees:
        print(emp)


def highest_paid(employees):
    employee = max(employees, key=lambda x: x[3])

    print("\nHighest Paid Employee:")
    print(employee)


def average_salary(employees):
    total = sum(emp[3] for emp in employees)
    average = total / len(employees)

    print("\nAverage Salary:", average)


def above_salary(employees, salary):
    print("\nEmployees earning above", salary)

    for emp in employees:
        if emp[3] > salary:
            print(emp)


employees = read_employees()

display_employees(employees)

highest_paid(employees)

average_salary(employees)

salary = float(input("\nEnter salary limit: "))
above_salary(employees, salary)


#19. Student attendance
file = open("attendance.txt", "r")

print("Students with attendance below 75%:")

for line in file:
    data = line.strip().split(",")

    roll = data[0]
    name = data[1]
    present = int(data[2])
    total = int(data[3])

    percentage = (present / total) * 100

    print(name, "Attendance:", percentage, "%")

    if percentage < 75:
        print("Below 75%:", name)

file.close()

#20. deposits and withdrawal

file = open("transactions.txt", "r")

total_deposits = 0
total_withdrawals = 0
transactions = []

for line in file:
    data = line.strip().split(",")

    transaction_type = data[0]
    amount = float(data[1])

    transactions.append(amount)

    if transaction_type == "deposit":
        total_deposits += amount

    elif transaction_type == "withdrawal":
        total_withdrawals += amount

file.close()

final_balance = total_deposits - total_withdrawals

largest_transaction = max(transactions)

print("Total Deposits:", total_deposits)

#21. Book Record Management 
def load_books():
    file = open("books.txt", "r")

    books = []

    for line in file:
        data = line.strip().split(",")

        books.append(data)

    file.close()

    return books


def save_books(books):
    file = open("books.txt", "w")

    for book in books:
        file.write(",".join(book) + "\n")

    file.close()


def add_book(books):
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    books.append([book_id, title, author, "Available"])

    save_books(books)

    print("Book added successfully.")


def search_book(books):
    book_id = input("Enter Book ID to search: ")

    for book in books:
        if book[0] == book_id:
            print("Book Found:", book)
            return

    print("Book not found.")


def issue_book(books):
    book_id = input("Enter Book ID to issue: ")

    for book in books:
        if book[0] == book_id:

            if book[3] == "Available":
                book[3] = "Issued"
                save_books(books)
                print("Book issued successfully.")
            else:
                print("Book is already issued.")

            return

    print("Book not found.")


def return_book(books):
    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book[0] == book_id:
            book[3] = "Available"

            save_books(books)

            print("Book returned successfully.")
            return

    print("Book not found.")


def display_available(books):
    print("\nAvailable Books:")

    for book in books:
        if book[3] == "Available":
            print(book)


books = load_books()

while True:

    print("\n--- BOOK MANAGEMENT ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book(books)

    elif choice == "2":
        search_book(books)

    elif choice == "3":
        issue_book(books)

    elif choice == "4":
        return_book(books)

    elif choice == "5":
        display_available(books)

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

#22. Merge files
file1 = open("file1.txt", "r")
content1 = file1.read()
file1.close()

file2 = open("file2.txt", "r")
content2 = file2.read()
file2.close()

file3 = open("merged.txt", "w")

file3.write(content1)
file3.write("\n")
file3.write(content2)

file3.close()

print("Two files merged successfully.")

#23. Compare two text files 
file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

if lines1 == lines2:
    print("Both files have identical contents.")

else:
    print("Files are different.")

    max_lines = max(len(lines1), len(lines2))

    for i in range(max_lines):

        line1 = lines1[i].strip() if i < len(lines1) else ""
        line2 = lines2[i].strip() if i < len(lines2) else ""

        if line1 != line2:
            print("First difference found at line:", i + 1)
            print("File 1:", line1)
            print("File 2:", line2)
            break


