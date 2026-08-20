#1. Create set containing five integers and display all its elements.
s={1,2,3,4,5}
print(s)

#2. Create a list containing duplicate values. Convert the list into a set and display the resulting set
l=[1,2,3,4,5]
s=set(l)
print(s)

#3.Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.
s={"banana","orange","mango","kiwi","apple"}
s.add("grapes")
s.add("watermelon")
print(s)

#4.a set of numbers and remove a specified number from the set.
s={10,20,30,40}
s.remove(20)
print(s)

#5.	Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
stud={"Vaishnavi","Shravani","Piyusha"}
i=input("Enter name:")
if i in stud:
    print("Student exists..")
else:
    print("Student does not exists..")

#6.	Create a set of cities and determine the total number of cities using an appropriate function.
cities={"Kolhapur","Sangli","Pune","Satara"}
print("Count of cities:",len(cities))

#7.Create set of programming languages and display each language using a for loop.
lang={"C","C++","Java","Python"}
for i in lang:
    print(i)

#8.Create a list containing duplicate numbers, use a set to remove the duplicates.
l=[1,2,3,4,7,3,8,9]
s=set(l)
print(s)

#9. two sets of integers and find their union.
s1={1,2,34,3}
s2={2,1,44,0}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

# 13. Create two sets and determine whether the first set is a subset of the second set.

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

if set1.issubset(set2):
    print("Set 1 is a subset of Set 2")
else:
    print("Set 1 is not a subset of Set 2")

# 14. Create two sets and determine whether the first set is a superset of the second set.

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

if set1.issuperset(set2):
    print("Set 1 is a superset of Set 2")
else:
    print("Set 1 is not a superset of Set 2")

# 15. Write a program to determine whether two sets have no elements in common.

set1 = {1, 2, 3}
set2 = {4, 5, 6}

if set1.isdisjoint(set2):
    print("The sets have no elements in common")
else:
    print("The sets have common elements")

# 16. Create two sets and check whether they are equal.

set1 = {1, 2, 3, 4}
set2 = {4, 3, 2, 1}

if set1 == set2:
    print("Both sets are equal")
else:
    print("Both sets are not equal")

# 17. Two students have selected different subjects.
# Store their subjects in two sets and determine the subjects studied by both students.

student1 = {"Python", "Java", "Maths", "DBMS"}
student2 = {"Java", "DBMS", "Networks", "Python"}

common_subjects = student1.intersection(student2)

print("Subjects studied by both students:", common_subjects)

# 18. Accept a sentence from the user and use a set to display all unique words.

sentence = input("Enter a sentence: ")

words = set(sentence.lower().split())

print("Unique words:", words)

# 19. Create two sets:
# Students present in the morning session
# Students present in the afternoon session
# Find:
# - Students present in both sessions
# - Students present only in the morning
# - Students present only in the afternoon
# - Students present in at least one session

morning = {"Amit", "Rahul", "Priya", "Sneha"}
afternoon = {"Priya", "Sneha", "Rohan", "Neha"}

print("Present in both sessions:", morning & afternoon)
print("Only in morning:", morning - afternoon)
print("Only in afternoon:", afternoon - morning)
print("Present in at least one session:", morning | afternoon)

# 20. Create sets representing students enrolled in:
# - Python
# - Java

python_students = {"Amit", "Rahul", "Priya", "Sneha"}
java_students = {"Priya", "Sneha", "Rohan", "Neha"}

print("Python students:", python_students)
print("Java students:", java_students)

# 21. Find students enrolled in both courses and students enrolled in only one course.

python_students = {"Amit", "Rahul", "Priya", "Sneha"}
java_students = {"Priya", "Sneha", "Rohan", "Neha"}

both_courses = python_students & java_students
only_one_course = python_students ^ java_students

print("Students enrolled in both courses:", both_courses)
print("Students enrolled in only one course:", only_one_course)

# 22. Create two sets representing technical skills of two employees. Find:
# - Common skills
# - Skills unique to Employee 1
# - Skills unique to Employee 2
# - All available skills

employee1 = {"Python", "Java", "SQL", "HTML"}
employee2 = {"Java", "Python", "CSS", "JavaScript"}

print("Common skills:", employee1 & employee2)
print("Skills unique to Employee 1:", employee1 - employee2)
print("Skills unique to Employee 2:", employee2 - employee1)
print("All available skills:", employee1 | employee2)

# 23. Create a set containing available books and another set containing requested books.
# Determine which requested books are available.

available_books = {"Python", "Java", "DBMS", "Networks", "AI"}
requested_books = {"Python", "AI", "Cloud Computing", "Java"}

available_requested = available_books & requested_books

print("Requested books that are available:", available_requested)

# 24. Store visitor IDs from two different days in separate sets. Determine:
# - Unique visitors across both days
# - Returning visitors
# - Visitors who came only on the first day
# - Visitors who came only on the second day
# Also, create sets representing products belonging to different categories
# and find products that belong to both categories.

day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

print("Unique visitors across both days:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("Visitors only on first day:", day1 - day2)
print("Visitors only on second day:", day2 - day1)

electronics = {"Laptop", "Mobile", "Tablet", "Headphones"}
gadgets = {"Mobile", "Tablet", "Smartwatch", "Camera"}

print("Products belonging to both categories:", electronics & gadgets)

# 25. Represent the friends of two users using sets. Find:
# - Mutual friends
# - Friends unique to User 1
# - Friends unique to User 2
# - Total unique friends

user1 = {"Amit", "Rahul", "Priya", "Sneha"}
user2 = {"Priya", "Sneha", "Rohan", "Neha"}

print("Mutual friends:", user1 & user2)
print("Friends unique to User 1:", user1 - user2)
print("Friends unique to User 2:", user2 - user1)
print("Total unique friends:", user1 | user2)