#Write a PYTHON program to print the natural numbers up to n
'''n=int(input("Enter upto n :"))
i=1
while i<=n:
    print(i)
    i+=1'''

#Write a PYTHON program to print even numbers up to n
'''n=int(input("Enter upto n :"))
i=2
while i<=n:
    print(i)
    i+=2'''

#Write a PYTHON program to print odd numbers up to n
'''n=int(input("Enter upto n :"))
i=1
while i<=n:
    print(i)
    i+=2'''

#Write a PYTHON program to print sum of natural numbers up to n
'''n=int(input("Enter upto n :"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1
print("Sum of natural numbers:",sum)'''

#Write a PYTHON program to print sum of odd numbers up to n
'''n=int(input("Enter n :"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=2
print("Sum of odd natural numbers:",sum)'''

#Write a PYTHON program to print even of odd numbers up to n
'''n=int(input("Enter n :"))
sum=0
i=0
while i<=n:
    sum=sum+i
    i+=2
print("Sum of even natural numbers:",sum)'''

#Write a PYTHON program to print natural numbers up to n in reverse order.
'''n=int(input("Enter upto n :"))
i=n
while i>=1:
    print(i)
    i-=1'''

# Program to print Fibonacci series up to n
'''n = int(input("Enter the limit n: "))
a, b = 0, 1
print("Fibonacci series up to", n, ":")

while a <= n:
    print(a, end=" ")
    a, b = b, a + b'''

#Write a PYTHON program  find a factorial of given number
'''fact=1
i=1
n=int(input("Enter number:"))
while i<=n:
    fact=fact*i
    i+=1
print("Factorial =",fact)'''

# Prime number check using while loop
'''num = int(input("Enter a number: "))
i = 2
is_prime = True

if num > 1:
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
else:
    print(num, "is not a prime number")'''

# Sum of digits using while loop
'''num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

print("Sum of digits:", sum_digits)'''

# Palindrome check using while loop
num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if num == rev:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")


# Reverse a number using while loop
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)

# Multiplication table using while loop
num = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
# Largest of n numbers 
n = int(input("Enter how many numbers: "))
i = 1
largest = None

while i <= n:
    num = int(input("Enter number {}: ".format(i)))
    if largest is None or num > largest:
        largest = num
    i += 1

print("Largest number is:", largest)

# Smallest of n numbers using while loop
n = int(input("Enter how many numbers: "))
i = 1
smallest = None

while i <= n:
    num = int(input("Enter number {}: ".format(i)))
    if smallest is None or num < smallest:
        smallest = num
    i += 1

print("Smallest number is:", smallest)




