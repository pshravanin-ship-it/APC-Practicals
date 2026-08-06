
#1
l=["mango","grapes","apple","banana","orange"]
print(l)
#2
i=[10,20,30,40,50]
print(i[0])
print(i[4])
print(i[2])
#3
colors=["blue","white","pink","red"]
print(colors)
colors[2]="purple"
print("Updated list of colors:",colors)
#4
num=[10,20]
num.append(30)
num.insert(0,9)
num.insert(2,12)
print(num)

#5
stud=["Shravani","piyusha","vaishnavi","madhura","pranali"]
stud.remove("Shravani")
print(stud)
stud.pop()
stud.remove("vaishnavi")
print(stud)


numbers = [12, 45, 7, 89, 23, 5, 67]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)

'''numbers = []
total = 0

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
    total += num

average = total / 10

print("List:", numbers)
print("Sum =", total)
print("Average =", average)'''

'''numbers = []
even = 0
odd = 0

for i in range(15):
    num = int(input("Enter an integer: "))
    numbers.append(num)

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("List:", numbers)
print("Even numbers =", even)
print("Odd numbers =", odd)
'''

cities=["kolhapur","pune","sangli","mumbai","satara"]
s=input("Enter city:")
if s in cities:
    print("City is present")
else:
    print("City no present")

l=[10,20,30,40,50]
print(l[::-1])



l1=[10,20,30,40,50,60,70,80,90,100]
print(l1[0:5])
print(l1[5:])
print(l1[3:7])
print(l1[::2])
print(l1[::-1])


n = [10,20,30,40,50,60]
print(n[::2])


numbers = []
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)
numbers.sort()
print("Ascending:", numbers)
numbers.sort(reverse=True)
print("Descending:", numbers)



numbers = [10,20,10,30,20,40]
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)


n1 = [10,50,30,80,60]
n1.sort()
print("Second Largest =", n1[-2])

# 16

students = [["Shravani",101,85],["Isha",102,90],["Rohan",103,80]]
for s in students:
    print("Name:", s[0])
    print("Roll:", s[1])
    print("Marks:", s[2])
    print()

# 17

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,1,1],[1,1,1],[1,1,1]]

print(a[0][0] + b[0][0], a[0][1] + b[0][1], a[0][2] + b[0][2])
print(a[1][0] + b[1][0], a[1][1] + b[1][1], a[1][2] + b[1][2])
print(a[2][0] + b[2][0], a[2][1] + b[2][1], a[2][2] + b[2][2])

# 18.

list = ["Veggies","Milk", "Bread", "Fruits"]
list.append("Butter")
list.remove("Bread")
name = input("Enter item name: ")
if name in list:
    print("Item Found")
else:
    print("Item Not Found")
print("Cart:", list)
print("Total Items:", len(list))

#19
names = ["Arya", "Riya", "Vinit"]
print("Total Students:", len(names))
s = input("Enter student name: ")
if s in names:
    print("Present")
else:
    print("Absent")
names.append("Sneha")
names.remove("Rahul")
print("Students:", names)

#20

b=["b1","b2","b3","b4"]
b.append("b5")
book = input("Enter book name: ")
if book in b:
    print("Book Found")
else:
    print("Book Not Found")
b.remove("b2")
print("Books:", b)
print("Total Books:", len(b))

#21.
l1=[10,20]
l2=[30,40]
print(l1+l2)

#23

list1 = [1, 2, 2, 3, 1, 2]

print("1 =", list1.count(1))
print("2 =", list1.count(2))
print("3 =", list1.count(3))

#24
lst = [10, 20, 30, 40, 50]

left = lst[1:] + [lst[0]]
print("Left Rotation:", left)

right = [lst[-1]] + lst[:-1]
print("Right Rotation:", right)

#25
lst = [10, 20, 10, 30, 20, 40, 50, 30]
new_list = []

for i in lst:
    if i not in new_list:
        new_list.append(i)

print("Original List:", lst)
print("List after removing duplicates:", new_list)

#26
marks = []

for i in range(20):
    m = int(input("Enter marks: "))
    marks.append(m)

highest = marks[0]
lowest = marks[0]
total = 0

for m in marks:
    total += m
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m

average = total / 20

above = 0
below = 0

for m in marks:
    if m > average:
        above += 1
    elif m < average:
        below += 1

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Students Above Average:", above)
print("Students Below Average:", below)

#27
salary = []

n = int(input("Enter number of employees: "))

for i in range(n):
    s = int(input("Enter salary: "))
    salary.append(s)

highest = salary[0]
lowest = salary[0]
total = 0

for s in salary:
    total += s
    if s > highest:
        highest = s
    if s < lowest:
        lowest = s

average = total / n

above50000 = 0
below30000 = 0

for s in salary:
    if s > 50000:
        above50000 += 1
    if s < 30000:
        below30000 += 1

print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Employees Above ₹50000:", above50000)
print("Employees Below ₹30000:", below30000)

#28
scores = []

for i in range(10):
    run = int(input("Enter score: "))
    scores.append(run)

highest = scores[0]
lowest = scores[0]
total = 0
century = 0
half = 0

for run in scores:
    total += run

    if run > highest:
        highest = run

    if run < lowest:
        lowest = run

    if run >= 100:
        century += 1
    elif run >= 50:
        half += 1

average = total / 10

print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Total Runs:", total)
print("Average Runs:", average)
print("Centuries:", century)
print("Half-Centuries:", half)


#29
temp = []

for i in range(30):
    t = float(input("Enter temperature: "))
    temp.append(t)

highest = temp[0]
lowest = temp[0]
total = 0

for t in temp:
    total += t

    if t > highest:
        highest = t

    if t < lowest:
        lowest = t

average = total / 30

above = 0
below = 0

for t in temp:
    if t > average:
        above += 1
    elif t < average:
        below += 1

print("Hottest Day Temperature:", highest)
print("Coldest Day Temperature:", lowest)
print("Average Temperature:", average)
print("Days Above Average:", above)
print("Days Below Average:", below)

#30
names = []
ages = []

n = int(input("Enter number of patients: "))

for i in range(n):
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    names.append(name)
    ages.append(age)

print("Patients:")
for i in range(len(names)):
    print(names[i], "-", ages[i])

# Add a patient
name = input("Enter new patient name: ")
age = int(input("Enter age: "))
names.append(name)
ages.append(age)

# Delete a patient
delete = input("Enter patient name to delete: ")

if delete in names:
    index = names.index(delete)
    names.pop(index)
    ages.pop(index)
    print("Patient deleted.")
else:
    print("Patient not found.")

print("Updated Patient List:")
for i in range(len(names)):
    print(names[i], "-", ages[i])