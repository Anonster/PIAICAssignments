#!/usr/bin/env python
# coding: utf-8

# # **Assignment For Numpy**

# Difficulty Level **Beginner**

# 1. Import the numpy package under the name np

# In[1]:


import numpy as np


# 2. Create a null vector of size 10 

# In[2]:


arr = np.zeros((10))


# 3. Create a vector with values ranging from 10 to 49

# In[3]:


rng = np.arange(10,49)


# 4. Find the shape of previous array in question 3

# In[4]:


rng.shape


# 5. Print the type of the previous array in question 3

# In[5]:


rng.dtype


# 6. Print the numpy version and the configuration
# 

# In[6]:


print(np.__version__)
print(np.show_config())


# 7. Print the dimension of the array in question 3
# 

# In[7]:


print(rng.ndim)


# 8. Create a boolean array with all the True values

# In[8]:


boolean = np.ones((10),dtype=bool)


# 9. Create a two dimensional array
# 
# 
# 

# In[9]:


twoDim = np.zeros((10,10))
print(twoDim.ndim)


# 10. Create a three dimensional array
# 
# 

# In[10]:


threedim = np.zeros((10,10,10))
print(threedim.ndim)


# Difficulty Level **Easy**

# 11. Reverse a vector (first element becomes last)

# In[11]:


reverse = np.random.randn((10))
print(reverse)
reverse = np.flip(reverse)
print(reverse)


# 12. Create a null vector of size 10 but the fifth value which is 1 

# In[12]:


nullVector = np.array([1 if x == 4 else 0 for x in range(10)])
print(nullVector)


# 13. Create a 3x3 identity matrix

# In[13]:


identity = np.identity(3)
print(identity)


# 14. arr = np.array([1, 2, 3, 4, 5]) 
# 
# ---
# 
#  Convert the data type of the given array from int to float 

# In[14]:


arr = np.array([1,2,3,4,5],dtype=float)
arr.dtype


# 15. arr1 =          np.array([[1., 2., 3.],
# 
#                     [4., 5., 6.]])  
#                       
#     arr2 = np.array([[0., 4., 1.],
#      
#                    [7., 2., 12.]])
# 
# ---
# 
# 
# Multiply arr1 with arr2
# 

# In[15]:


arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])  
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
arr1 * arr2


# 16. arr1 = np.array([[1., 2., 3.],
#                     [4., 5., 6.]]) 
#                     
#     arr2 = np.array([[0., 4., 1.], 
#                     [7., 2., 12.]])
# 
# 
# ---
# 
# Make an array by comparing both the arrays provided above

# In[16]:


arr1 = np.array([[1., 2., 3.],[4., 5., 6.]]) 
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
arr3 = arr1 == arr2
print(arr3)


# 17. Extract all odd numbers from arr with values(0-9)

# In[17]:


odd = np.arange(0,10)
print(odd[odd % 2 != 0])


# 18. Replace all odd numbers to -1 from previous array

# In[18]:


odd[odd % 2 != 0] = -1
print(odd)


# 19. arr = np.arange(10)
# 
# 
# ---
# 
# Replace the values of indexes 5,6,7 and 8 to **12**

# In[19]:


arr = np.arange(10)
arr[[5,6,7,8]] = 12
print(arr)


# 20. Create a 2d array with 1 on the border and 0 inside

# In[20]:


twoD = np.ones((4,4))
twoD[1:-1,1:-1] = 0
print(twoD)


# Difficulty Level **Medium**

# 21. arr2d = np.array([[1, 2, 3],
# 
#                     [4, 5, 6], 
# 
#                     [7, 8, 9]])
# 
# ---
# 
# Replace the value 5 to 12

# In[21]:


arr2d = np.array([[1, 2, 3],
                  [4, 5, 6], 
                  [7, 8, 9]])
arr2d = np.where(arr2d == 5,12,arr2d)
print(arr2d)


