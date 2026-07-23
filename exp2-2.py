#create program to calculate area of trianagle , vol of sphere, total surface area of cylinder, area of square
'''base=int(input("Enter base:"))
height=int(input("Enter height:"))
at=0.5*base*height
print("Area of triangle:",at)'''

'''r=float(input("Enter radius:"))
vs=4/3*3.14*r**3
print("Volume of sphere:",vs)'''

'''h=float(input("Enter height:"))
r=float(input("Enter radius:"))
tsa=2*3.14*r*(h+r)
print("TSA of cylinder:",tsa)'''

'''side=int(input("Enter side:"))
area=side*side
print("Area od square:",area)'''



#wap to convert pounds into kg,km into miles,
'''pound=float(input("Enter pounds:"))
kg=pound*0.453592
print(kg)'''

'''km=int(input("Enter km:"))
miles=km*0.621371
print(miles)'''


#wap to calculate factorial of number
'''n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)'''

#wap to check number is prime or not
'''
n = int(input("Enter a number: "))

if n <= 1:
    print("Not a prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")'''


#wap to check the number is palindrome or not

'''n=int(input("Enter a number:"))
rev=0
num=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if num==rev:
    print("Palindrome")
else:
    print("Not a palindrome")'''
    
    
#wap to convert decinal to binary, decimal to hexadecimal

'''n1 = int(input("Enter a decimal number: "))

binary = bin(n1)

print("Binary number:", binary[2:])


n2 = int(input("Enter a decimal number: "))

hexa = hex(n2)

print("Hexadecimal number:", hexa[2:].upper())

n3 = int(input("Enter a decimal number: "))

octal = oct(n3)

print("Octal number:", octal[2:])'''
#wap to factors of a number

'''n = int(input("Enter a number: "))

print("Factors of", n, "are:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i)'''
        
#wap to find ascii value of character
ch = input("Enter a character: ")

print("ASCII value of", ch, "is:", ord(ch))
