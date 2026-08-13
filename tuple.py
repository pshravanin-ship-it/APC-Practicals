#tuple of five integers and display it.
t=(1,2,3,4,5)
print(t)

#22.	Create a tuple containing five city names. Display:First city ,Last city ,Third city
t=("Sangli","Pune","Satara","Kolhapur","Mumbai")
print("First city:",t[0])
print("Last city:",t[4])
print("Third city:",t[2])

#3student names and display the total number of students using the len() function.
stud=("Shravani","Pranali","Vaishnavi","Piyusha","Madhura")
print("Total Students:",len(stud))

#4tuple of colors. Check whether a given color exists in the tuple
color=("Blue","green","White","Pink")
if "Blue" in color:
    print("Color exists..")
else:
    print("Color not exists..")

#5tuple of fruits and display each fruit using a loop.
fruits=("Apple","Orange","Banana","Kiwi")
for i in fruits:
    print(i)

#6.tuple with repeated numbers and count how many times a particular number appears.
num=(1,2,3,1,1,5,8)
n=int(input("Enter number:"))
print("Count of numbers:",num.count(n))


#7.employee IDs and find the index of a given ID.
emp=("Shravani","Pranali","Vaishnavi","Piyusha","Madhura")
id=(input("Enter id:"))
if id in emp:
    print(emp.index(id))

#8.tuples of numbers and concatenate them into a single tuple.
t1=(1,2,3,4)
t2=(5,6,7,8)
t3=t1+t2
print(t3)

#9.tuple containing three elements and repeat it four times.
t=(1,2,3)
t2=t1*3
print(t2)

#10.tuple of 10 numbers and display
t=(10,20,30,40,50,60,70,80,90,100)
print("First five elements:",t[0:6])
print("Last five elements:",t[5:11])
print("Middle four elements:",t[3:7])
print("Alternate elements:",t[::2])
print("Reverse tuple:",t[::-1])

#11.tuple into a list and add a new element.
t=(1,23,45,20,56)
l=list(t)
print(l)

#12.Accept five numbers from the user, store them in a list, and convert the list into a tuple


students = (
    (1, "Rahul", "Computer", 85),
    (2, "Priya", "IT", 90),
    (3, "Amit", "Mechanical", 78)
)

for student in students:
    print("Roll Number:", student[0])
    print("Name:", student[1])
    print("Department:", student[2])
    print("Marks:", student[3])
    print()



# 13 Store ten numbers in a tuple and calculate their sum.


numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

total = 0

for n in numbers:
    total += n

print(" Sum:", total)
print()



# 14. Find the largest and smallest number in a tuple
#     without using max() and min().


numbers = (25, 10, 45, 5, 60, 30)

largest = numbers[0]
smallest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

    if n < smallest:
        smallest = n

print(" Largest:", largest)
print(" Smallest:", smallest)
print()



# 15 Calculate the average of elements stored in a tuple.


numbers = (10, 20, 30, 40, 50)

total = 0

for n in numbers:
    total += n

average = total / len(numbers)

print("Average:", average)
print()



# 16 Store 15 integers in a tuple and count:
#     Even numbers and Odd numbers.


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

even = 0
odd = 0

for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print(" Odd numbers:", odd)
print()



# 17. Accept a number from the user and determine whether
#     it exists in the tuple.


numbers = (10, 20, 30, 40, 50)

n = int(input("Enter number to search: "))

if n in numbers:
    print("Number exists in tuple")
else:
    print("Number does not exist in tuple")

print()


# 18. Store student details in a tuple:
#     Roll Number, Name, Department and Marks.
#     Display all the details.


student = (101, "Shravani", "Computer Science", 85)

print("Student Details")
print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])
print()



# 22. Create tuples containing:
#     Employee ID, Name and Salary.
#     Display all employee information.


employees = (
    (101, "Rahul", 30000),
    (102, "Priya", 35000),
    (103, "Amit", 28000)
)

