# 1. Write a function factorial(n) that accepts an integer and returns its factorial.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# 2. Write a function check_even_odd(n) that determines whether a given number is even or odd.
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


# 3. Define a function that accepts two numbers and returns the greater number.
def greater_number(a, b):
    if a > b:
        return a
    else:
        return b


# 4. Create a function simple_interest(p, r, t) to calculate simple interest.
def simple_interest(p, r, t):
    return (p * r * t) / 100


# 5. Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# 6. Define a function to calculate the area of a circle using its radius.
def circle_area(radius):
    return 3.14159 * radius * radius


# 7. Write a function that accepts n and returns the sum of the first n natural numbers.
def sum_natural(n):
    return n * (n + 1) // 2


# 8. Create a function power(base, exponent) to calculate the value of base raised to exponent.
def power(base, exponent):
    return base ** exponent


# 9. Write a function that accepts a list of numbers and returns the largest element
#    without using the built-in max() function.
def largest_element(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


# 10. Define a function that accepts a string and returns the number of vowels present in it.
def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count += 1

    return count


# 11. Write a function that accepts a string and returns its reverse.
def reverse_string(text):
    return text[::-1]


# 12. Create a function that checks whether a given string or number is a palindrome.
def is_palindrome(value):
    value = str(value)
    return value == value[::-1]


# 13. Write a function that accepts a list of numbers and returns their average.
def average(numbers):
    return sum(numbers) / len(numbers)


# 14. Define a function that accepts a list and an element and returns the number of times
#     that element occurs.
def count_element(my_list, element):
    count = 0

    for item in my_list:
        if item == element:
            count += 1

    return count


# 15. Write a function that accepts a list and returns a new list containing only unique elements.
def unique_elements(my_list):
    unique = []

    for item in my_list:
        if item not in unique:
            unique.append(item)

    return unique


# 16. Create a function to find the second-largest number in a list.
def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()

    return unique[-2]


# 17. Write a function that accepts n and returns the first n Fibonacci numbers.
def fibonacci(n):
    result = []
    a = 0
    b = 1

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result


# 18. Create a function that accepts marks in five subjects and returns the student's
#     percentage and grade.
def percentage_grade(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade


# 19. Write a function that accepts the number of units consumed and calculates the
#     electricity bill according to predefined slabs.
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    elif units <= 300:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    else:
        bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 12)

    return bill


# 20. Write a function that accepts basic salary and calculates gross salary after
#     adding HRA and DA.
def gross_salary(basic_salary):
    hra = basic_salary * 0.20
    da = basic_salary * 0.10

    gross = basic_salary + hra + da

    return gross


# 21. Create a function that accepts item prices and quantities and returns the total bill
#     after applying a discount.
def total_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total += prices[i] * quantities[i]

    # 10% discount
    discount = total * 0.10
    final_bill = total - discount

    return final_bill


# 22. Write a function that accepts a list of numbers and returns the minimum, maximum,
#     sum, and average.
def list_statistics(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    avg = total / len(numbers)

    return minimum, maximum, total, avg


# FUNCTION CALLS / OUTPUT 

print("1. Factorial:", factorial(5))

print("2. Even/Odd:", check_even_odd(10))

print("3. Greater Number:", greater_number(25, 40))

print("4. Simple Interest:", simple_interest(10000, 5, 2))

print("5. Is Prime:", is_prime(17))

print("6. Circle Area:", circle_area(5))

print("7. Sum of Natural Numbers:", sum_natural(10))

print("8. Power:", power(2, 5))

print("9. Largest Element:", largest_element([10, 25, 5, 40, 15]))

print("10. Number of Vowels:", count_vowels("Hello World"))

print("11. Reverse String:", reverse_string("Python"))

print("12. Palindrome:", is_palindrome("madam"))

print("13. Average:", average([10, 20, 30, 40, 50]))

print("14. Element Occurs:", count_element([1, 2, 2, 3, 2, 4], 2))

print("15. Unique Elements:", unique_elements([1, 2, 2, 3, 3, 4]))

print("16. Second Largest:", second_largest([10, 25, 5, 40, 30]))

print("17. Fibonacci:", fibonacci(8))

percentage, grade = percentage_grade(85, 90, 78, 88, 92)
print("18. Percentage:", percentage)
print("18. Grade:", grade)

print("19. Electricity Bill:", electricity_bill(250))

print("20. Gross Salary:", gross_salary(30000))

print("21. Total Bill:", total_bill([100, 200, 300], [2, 1, 3]))

minimum, maximum, total, avg = list_statistics([10, 20, 30, 40, 50])
print("22. Minimum:", minimum)
print("22. Maximum:", maximum)
print("22. Sum:", total)
print("22. Average:", avg)


# 23. Write a program using separate functions to process student
# records containing name, roll number, and marks in five subjects.
# Calculate total, percentage, grade, class average, highest scorer,
# and lowest scorer.


def calculate_total(marks):
    return sum(marks)


def calculate_percentage(marks):
    return calculate_total(marks) / 5


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "F"


def display_student(student):
    total = calculate_total(student["marks"])
    percentage = calculate_percentage(student["marks"])
    grade = calculate_grade(percentage)

    print("Name:", student["name"])
    print("Roll Number:", student["roll"])
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)
    print()


def class_average(students):
    total_percentage = 0

    for student in students:
        total_percentage += calculate_percentage(student["marks"])

    return total_percentage / len(students)


def highest_scorer(students):
    highest = students[0]

    for student in students:
        if calculate_total(student["marks"]) > calculate_total(highest["marks"]):
            highest = student

    return highest


def lowest_scorer(students):
    lowest = students[0]

    for student in students:
        if calculate_total(student["marks"]) < calculate_total(lowest["marks"]):
            lowest = student

    return lowest


students = [
    {"name": "Shaurya", "roll": 101, "marks": [85, 90, 78, 88, 92]},
    {"name": "Riya", "roll": 102, "marks": [75, 80, 72, 70, 78]},
    {"name": "Amit", "roll": 103, "marks": [92, 95, 90, 94, 96]}
]

for student in students:
    display_student(student)

print("Class Average:", class_average(students))

high = highest_scorer(students)
print("Highest Scorer:", high["name"])

low = lowest_scorer(students)
print("Lowest Scorer:", low["name"])



# 24. Create functions for deposit, withdrawal, balance enquiry,
# and transaction history. Prevent withdrawal when the balance
# is insufficient and maintain a transaction record.


balance = 5000
transactions = []


def deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposited: Rs.", amount)
    print("Amount deposited successfully.")


def withdrawal(amount):
    global balance

    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn: Rs.", amount)
        print("Amount withdrawn successfully.")
    else:
        print("Insufficient balance.")


def balance_enquiry():
    print("Current Balance: Rs.", balance)


def transaction_history():
    print("Transaction History:")

    for transaction in transactions:
        print(transaction)


deposit(2000)
withdrawal(1500)
balance_enquiry()
transaction_history()


# 25. Create functions to add books, issue books, return books,
# search books, and display available books. Maintain book
# availability using dictionaries.

books = {}


def add_book(book_id, title):
    books[book_id] = {
        "title": title,
        "available": True
    }
    print("Book added successfully.")


def issue_book(book_id):
    if book_id in books:
        if books[book_id]["available"]:
            books[book_id]["available"] = False
            print("Book issued successfully.")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")


def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned successfully.")
    else:
        print("Book not found.")


def search_book(title):
    found = False

    for book_id, book in books.items():
        if book["title"].lower() == title.lower():
            print("Book ID:", book_id)
            print("Title:", book["title"])
            print("Available:", book["available"])
            found = True

    if not found:
        print("Book not found.")


def display_available_books():
    print("Available Books:")

    for book_id, book in books.items():
        if book["available"]:
            print(book_id, "-", book["title"])


add_book(101, "Python Programming")
add_book(102, "Data Structures")
add_book(103, "Database Management")

issue_book(101)

display_available_books()

search_book("Python Programming")

return_book(101)

display_available_books()



# 26. Develop a modular program using functions to calculate
# electricity bills using different consumption slabs.
# Include fixed charges, taxes, and discounts.


def calculate_energy_charge(units):
    if units <= 100:
        charge = units * 5
    elif units <= 200:
        charge = (100 * 5) + ((units - 100) * 7)
    elif units <= 300:
        charge = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    else:
        charge = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 12)

    return charge


