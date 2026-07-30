#Write a PYTHON program to print the natural numbers up to n
'''n=int(input("Enter upto n :"))
for i in range(1,n+1):
    print(i)'''

#Write a PYTHON program to print even numbers up to n
'''n=int(input("Enter upto n :"))
for i in range(0,n+1,2):
    print(i)'''

#Write a PYTHON program to print odd numbers up to n
'''n=int(input("Enter upto n :"))
for i in range(1,n+1,2):
    print(i)'''

# Program to print 1, 2, 4, 8, 16, 32 … up to n^2
'''n = int(input("Enter size: "))
value = 1
for i in range(n):
    print(value)
    value = value * 2'''

#Write a PYTHON program to sum the given sequence 1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!
'''def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

n = int(input("Enter the value of n: "))
series_sum = 0

for i in range(n + 1):
    series_sum += 1 / factorial(i)

print("Sum of the series up to 1/{}! is: {:.6f}".format(n, series_sum))'''

# Program to compute cosine series expansion

'''import math

# Input values
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))

cosine_sum = 0

# Loop through terms
for i in range(n + 1):
    term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    cosine_sum += term

print("Cosine series approximation of cos({}) with {} terms is: {:.6f}".format(x, n, cosine_sum))'''

import math

# Function to check if a number is prime
'''def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Main program
n = int(input("Enter a number: "))

sqrt_n = int(math.sqrt(n))

if sqrt_n * sqrt_n == n:  # Check if n is a perfect square
    if is_prime(sqrt_n):
        print(f"The square root of {n} is {sqrt_n}, and it is prime.")
    else:
        print(f"The square root of {n} is {sqrt_n}, and it is not prime.")
else:
    print(f"{n} is not a perfect square, so its square root is not an integer.")'''

#Write a PYTHON program to produce following design
			#A B C 
			#A B C 
			#A B C 
'''for i in range(3):  
    for ch in ['A', 'B', 'C']:  
        print(ch, end=" ")
    print() '''

# Increasing Alphabet Pattern
'''n = int(input("Enter value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()'''

# Decreasing Alphabet Pattern
'''n = int(input("Enter value of n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()'''

#numbers ascending
n = int(input("Enter value of n: "))

for i in range(1, n + 1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

# Descending Number Pattern
n = int(input("Enter value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()







