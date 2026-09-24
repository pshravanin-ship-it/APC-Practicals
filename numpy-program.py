import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("2D Array:")
print(arr)

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)

import numpy as np

print("Zeros:")
print(np.zeros((2, 3)))

print("Ones:")
print(np.ones((2, 3)))

import numpy as np

arr = np.arange(1, 11)

print("Array:", arr)

import numpy as np

arr = np.arange(1, 10)

new_arr = arr.reshape(3, 3)

print("Original Array:", arr)
print("Reshaped Array:")
print(new_arr)

import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("First element:", arr[0])
print("Third element:", arr[2])
print("First three elements:", arr[:3])
print("Last two elements:", arr[-2:])

import numpy as np

arr = np.array([50, 20, 40, 10, 30])

print("Original:", arr)
print("Sorted:", np.sort(arr))

import numpy as np

arr = np.array([1, 4, 9, 16, 25])

print("Square Root:", np.sqrt(arr))
print("Square:", np.square(arr))
print("Exponential:", np.exp(arr))

import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

result = np.matmul(a, b)

print("Matrix Multiplication:")
print(result)


import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.dot(a, b)

print("Array A:", a)
print("Array B:", b)
print("Dot Product:", result)

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

result = np.split(arr, 3)

print("Original Array:", arr)
print("Split Arrays:")

for x in result:
    print(x)

import numpy as np

arr = np.array([10, 20, 10, 30, 20, 40, 30])

print("Original Array:", arr)
print("Unique Elements:", np.unique(arr))


#Q1.

import numpy as np

arr = np.array([10, 20, 30, 40, 50,60,70,80,90,100])
print("\nQ1")
print(arr)
print("Array size:",arr.size)
print("Array Datatype:",arr.dtype)
print("No of dimensions:",arr.ndim)

#Q2.

a1=np.array([10,20,30,40,50])
a2=np.array([1,2,3,4,5])
print("\nQ2")
print("Addition:",a1+a2)
print('Subtraction:',a1-a2)
print('Multiply:',a1*a2)
print('Division:',a1/a2)
print('Modulus:',a1%a2)


# Q3
arr = np.array([12, 25, 8, 45, 32, 19, 50, 6, 28, 40])

print("\nQ3")
print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))


# Q4
arr = np.arange(1, 21)

even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("\nQ4")
print("Array:", arr)
print("Even Numbers:", even)
print("Odd Numbers:", odd)


# Q5
arr = np.arange(1, 13)

print("\nQ5")
print("Original Array:", arr)

print("2 x 6 Matrix:")
print(arr.reshape(2, 6))

print("3 x 4 Matrix:")
print(arr.reshape(3, 4))

print("4 x 3 Matrix:")
print(arr.reshape(4, 3))


# Q6
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("\nQ6")
print("Matrix A:")
print(a)

print("Matrix B:")
print(b)

print("Matrix Addition:")
print(a + b)


# Q7
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8],
              [9, 10],
              [11, 12]])

print("\nQ7")
print("Matrix A:")
print(a)

print("Matrix B:")
print(b)

print("Matrix Multiplication:")
print(np.matmul(a, b))


# Q8
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("\nQ8")
print("Original Matrix:")
print(arr)

print("Transpose:")
print(arr.T)


# Q9
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 24, 15, 16]])

print("\nQ9")
print("Matrix:")
print(arr)

print("First Row:", arr[0])
print("Last Column:", arr[:, -1])
print("Diagonal Elements:", np.diag(arr))
print("Second and Third Rows:")
print(arr[1:3])


# Q10
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("\nQ10")
print("Matrix:")
print(arr)

print("Sum of Each Row:", np.sum(arr, axis=1))
print("Sum of Each Column:", np.sum(arr, axis=0))


# Q11
arr = np.arange(1, 21)

print("\nQ11")
print("Array:", arr)
print("First 5 Elements:", arr[:5])
print("Last 5 Elements:", arr[-5:])
print("Alternate Elements:", arr[::2])
print("Reverse Order:", arr[::-1])


