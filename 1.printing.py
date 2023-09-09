
# 1. Using the print method, print "Hello World"
# print("hello World")
# 2. Create variables for the data type below. 
# Data Types:
# Int
i = 1
# Float
f = 0.1
# String
s  = "we"
# Boolean 
b = True
# Boolean (The other boolean value)
bf = False 
# Lists ( 4 items in list min.)
l = [1,2,3,4]
# Dictionaries  ( 4 key/value pairs min.)
d = {"ron":"james",12:911, 23:"bron", 0:"russ"}
# print(d["ron"])
# 3. For each of the variables, use the print method for each variable. To print each varible
# print(i)
# print(f)
# print(s)
# print(b)
# print(bf)
# print(d)
# 4. Backtick ` in JS are used for Template literals. In a JS file a variable called intVariable and stringVariable exist.
# They are equal to the int and string variables on step 2.
# What is the python equivalent for: console.log(`int: ${intVariable}, string ${stringVariable}`)
# print(f'int: {i} string {s}')
# 5. Comment out all print statements up to this point

# 6. Write a FOR LOOP in python that prints "David Rocks" 5 times
# Hint: type this into google "loop range python"
for n in range(0,5):
    print("David Rocks")
# 7. Declare a function that prints "Alex Rocks". Invoke that function 5 times. 
def alex():
    print("Alex Rocks")
for n in range(0,5):
    alex()
# 8. Declare a function that takes in 2 parameters. 
def sec_func(name1, name2):
    print(f"{name1} and {name2} Rocks")
# It will print "P1(your parameter1) and P2(your parameter2) Rocks"
# Now call that function using "Kyle" and "Winston" as the arguments
sec_func("Kyle", "Winston") 
# invoke that function 4 more times
sec_func("ron","James")
sec_func("Dylan","gibson")
sec_func("Dav","robinson")
sec_func("great","Fans")
# Definitions:  
# P is for Placeholder. P is for Parameters.
# These 2 start w/ the letter P 
# A parameter is variable in the declaration of the function - The place holder

# A is for actual value. A is for aguement.
# These 2 start w/ the letter A
# Arguement is are the values when calling the function - The actual value

# 9. Remember the list variable in step 2. 
# a. Print the index at 3. Then comment it out
# print(l[3])
# b. Now print the index at 100. Does this error? comment it out
# print(l[100])
# e. Now print the index at -1 index. Observe what it prints. Then comment it out
# print(l[-1])
# f. Now print the index at -100.  Does this error? comment it out
# print(l[-100])
# 10. Write a FOR LOOP in python that prints each item in the list variable in step 2. 
for i in l:
    print(i) 
# The staring number MUST be a negative number. The ending number MUST be postive number

# Looking to get each item printed once in order and then a second time in order

# 11. Write a WHILE LOOP in python that does the same thing as 10.
index = 0
while index < len(l):
    print(l[index])
    index += 1
# 12. For loops.
# Write a FOR LOOP in python that prints each item in list variable in step 2.  
# Hint: type this into google "loop python"

# 13. Repeat step 12 but instead of the list variable, use the dictionary variable. 
# Print each key
for i in d:
    print(i)

# 14. Repeat step 13. Instead of printing each key, print each value
for i in d:
    print(d[i])
# Hint: google "dictionary values python"
