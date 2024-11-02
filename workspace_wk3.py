# Group 3

from array import *
from multiprocessing import dummy

example_array = array('i', [1, 2, 3, 4, 5])

# Question 1: Write a Python function to create an array of 5 integers and display the array items.
# Access individual elements through indexes.
print("Question 1 Solution:")

def create_array():
  my_array = array('i', [1, 2, 3, 4, 5])
  print(array[0])
  print(array[1])
  print(array[2])
  print(array[3])
  print(array[4])


create_array()

# Question 2:  Write a Python function to append a new item to the end of the array.
# Sample Output:
# Original array: array('i', [1, 3, 5, 7, 9])
# Append 11 at the end of the array:
# New array: array('i', [1, 3, 5, 7, 9, 11])
print("Question 2 Solution:")

def append_item(item=None):
  i = array('i', [1, 3, 5, 7, 9])
  i.append(item)

print(append_item(11))

# Question 3: Write a Python function to reverse the order of the items in the array.
# Sample Output
# Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# Reverse the order of the items:
# array('i', [3, 9, 1, 7, 3, 5, 3, 1])
print("Question 3 Solution:")

dummy = array('i', [1, 2, 3, 4, 5])

def reverse_array(item):
  n=0
  for i in range(len(item), 0, -1):
      dummy[n] = item[i]
      n+=1

print(reverse_array(dummy))

# Question 4: Write a Python function to get the number of occurrences of a specified element in an array.
# Sample Output:
# Original array: array('i', [1, 3, 5, 3, 7, 9, 3])
# Number of occurrences of the number 3 in the said array: 3
print("Question 4 Solution:")

orig = array('i', [1, 3, 5, 3, 7, 9, 3])

def count_occurrance(var):
  dumy = 0
  for i in range(len(orig)):
    if var == orig[i]:
      dumy+=1
  return dumy

count_occurrance(3)

# Question 5: Write a Python function to insert a newly created item before the second element in an existing array.
# Sample Output:
# Original array: array('i', [1, 3, 5, 7, 9])
# Insert new value 4 before 3:
# New array: array('i', [1, 4, 3, 5, 7, 9])
print("Question 5 Solution:")

orig = array('i', [1, 3, 5, 7, 9])
def insert_second(item):
  tmp = item
  for i in range(1, len(orig), 1):
    orig[i] = tmp
    if i != len(orig):
      tmp = orig[i+1]

print(insert_second(4))


# Question 6: Write a Python function to remove a specified item using the index of an array.
# Sample Output:
# Original array: array('i', [1, 3, 5, 7, 9])
# Remove the third item form the array:
# New array: array('i', [1, 3, 7, 9])
print("Question 6 Solution:")
orig = array('i', [1, 3, 5, 7, 9])


# orig.pop(2)
# orig.remove(3)
def remove_item(item):
  tmp = array([])
  n=0
  for i in range(len(orig)):
    if orig[i] != item:
      tmp[n] = orig[i]
      n+=1




# Question 7: Write a Python function to remove the first occurrence of a specified element from an array.
# Sample Output:
# Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# Remove the first occurrence of 3 from the said array:
# New array: array('i', [1, 5, 3, 7, 1, 9, 3])
print("Question 7 Solution:")

# Question 8: Write a Python function to find out if a given array of integers contains any duplicate elements.
# Return true if any value appears at least twice in the array, and return false if every element is distinct.
print("Question 8 Solution:")

# Question 9: Write a Python function to find a pair with the highest product from a given array of integers.
# Original array: [1, 2, 3, 4, 7, 0, 8, 4]
# Maximum product pair is: (7, 8)
print("Question 9 Solution:")

# Question 10: Write a Python function to find the missing number in a given array of numbers between 10 and 20.
# Sample Output:
# Original array: 10 11 12 13 14 16 17 18 19 20
# Missing number in the said array (10-20): 15
# Original array: 10 11 12 13 14 15 16 17 18 19
# Missing number in the said array (10-20): 20
print("Question 10 Solution:")

