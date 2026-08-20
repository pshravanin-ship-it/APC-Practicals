#1.	Create a dictionary containing student details such as roll number, name, department, and marks. Display all key-value pairs
d={"name":"Shravani","Rollno":124,"Department":"CSE","Marks":95}
print(d)

#2.	Create a dictionary containing employee information and display the value associated with a specified key.
emp={"name":"Shravani","Age":20}
print(emp["name"])

#3.	Create a dictionary of five products and their prices. Add a new product and price to the dictionary.
product={"Clothes":1000,"Mobile":20000,"Grocery":2000}
product["Mouse"] = 800
print("Product dictionary:")
print(product)

#4. Create a dictionary containing student marks.
# Update the marks of a specified student.

marks = {
    "Amit": 75,
    "Rahul": 82,
    "Priya": 90,
    "Sneha": 78 }

student = input("Enter student name: ")

if student in marks:
    new_marks = int(input("Enter new marks: "))
    marks[student] = new_marks
    print("Updated dictionary:", marks)
else:
    print("Student not found")

# 5. Create a dictionary of cities and their populations.
# Remove a specified city from the dictionary.

cities = {
    "Mumbai": 20000000,
    "Pune": 7000000,
    "Delhi": 32000000,
    "Bangalore": 13000000,
    "Chennai": 11000000
}

city = input("Enter city to remove: ")

if city in cities:
    del cities[city]
    print("Updated dictionary:", cities)
else:
    print("City not found")

#6.	Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.
# 4. Create a dictionary of employee IDs and names.
# Ask the user for an employee ID and check whether it exists.

employees = {
    101: "Piyusha",
    102: "Rahul",
    103: "Isha",
    104: "Swara",
    105: "Sid"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee ID exists")
    print("Employee name:", employees[emp_id])
else:
    print("Employee ID does not exist")

#7. Create a dictionary containing student records
# and find the total number of key-value pairs.

students = {
    "Amit": 75,
    "Vaishnavi": 82,
    "Priya": 90,
    "Neha": 78,
    "Amar": 85
}

total = len(students)

print("Total number of key-value pairs:", total)

#8.	Create a dictionary and display:
#•	All keys 
#•	All values 
#•	All key-value pairs
students = {
    "Amit": 75,
    "Vaishnavi": 82,
    "Priya": 90,
    "Neha": 78,
    "Amar": 85
}
print(students.keys())
print(students.values())
print(students)

#9. Create a dictionary of programming languages and their creators.
# Display each key and value using a loop.

languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
}

for language, creator in languages.items():
    print(language, ":", creator)

#10.Accept five student names and their marks from the user and store them in a dictionary.

students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("Student dictionary:")
print(students)

#11.	Create a dictionary containing student names and marks. Find the student who has scored the highest marks.
# 9. Create a dictionary containing student names and marks.
# Find the student who has scored the highest marks.

students = {
    "Aarav": 75,
    "Rahul": 82,
    "Siya": 95,
    "Sneha": 88,
    "Sid": 79
}

highest = max(students, key=students.get)

print("Student with highest marks:", highest)
print("Highest marks:", students[highest])

#12.	Create a dictionary containing student names and marks. Find the student with the lowest marks.
students = {
    "Aarav": 75,
    "Rahul": 82,
    "Siya": 95,
    "Sneha": 88,
    "Sid": 79
}

lowest = min(students, key=students.get)

print("Student with highest marks:", lowest)
print("Highest marks:", students[lowest])

#13.	Create a dictionary containing student names and marks. Calculate the average marks of all students.
students = {
    "Aarav": 75,
    "Rahul": 82,
    "Siya": 95,
    "Sneha": 88,
    "Sid": 79
}

total = sum(students.values())
average = total / len(students)

print("Average marks:", average)

#14. Accept a string from the user and create a dictionary
# containing each character and its frequency.

text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequency:")
print(frequency)

#15.Accept a sentence and create a dictionary containing
# each word and the number of times it occurs.

sentence = input("Enter a sentence: ")

words = sentence.lower().split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequency:")
print(frequency)

#16.Create two dictionaries and merge them into a single dictionary.

dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dict2 = {
    "D": 40,
    "E": 50,
    "F": 60
}

merged = dict1.copy()
merged.update(dict2)

print("Merged dictionary:")
print(merged)

# 17. Given two dictionaries, find the keys that are common to both dictionaries.

dict1 = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40
}

