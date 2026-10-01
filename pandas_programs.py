# Q1. Create a dictionary for 5 students and perform operations using Pandas

import pandas as pd

data = {
    "Student ID": [101, 102, 103, 104, 105],
    "Student Name": ["Aarav", "Alex", "Gaurav", "Shruti", "Ananya"],
    "Python Marks": [85, 72, 90, 68, 80],
    "DBMS Marks": [78, 75, 88, 70, 82],
    "Mathematics Marks": [92, 80, 85, 65, 88]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

df["Total Marks"] = (
    df["Python Marks"] +
    df["DBMS Marks"] +
    df["Mathematics Marks"]
)

print("\nTotal Marks:")
print(df[["Student Name", "Total Marks"]])

df["Average Marks"] = df["Total Marks"] / 3

print("\nAverage Marks:")
print(df[["Student Name", "Average Marks"]])

students_above_75 = df[df["Average Marks"] > 75]

print("\nStudents who scored more than 75% average:")
print(students_above_75[
    ["Student ID", "Student Name", "Average Marks"]
])

# Q2. Create a dictionary containing employee information
# and perform operations using Pandas

import pandas as pd
data = {
    "Employee ID": [101, 102, 103, 104, 105],
    "Employee Name":["Aarav", "Alex", "Gaurav", "Shruti", "Ananya"],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing"],
    "Salary": [55000, 48000, 65000, 72000, 50000],
    "Experience": [3, 2, 5, 7, 4]
}

df = pd.DataFrame(data)

print("Employee Data:")
print(df)

print("Employees with Salary greater than 50000:")
print(df[df["Salary"] > 50000])

average_salary = df["Salary"].mean()

print("\nAverage Salary:")
print(average_salary)

highest_salary = df["Salary"].max()

print("\nHighest Salary:")
print(highest_salary)

highest_experience = df["Experience"].max()

employee = df[df["Experience"] == highest_experience]

print("\nEmployee with Highest Experience:")
print(employee)

# Q3. Create a dictionary containing product information
# and calculate total sales using Pandas

import pandas as pd

data = {
    "Product ID": [101, 102, 103, 104, 105],
    "Product Name": ["Laptop", "Mobile", "Keyboard", "Mouse", "Headphones"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Accessories"],
    "Price": [55000, 25000, 1500, 800, 2000],
    "Quantity": [2, 5, 10, 15, 8]
}

df = pd.DataFrame(data)

print("Product Data:")
print(df)

df["Total Amount"] = df["Price"] * df["Quantity"]

print("\nProduct Sales:")
print(df[["Product ID", "Product Name", "Price", "Quantity", "Total Amount"]])

highest_sales = df["Total Amount"].max()

product = df[df["Total Amount"] == highest_sales]

print("\nProduct with Highest Total Sales:")
print(product)

# Q4. Create a dictionary containing patient information
# and perform operations using Pandas

import pandas as pd

data = {
    "Patient ID": [101, 102, 103, 104, 105],
    "Patient Name": ["Aarav", "Alex", "Gaurav", "Shruti", "Ananya"],
    "Age": [65, 45, 72, 58, 67],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Hypertension"],
    "Medical Charges": [55000, 25000, 85000, 40000, 65000]
}

df = pd.DataFrame(data)

print("Patient Data:")
print(df)

print("\nPatients above 60 years:")
print(df[df["Age"] > 60])

average_charge = df["Medical Charges"].mean()

print("\nAverage Medical Charge:")
print(average_charge)

maximum_charge = df["Medical Charges"].max()

print("\nMaximum Medical Charge:")
print(maximum_charge)

print("\nPatients with Medical Charges greater than 50,000:")
print(df[df["Medical Charges"] > 50000])


#Q5 Order DataFrame and Calculations
import pandas as pd

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Customer": ["Aarav", "Alex", "Gaurav", "Shruti", "Ananya"],
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor", "Printer"],
    "Quantity": [2, 3, 2, 4, 1],
    "Price": [45000, 20000, 18000, 12000, 25000],
    "Discount": [5000, 3000, 2000, 1000, 1500]
}

df = pd.DataFrame(data)

df["Final Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders Above 5,000:")
print(df[df["Final Amount"] > 5000])

highest_order = df.loc[df["Final Amount"].idxmax()]

print("\nHighest-Value Order:")
print(highest_order)

average_order = df["Final Amount"].mean()

print("\nAverage Order Value: ", average_order)


#Q6 Student Attendance 
import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Department": ["Computer", "IT", "Computer", "AI", "IT"],
    "Total_Classes": [50, 50, 60, 40, 50],
    "Classes_Attended": [40, 35, 50, 25, 45]
}

df = pd.DataFrame(data)