def calculate_electricity_bill(units):
    fixed_charge = 100
    energy_charge = calculate_energy_charge(units)

    subtotal = energy_charge + fixed_charge

    tax = subtotal * 0.05
    discount = subtotal * 0.10 if units < 100 else 0

    final_bill = subtotal + tax - discount

    return energy_charge, fixed_charge, tax, discount, final_bill


units = 250

energy, fixed, tax, discount, bill = calculate_electricity_bill(units)

print("Electricity Bill")
print("Energy Charge:", energy)
print("Fixed Charge:", fixed)
print("Tax:", tax)
print("Discount:", discount)
print("Final Bill:", bill)



# 27. Create functions to calculate consultation charges,
# laboratory charges, medicine charges, room charges, and
# final bill. Apply discounts based on patient category.


def consultation_charge():
    return 500


def laboratory_charge():
    return 1500


def medicine_charge():
    return 2000


def room_charge(days):
    return days * 1000


def get_discount(category):
    if category.lower() == "senior":
        return 0.20
    elif category.lower() == "child":
        return 0.15
    elif category.lower() == "general":
        return 0.05
    else:
        return 0


def final_hospital_bill(category, days):
    consultation = consultation_charge()
    laboratory = laboratory_charge()
    medicine = medicine_charge()
    room = room_charge(days)

    subtotal = consultation + laboratory + medicine + room

    discount_rate = get_discount(category)
    discount = subtotal * discount_rate

    final_bill = subtotal - discount

    return consultation, laboratory, medicine, room, discount, final_bill