dict2 = {
    "B": 50,
    "C": 60,
    "E": 70
}

common_keys = dict1.keys() & dict2.keys()

print("Common keys:", common_keys)

# 18. Given two dictionaries, identify the values that are common to both dictionaries.

dict1 = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40
}

dict2 = {
    "P": 30,
    "Q": 40,
    "R": 50,
    "S": 60
}

common_values = set(dict1.values()) & set(dict2.values())

print("Common values:", common_values)

# 19. Create a dictionary containing duplicate values and remove
# duplicate values while retaining the corresponding keys where appropriate.

data = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "E": 20
}

unique_data = {}

for key, value in data.items():
    if value not in unique_data.values():
        unique_data[key] = value

print("Original dictionary:", data)
print("Dictionary after removing duplicate values:", unique_data)

# 20. Create a dictionary and display its elements in ascending order of keys.

data = {
    5: "Apple",
    2: "Banana",
    4: "Mango",
    1: "Orange",
    3: "Grapes"
}

sorted_data = dict(sorted(data.items()))

print("Dictionary in ascending order of keys:")

for key, value in sorted_data.items():
    print(key, ":", value)

    # 21. Create a dictionary containing numbers from 1 to 10 as keys
# and their squares as values.

squares = {}

for i in range(1, 11):
    squares[i] = i ** 2

print("Dictionary of squares:")
print(squares)

# 22. Create a dictionary containing numbers from 1 to 20 as keys
# and their squares as values, but include only even numbers.

squares = {}

for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i ** 2

print("Dictionary of squares of even numbers:")
print(squares)

# 23. Given a list of numbers, create a dictionary containing
# each unique number and its frequency.

numbers = [1, 2, 3, 2, 4, 1, 3, 5, 2, 4, 1]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Number frequency:")
print(frequency)

## 24. Create a dictionary containing integers from 1 to 10 and their cubes.

cubes = {}

for i in range(1, 11):
    cubes[i] = i ** 3

print("Dictionary containing numbers and their cubes:")
print(cubes)

# 25. Create a dictionary containing student names and marks.
# Develop a program to:
# - Add a student
# - Update marks
# - Delete a student
# - Search for a student
# - Display all students
# - Find the highest marks
# - Calculate the average

students = {
    "Amit": 75,
    "Rahul": 82,
    "Priya": 90
}

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Find Highest Marks")
    print("7. Calculate Average")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    # Add a student
    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully.")

    # Update marks
    elif choice == 2:
        name = input("Enter student name: ")

        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated successfully.")
        else:
            print("Student not found.")

    # Delete a student
    elif choice == 3:
        name = input("Enter student name: ")

        if name in students:
            del students[name]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    # Search for a student
    elif choice == 4:
        name = input("Enter student name: ")

        if name in students:
            print("Student found.")
            print("Name:", name)
            print("Marks:", students[name])
        else:
            print("Student not found.")

    # Display all students
    elif choice == 5:
        print("\nStudent Records:")

        if len(students) == 0:
            print("No student records available.")
        else:
            for name, marks in students.items():
                print(name, ":", marks)

    # Find highest marks
    elif choice == 6:
        if len(students) == 0:
            print("No student records available.")
        else:
            highest = max(students.values())

            print("Highest marks:", highest)

            print("Student(s) with highest marks:")
            for name, marks in students.items():
                if marks == highest:
                    print(name)

    # Calculate average
    elif choice == 7:
        if len(students) == 0:
            print("No student records available.")
        else:
            average = sum(students.values()) / len(students)
            print("Average marks:", average)

    # Exit
    elif choice == 8:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

# 26. Create a dictionary containing employee names and salaries.
# Find:
# - Highest salary
# - Lowest salary
# - Average salary
# - Employees earning more than ₹50,000

employees = {
    "Raghav": 45000,
    "Rahul": 60000,
    
}

salaries = employees.values()

highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / len(employees)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)