# Q12
arr = np.array([25, 60, 45, 75, 30, 90, 55, 40, 80, 20])

arr[arr > 70] = 0

print("\nQ12")
print("Updated Array:", arr)


# Q13
arr = np.array([45, 12, 78, 23, 56, 9, 34])

ascending = np.sort(arr)
descending = np.sort(arr)[::-1]

print("\nQ13")
print("Original Array:", arr)
print("Ascending Order:", ascending)
print("Descending Order:", descending)


# Q14
arr = np.array([10, 20, 10, 30, 40, 20, 50, 30, 60, 40])

print("\nQ14")
print("Original Array:", arr)
print("Unique Elements:", np.unique(arr))


# Q15
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("\nQ15")
print("Array A:")
print(a)

print("Array B:")
print(b)

print("Horizontal Concatenation:")
print(np.hstack((a, b)))

print("Vertical Concatenation:")
print(np.vstack((a, b)))


# Q16
marks = np.array([78, 85, 92, 67, 88, 76, 95, 82, 71, 89])

print("\nQ16")
print("Marks:", marks)
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))


# Q17
marks = np.array([
    65, 78, 85, 92, 56,
    74, 88, 69, 95, 81,
    72, 60, 90, 83, 77,
    68, 86, 94, 55, 80
])

average = np.mean(marks)
above_average = marks[marks > average]

print("\nQ17")
print("Marks:", marks)
print("Class Average:", average)
print("Marks Above Average:", above_average)


# Q18
arr = np.arange(1, 25).reshape(2, 3, 4)

print("\nQ18")
print("3D Array:")
print(arr)

print("Number of Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)


# Q19
arr = np.arange(1, 25).reshape(2, 3, 4)

print("\nQ19")
print("3D Array:")
print(arr)

print("First Element:", arr[0, 0, 0])
print("Last Element:", arr[-1, -1, -1])
print("Element at [0,1,2]:", arr[0, 1, 2])
print("Element at [1,2,3]:", arr[1, 2, 3])


# Q20
arr = np.arange(1, 25).reshape(2, 3, 4)

print("\nQ20")
print("3D Array:")
print(arr)

print("Sum of All Elements:", np.sum(arr))

print("Sum of Each Layer:")
print(np.sum(arr, axis=(1, 2)))

print("Sum Along Rows:")
print(np.sum(arr, axis=2))

print("Sum Along Columns:")
print(np.sum(arr, axis=1))


# Q21
arr = np.random.randint(1, 101, size=(2, 3, 4))

print("\nQ21")
print("Original 3D Array:")
print(arr)

arr[arr > 50] = 0

print("Array After Replacing Values Greater Than 50:")
print(arr)


# Q22
arr = np.random.randint(1, 101, size=(3, 4, 5))

print("\nQ22")
print("3D Random Array:")
print(arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))


# Q23
arr = np.arange(1, 25).reshape(2, 3, 4)

flattened = arr.flatten()

print("\nQ23")
print("Original 3D Array:")
print(arr)

print("Flattened Array:")
print(flattened)


# Q24
arr = np.arange(1, 28).reshape(3, 3, 3)

flattened = arr.flatten()

print("\nQ24")
print("3D Array:")
print(arr)

print("Flattened Array:")
print(flattened)

print("Sum:", np.sum(flattened))
print("Average:", np.mean(flattened))
print("Maximum:", np.max(flattened))
print("Minimum:", np.min(flattened))


# Q25
arr = np.random.randint(1, 101, size=(3, 4, 5))

flattened = arr.flatten()
average = np.mean(flattened)

print("\nQ25")
print("Original 3D Array:")
print(arr)

print("Flattened Array:")
print(flattened)

print("Elements Greater Than 50:")
print(flattened[flattened > 50])

print("Even Numbers:")
print(flattened[flattened % 2 == 0])

print("Average:", average)

print("Elements Less Than Average:")
print(flattened[flattened < average])