df["Attendance Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print("All Students:")
print(df)

print("\nStudents with Attendance Below 75%:")
print(df[df["Attendance Percentage"] < 75])


#Q7Retail Shop Sales Analysis
import pandas as pd

sales_data = {
    "Product_ID": [101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Mobile", "Headphones", "Monitor", "Keyboard"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Accessories"],
    "Price": [45000, 20000, 3000, 12000, 2500],
    "Quantity": [2, 3, 5, 2, 4]
}

df = pd.DataFrame(sales_data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("All Product Sales:")
print(df)

print("\nProducts with Sales Greater Than 10,000:")
print(df[df["Total_Sales"] > 10000])

max_sales = df.loc[df["Total_Sales"].idxmax()]

print("\nProduct with Maximum Sales:")
print(max_sales)

average_sales = df["Total_Sales"].mean()

print("\nAverage Sales: ", average_sales)


#Q8 Student Marks 
import pandas as pd

marks_data = {
    "Amit": 85,
    "Priya": 72,
    "Rahul": 90,
    "Sneha": 68,
    "Neha": 78
}

marks = pd.Series(marks_data)

print("Student Marks:")
print(marks)

print("\nMarks of Rahul:")
print(marks["Rahul"])

print("\nMaximum Marks:", marks.max())
print("Minimum Marks:", marks.min())

print("\nAverage Marks:", marks.mean())

print("\nStudents who scored more than 75:")
print(marks[marks > 75])

#Q9 Employee Salaries
import pandas as pd

salary_data = {
    "Amit": 45000,
    "Priya": 55000,
    "Neha": 75000
}

salary = pd.Series(salary_data)

print("Employee Salaries:")
print(salary)

print("\nHighest Salary:", salary.max())

print("Lowest Salary:", salary.min())

print("Average Salary:", salary.mean())

print("\nEmployees earning more than 50,000:")
print(salary[salary > 50000])

#Q10 Patient Information 
patient_data = {
    "P001": 45,
    "P002": 67,
    "P003": 52,
    "P004": 75,
    "P005": 61,
    "P006": 38
}

ages = pd.Series(patient_data)

# Display the patient ages
print("Patient Ages:")
print(ages)

print("\nAverage Age:", ages.mean())

print("Oldest Patient Age:", ages.max())

print("Youngest Patient Age:", ages.min())

print("\nPatients above 60 years:")
print(ages[ages > 60])


#q10
import pandas as pd

student_data = {
    
    "Amit": 94,
    "Priya": 68,
    "Riya": 91,
    "Akash": 78
}

attendance = pd.Series(student_data)

print("Student Attendance:")
print(attendance)

print("\nAverage Attendance:", attendance.mean(), "%")

print("\nStudents with attendance below 75%:")
print(attendance[attendance < 75])

print("\nStudents with attendance above 90%:")
print(attendance[attendance > 90])

print("\nHighest Attendance:", attendance.max(), "%")


#Q11
import pandas as pd

df = pd.read_csv("student.csv")


print("First 5 Records:")
print(df.head())


print("\nLast 5 Records:")
print(df.tail())


df["Total"] = df[["Python", "DBMS", "Maths"]].sum(axis=1)
df["Average"] = df[["Python", "DBMS", "Maths"]].mean(axis=1)

print("\nTotal and Average Marks of Each Student:")
print(df[["Student_ID", "Name", "Total", "Average"]])


print("\nStudents with Average Marks Greater Than 75:")
print(df[df["Average"] > 75])

highest_student = df.loc[df["Average"].idxmax()]

print("\nStudent with Highest Average:")
print(highest_student)

print("\nAverage Marks for Each Subject:")
print(df[["Python", "DBMS", "Maths"]].mean())


#q12
import pandas as pd

df = pd.read_csv("employees.csv")

print("Employee Dataset:")
print(df)

print("\nEmployees from CSE Department:")
print(df[df["Department"] == "CSE"])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nLowest Salary:")
print(df["Salary"].min())

print("\nEmployees having salary greater than 50,000:")
print(df[df["Salary"] > 50000])

print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())


#q13
import pandas as pd

df = pd.read_csv("patient.csv")

print("Patient Dataset:")
print(df)

print("\n1. Patients above 60 years:")
print(df[df["Age"] > 60])

average_expense = df["Medical_Expense"].mean()
print("\n2. Average Medical Expense:")
print(average_expense)

highest_expense = df.loc[df["Medical_Expense"].idxmax()]
print("\n3. Patient with Highest Medical Expense:")
print(highest_expense)

disease_count = df["Disease"].value_counts()
print("\n4. Number of Patients for Each Disease:")
print(disease_count)

print("\n5. Patients with Medical Expense above 50,000:")
print(df[df["Medical_Expense"] > 50000])

#16
import pandas as pd

df = pd.read_csv("weather.csv")

print("Weather Dataset:")
print(df)

max_temp = df["Temperature"].max()
print("\n1. Maximum Temperature:")
print(max_temp, "°C")

min_temp = df["Temperature"].min()
print("\n2. Minimum Temperature:")
print(min_temp, "°C")

avg_temp = df["Temperature"].mean()
print("\n3. Average Temperature:")
print(avg_temp, "°C")

print("\n4. Records with Temperature above 35 C:")
print(df[df["Temperature"] > 35])

city_avg = df.groupby("City")["Temperature"].mean()
print("\n5. City-wise Average Temperature:")
print(city_avg)