print("Employees earning more than ₹50,000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)

# 27. Create a dictionary containing product names and quantities.
# Perform:
# - Add a product
# - Update quantity
# - Delete a product
# - Search for a product
# - Display products with quantity below 10

products = {
    "Laptop": 15,
    "Mobile": 25,
    "Keyboard": 8,
    "Mouse": 5
}

while True:
    print("\n--- Product Management ---")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Display Products Below 10")
    print("6. Display All Products")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        products[product] = quantity
        print("Product added successfully.")

    elif choice == 2:
        product = input("Enter product name: ")

        if product in products:
            quantity = int(input("Enter new quantity: "))
            products[product] = quantity
            print("Quantity updated successfully.")
        else:
            print("Product not found.")

    elif choice == 3:
        product = input("Enter product name: ")

        if product in products:
            del products[product]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    elif choice == 4:
        product = input("Enter product name: ")

        if product in products:
            print("Product:", product)
            print("Quantity:", products[product])
        else:
            print("Product not found.")

    elif choice == 5:
        print("Products with quantity below 10:")
        for product, quantity in products.items():
            if quantity < 10:
                print(product, ":", quantity)

    elif choice == 6:
        print("All products:")
        for product, quantity in products.items():
            print(product, ":", quantity)

    elif choice == 7:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

# 28. Create a dictionary containing names and phone numbers.
# Implement:
# - Add contact
# - Search contact
# - Update contact
# - Delete contact
# - Display all contacts

contacts = {
    "Shravani": "9876543210",
    "Shreya": "9876501234",
    "Piya": "9123456789"
}

while True:
    print("\n--- Contact Management ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully.")

    elif choice == 2:
        name = input("Enter name: ")

        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == 3:
        name = input("Enter name: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == 4:
        name = input("Enter name: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == 5:
        print("All Contacts:")
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

# 29. Create a dictionary containing book IDs and book names.
# Implement:
# - Add a book
# - Search a book
# - Remove a book
# - Display all books
# - Count total books

books = {
    101: "Python Programming",
    102: "Java Programming",
    103: "Data Structures"
}

while True:
    print("\n--- Book Management ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Remove Book")
    print("4. Display All Books")
    print("5. Count Total Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter book ID: "))
        book_name = input("Enter book name: ")
        books[book_id] = book_name
        print("Book added successfully.")

    elif choice == 2:
        book_id = int(input("Enter book ID: "))

        if book_id in books:
            print("Book name:", books[book_id])
        else:
            print("Book not found.")

    elif choice == 3:
        book_id = int(input("Enter book ID: "))

        if book_id in books:
            del books[book_id]
            print("Book removed successfully.")
        else:
            print("Book not found.")

    elif choice == 4:
        print("All Books:")
        for book_id, book_name in books.items():
            print(book_id, ":", book_name)

    elif choice == 5:
        print("Total number of books:", len(books))

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")

# 30. Take a dictionary containing student names and their departments.
# Create a new dictionary that groups students according to their department.

students = {
   
    "Madhura": "Computer",
    "Sneha": "Civil",
    "Sid": "Mechanical",
    "Neha": "Computer"
}

grouped = {}

for name, department in students.items():
    if department not in grouped:
        grouped[department] = []

    grouped[department].append(name)

print("Students grouped by department:")

for department, names in grouped.items():
    print(department, ":", names)

# 31. Take a list of words, create a dictionary where the key is
# the word length and the value is a list of words having that length.

words = ["cat", "dog", "apple", "mango", "bat", "banana", "book"]

grouped_words = {}

for word in words:
    length = len(word)

    if length not in grouped_words:
        grouped_words[length] = []

    grouped_words[length].append(word)

print("Words grouped by length:")

for length, word_list in grouped_words.items():
    print(length, ":", word_list)

# 32. Take a list of integers and a target value.
# Find two numbers whose sum is equal to the target using a dictionary.

numbers = [2, 7, 11, 15, 3, 6]
target = int(input("Enter target value: "))

seen = {}

for num in numbers:
    complement = target - num

    if complement in seen:
        print("Two numbers are:", complement, "and", num)
        print("Their sum is:", target)
        break

    seen[num] = True
else:
    print("No two numbers found.")

# 33. Take a string, use a dictionary to find
# the first character that occurs only once.

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating character found.")

## 34. Take a string, use a dictionary to find
# the first character that occurs more than once.

text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] > 1:
        print("First repeating character:", char)
        break
else:
    print("No repeating character found.")

# 35. Accept a paragraph and create a dictionary where:
# - Key = word length
# - Value = number of words having that length

paragraph = input("Enter a paragraph: ")

words = paragraph.split()
length_count = {}

for word in words:
    length = len(word)

    if length in length_count:
        length_count[length] += 1
    else:
        length_count[length] = 1

print("Word count according to length:")

for length, count in sorted(length_count.items()):
    print(length, ":", count)




