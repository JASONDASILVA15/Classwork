# jason dasilva
# 5/8/2024

# create an empty list
lst = []

# using a for loop to add the numbers 1 threw 100 to the list
for b in range(1, 101):
    lst += [b]

# printing the list lst
print(lst)

# creating an empty list named odd
odd = []

# using a for loop to add the odd numbers 1 threw 100 to the list odd
for b in range(1, 101, 2):
    odd += [b]

# printing a list od
print(odd)

# creating an empty list named even
even = []

# using a for loop to add the even numbers 1 threw 100 to the list eve
for b in range(1, 101, 1):
    even += [b]

# printing a list eve
print(even)

# create a variable named b that point tho the first list u created
b = lst

# create a variable named joined that joins even and odd list using a operator
joined = even + odd

# output the variable joins
print(joined)

# output the type of joined variable
print(type(joined))

# compare the list b to the list joined using possisinal comparision
print(b == joined)
