#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[1]:


import numpy as np
arr = np.array([0, 1, 2, 3, 4 , 5, 6, 7, 8, 9])
arr = arr.reshape((2,5))
print(arr)


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[2]:


arr1 = np.array([[0, 1, 2, 3, 4],
                [5, 6, 7, 8, 9]])
arr2 = np.ones((2,5))
arr3 = np.vstack((arr1,arr2))
arr3 = arr3.astype('int32')
print(arr3)


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[3]:


arr4 = np.hstack((arr1,arr2))
arr4 = arr4.astype('int32')
print(arr4)


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[4]:


arr = arr.flatten()
print(arr)


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[5]:


arr5 = np.array([
    [ 0, 1, 2],
    [ 3, 4, 5],
    [ 6, 7, 8],
    [ 9, 10, 11],
    [12, 13, 14]
])
arr5 = np.ravel(arr5)
print(arr5)


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[6]:


arr5.reshape(5,3)


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[7]:


arr6 = np.random.randint(1,25, size = (5,5))
print("Original Array: \n")
print (arr6)
print("\n")
print("Square of Array: \n")
print(arr6 ** 2)


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[8]:


arr8 = np.random.randint(1,20, size = (5,6))
print("Original Array: \n")
print (arr8)
print("\n")
print("Mean of Array: \n")
print(arr8.mean())


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[9]:


print("Original Array: \n")
print (arr8)
print("\n")
print("Standard deviation of Array: \n")
print(np.std(arr8))


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[10]:


print("Original Array: \n")
print (arr8)
print("\n")
print("Median of Array: \n")
print(np.median(arr8))


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[11]:


print("Original Array: \n")
print (arr8)
print("\n")
print("Transpose of Array: \n")
print(np.transpose(arr8))


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[12]:


arr7 = np.random.randint(1,20, size = (4,4))
print("Original Array: \n")
print (arr7)
print("\n")
print("Sum of diagonal elements of Array: \n")
print(np.trace(arr7))


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[13]:


print("Original Array: \n")
print (arr7)
print("\n")
print("Determinant of Array: \n")
print(np.linalg.det(arr7))


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[14]:


print("Original Array: \n")
print (arr7)
print("\n")
print(f"5th percentile of array: {np.percentile(arr7, 5)}")
print(f"95th percentile of array: {np.percentile(arr7, 95)}")


# ## Question:15

# ### How to find if a given array has any null values?

# In[15]:


np.isnan(arr7).any()