category = "Senior"
days = 3

consultation, laboratory, medicine, room, discount, final_bill = \
    final_hospital_bill(category, days)

print("Hospital Bill")
print("Consultation:", consultation)
print("Laboratory:", laboratory)
print("Medicine:", medicine)
print("Room:", room)
print("Discount:", discount)
print("Final Bill:", final_bill)



# 28. Implement functions to add/remove products, calculate
# subtotal, apply coupon discounts, calculate GST, and
# generate the final invoice.

products = {}


def add_product(name, price, quantity):
    products[name] = {
        "price": price,
        "quantity": quantity
    }


def remove_product(name):
    if name in products:
        del products[name]
        print("Product removed.")
    else:
        print("Product not found.")


def calculate_subtotal():
    subtotal = 0

    for product in products.values():
        subtotal += product["price"] * product["quantity"]

    return subtotal


def apply_coupon(subtotal, coupon):
    if coupon == "SAVE10":
        return subtotal * 0.10
    elif coupon == "SAVE20":
        return subtotal * 0.20
    else:
        return 0


def calculate_gst(amount):
    return amount * 0.18


def generate_invoice(coupon):
    subtotal = calculate_subtotal()
    discount = apply_coupon(subtotal, coupon)
    amount_after_discount = subtotal - discount
    gst = calculate_gst(amount_after_discount)
    final_amount = amount_after_discount + gst

    print("\n----- INVOICE -----")

    for name, product in products.items():
        total = product["price"] * product["quantity"]
        print(name, ":", total)

    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("GST:", gst)
    print("Final Amount:", final_amount)


add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)
add_product("Keyboard", 2000, 1)

generate_invoice("SAVE10")



# 29. Write a recursive function to search for an element in a
# sorted list using binary search.


def binary_search(arr, low, high, key):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)

    else:
        return binary_search(arr, mid + 1, high, key)


numbers = [10, 20, 30, 40, 50, 60, 70]

key = 50

result = binary_search(numbers, 0, len(numbers) - 1, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")



# 30. Convert a decimal number into binary using recursion
# without using Python's built-in conversion functions.


def decimal_to_binary(n):

    if n == 0:
        return ""

    return decimal_to_binary(n // 2) + str(n % 2)


number = 25

if number == 0:
    binary = "0"
else:
    binary = decimal_to_binary(number)

print("Decimal:", number)
print("Binary:", binary)



# 31. Check whether a string is a palindrome using recursion.

def palindrome_recursive(text):

    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome_recursive(text[1:-1])


text = "madam"

if palindrome_recursive(text):
    print("Palindrome")
else:
    print("Not a palindrome")



# 32. Create separate functions for addition, subtraction,
# multiplication, and division. Pass these functions as
# arguments to another function called calculate().


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b


def calculate(a, b, operation):
    return operation(a, b)


print("Addition:", calculate(20, 10, addition))
print("Subtraction:", calculate(20, 10, subtraction))
print("Multiplication:", calculate(20, 10, multiplication))
print("Division:", calculate(20, 10, division))