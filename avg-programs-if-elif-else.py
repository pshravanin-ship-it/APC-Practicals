'''per=float(input("Enter percentage:"))
if per>=90:
    print("Excellent performance")
elif per>=80:
    print("Very good")
elif per>=70:
    print("Good")
elif per>=60:
    print("Average")
else:
    print("Poor")'''

#largest among 3nos
'''a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b and a>c:
    print(a,"is greater")
elif b>a and b>c:
    print(b,"is greater")
else:
    print(c,"is greater")'''

#smallest among 3 nos
'''a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a<b and a<c:
    print(a,"is Smaller")
elif b<a and b<c:
    print(b,"is Smaller")
else:
    print(c,"is Smaller")'''

#number is even or odd.
'''num=int(input("Enter a number:"))
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")'''

#leap year
'''num=int(input("Enter year:"))
if num%4==0:
    print("leap year")
else:
    print("NOt a leap year")'''

#driver-insured or not
marital_status = input("Enter marital status (married/unmarried): ")
gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if marital_status == "married":
    print("Driver is insured")

elif marital_status == "unmarried" and gender == "male" and age > 30:
    print("Driver is insured")

elif marital_status == "unmarried" and gender == "female" and age > 25:
    print("Driver is insured")

else:
    print("Driver is not insured")
    
        
