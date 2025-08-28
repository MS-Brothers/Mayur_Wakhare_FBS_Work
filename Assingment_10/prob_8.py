#Write a program to create a duplicate of an existing list. It should not point to same list.
# Create a duplicate list (independent copy)
li = [10, 20, 30, 40, 50]

# Method 1: Using slicing
dup1 = li[:]      

# Method 2: Using list() constructor
dup2 = list(li)  

# Method 3: Using copy()
dup3 = li.copy() 

print("Original list:", li)
print("Duplicate list 1:", dup1)
print("Duplicate list 2:", dup2)
print("Duplicate list 3:", dup3)

li[0]=2345
print("Original list:", li)
print("Duplicate list 1:", dup1)
print("Duplicate list 2:", dup2)
print("Duplicate list 3:", dup3)

dup1[0]=000
print("Duplicate list 1:", dup1)