# 22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# 
# ---
# Convert all the values of 1st array to 64
# 

# In[22]:


arr3d = np.array([
    [
        [1, 2, 3], 
        [4, 5, 6]
    ], 
    [
        [7, 8, 9], 
        [10, 11, 12]
    ]
])
arr3d[0][0] = 64
print(arr3d)


# 23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[23]:


arr2d = np.arange(0,10).reshape((2,5))
print(arr2d)
arr2d[0]


# 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[24]:


arr2d = np.arange(0,10).reshape((2,5))
print(arr2d)
arr2d[1]


# 25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows

# In[25]:


arr2d = np.arange(0,10).reshape((2,5))
print(arr2d)
arr2d[:,2]


# 26. Create a 10x10 array with random values and find the minimum and maximum values

# In[26]:


rand = np.random.randn((100)).reshape((10,10))
print(f"Minimun Value {np.amin(rand)}")
print(f"Maximum Value {np.amax(rand)}")


# 27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
# ---
# Find the common items between a and b
# 

# In[27]:


a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(f"Common Elements are : {np.intersect1d(a,b)}")


# 28. a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# 
# ---
# Find the positions where elements of a and b match
# 
# 

# In[28]:


np.searchsorted(a, np.intersect1d(a, b))


# 29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will**
# 

# In[29]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
print(data)
print('==================================================')
print(data[names != 'Will'])


# 30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**
# 
# 

# In[30]:


print(data)
print('==================================================')
mask = (names != 'Will') & (names!= 'Joe')
print(data[mask])


# Difficulty Level **Hard**

# 31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.

# In[31]:


rand_arr = np.random.uniform(1,15, size=(5,3))
print(rand_arr)


# 32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.

# In[32]:


rand_arr2 = np.random.uniform(1,16, size=(2,2,4))
print(rand_arr2)


# 33. Swap axes of the array you created in Question 32

# In[33]:


print("Original Array")
print(rand_arr2)
print("Swapped Axes")
print(np.swapaxes(rand_arr2, 2, 0))


# 34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0

# In[34]:


arr = np.random.uniform(0,20, size=(10))
arr = arr.astype('int32') 
arr =np.sqrt(arr)
arr = np.where(arr < 0.5, 0, arr)
arr = arr.astype('int32')
print(arr)


# 35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays

# In[35]:


arr = np.random.uniform(0,20, size=(10))
arr1 = np.random.uniform(0,20, size=(10))
newArr = np.maximum(arr,arr1)
print(f"Array 1 : {arr}")
print(f"Array 2 : {arr1}")
print(f"New Array : {newArr}")


# 36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 
# ---
# Find the unique names and sort them out!
# 

# In[36]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.sort(np.unique(names)))


# 37. a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# 
# ---
# From array a remove all items present in array b
# 
# 

# In[37]:


a = np.array([1,2,3,4,5]) 
b = np.array([5,6,7,8,9])
c = np.setdiff1d(a, b)
print(c)


# 38.  Following is the input NumPy array delete column two and insert following new column in its place.
# 
# ---
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# 
# 
# ---
# 
# newColumn = numpy.array([[10,10,10]])
# 

# In[38]:


sampleArray = np.array([
    [34,43,73],
    [82,22,12],
    [53,94,66]
])
newColumn = np.array([[10,10,10]])
sampleArray = np.delete(sampleArray, 2, axis=1)
sampleArray = np.insert(sampleArray, 2, newColumn, axis=1)
print(sampleArray)


# 39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# 
# 
# ---
# Find the dot product of the above two matrix
# 

# In[39]:


x = np.array([[1., 2., 3.], [4., 5., 6.]]) 
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(np.dot(x,y))


# 40. Generate a matrix of 20 random values and find its cumulative sum

# In[40]:


arr = np.random.uniform(1,20,size=(4,5))
arr = arr.astype('int32')
print(arr.cumsum())


# In[ ]:




