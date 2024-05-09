# jason dasilva
# 5/8/2024

# create an empty list
lst = []

# using a for loop to add the numbers 1 threw 100 to the list
for b in range(1, 100):
    lst = [b]

# printing the list lst
print(lst)

# creating an empty list named od
od = []

# using a for loop to add the odd numbers 1 threw 100 to the list odd
for b in range(1, 101, 2):
    od += [b]

# printing a list od
print(od)

# creating an empty list named eve
eve = []

# using a for loop to add the even numbers 1 threw 100 to the list eve
for b in range(1, 101):
    eve += [b]

# printing a list eve
print(eve)