print("Employee Information")

for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()


# 23. Store item prices in a tuple and calculate:
#     Total bill, Average price, Highest-priced item
#     and Lowest-priced item.


prices = (100, 250, 150, 500, 300)

total = 0
highest = prices[0]
lowest = prices[0]

for price in prices:
    total += price

    if price > highest:
        highest = price

    if price < lowest:
        lowest = price

average = total / len(prices)

print("- Total Bill:", total)
print(" Average Price:", average)
print(" Highest Price:", highest)
print("Lowest Price:", lowest)
print()



# 24. Store temperatures of seven days in a tuple and
#      determine maximum, minimum and average temperature.


temperatures = (32, 35, 31, 30, 36, 34, 33)

total = 0
maximum = temperatures[0]
minimum = temperatures[0]

for temp in temperatures:
    total += temp

    if temp > maximum:
        maximum = temp

    if temp < minimum:
        minimum = temp

average = total / len(temperatures)

print(" Maximum Temperature:", maximum)
print("Minimum Temperature:", minimum)
print(" Average Temperature:", average)
print()



# 25 Store runs scored in 10 matches and calculate:
#      Total runs, Highest score, Lowest score and Average score.


runs = (45, 78, 32, 90, 65, 55, 100, 42, 70, 88)

total = 0
highest = runs[0]
lowest = runs[0]

for r in runs:
    total += r

    if r > highest:
        highest = r

    if r < lowest:
        lowest = r

average = total / len(runs)

print(" Total Runs:", total)
print(" Highest Score:", highest)
print("Lowest Score:", lowest)
print("Average Score:", average)
print()


# 26. Create two tuples and find the common elements
#      between them.


t1 = (10, 20, 30, 40, 50)
t2 = (30, 40, 50, 60, 70)

common = []

for n in t1:
    if n in t2:
        common.append(n)

print("Q12 - Common elements:", tuple(common))
print()



# 27. Merge two tuples and remove duplicate elements.


t1 = (10, 20, 30, 40)
t2 = (30, 40, 50, 60)

merged = t1 + t2
result = []

for n in merged:
    if n not in result:
        result.append(n)

print("Q13 - Merged tuple:", tuple(result))
print()


# 28. Count the frequency of each element in a tuple.


t = (10, 20, 10, 30, 20, 10, 40, 30)

frequency = {}

for n in t:
    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] = 1

print("Q14 - Frequency of elements:")

for key in frequency:
    print(key, ":", frequency[key])

print()


# 29 Convert a tuple into a sorted tuple in ascending
#      and descending order.


t = (50, 20, 40, 10, 30)

ascending = tuple(sorted(t))
descending = tuple(sorted(t, reverse=True))

print("Q15 - Ascending:", ascending)
print("Q15 - Descending:", descending)
print()


# 30. Create a tuple containing patient records:
#      Patient ID, Name, Age and Blood Group.
#
#      Perform the following operations:
#      1. Display all records
#      2. Search for a patient by ID
#      3. Count the total number of patients
#      4. Display patients with a specific blood group

patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Priya", 30, "B+"),
    (103, "Amit", 22, "O+"),
    (104, "Sneha", 28, "A+")
)

# Display all records
print("Q16 - All Patient Records")

for patient in patients:
    print("Patient ID:", patient[0])
    print("Name:", patient[1])
    print("Age:", patient[2])
    print("Blood Group:", patient[3])
    print()


# Search for a patient by ID
search_id = int(input("Enter Patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == search_id:
        print("Patient Found")
        print("Patient ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Blood Group:", patient[3])
        found = True

if not found:
    print("Patient not found")

print()


# Count the total number of patients
print("Total Number of Patients:", len(patients))
print()


# Display patients with a specific blood group
blood_group = input("Enter blood group to search: ")

print("Patients with", blood_group, "blood group:")

for patient in patients:
    if patient[3] == blood_group:
        print(patient)


