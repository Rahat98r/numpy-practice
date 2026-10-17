import numpy as np
array = np.arange(6)
twod_array = np.ones((3,3),dtype = bool)
print(twod_array)
# Create a 1D array filled with zeros and another filled with ones
zero_arr = np.zeros(5)
one_arr = np.ones(5)
print(zero_arr)
print(one_arr)
# Create a 1D array of 10 evenly spaced values between 5 and 50
evenly_arr = np.linspace(5,50,10)
print( evenly_arr)
#Create a 3×3 identity matrix
identity = np.eye(3)
print(identity)
#Create a 4×4 array and extract its first row and last column
arr = np.arange(1,17).reshape(4,4)
first_row = arr[0]
last_col = arr[:,-1]

print("4x4 array:\n", arr)
print("first-row:\n",first_row)
print("last-col:\n",last_col)
#Extract Odd Rows and Even Columns
arr = np.arange(1,61,3).reshape(5,4)
odd = arr[:,::2]
even = arr[:,1::2]
print("arr:\n",arr)
print("odd array :\n",odd)
print("even array :\n",even)
#Stack arrays horizontally
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
harray = np.hstack((a,b))
print("Horizontal array :\n",harray)

arr = np.arange(1,17).reshape(4,4)
slice = arr[0:2,:2]
print("Sliced array :\n",slice)
#Replace all odd numbers in a NumPy array with -1
arr = np.arange(1,11)
arr[arr % 2 == 1] = -1
print(arr)
#Create a random 3×2 matrix and find its maximum and minimum values
random = np.random.rand(3,2)
min = random.min()
max = random.max()
print("Random 3X2 matrix:\n",random)
print("Min value :\n",min)
print("Max value :\n",max)
