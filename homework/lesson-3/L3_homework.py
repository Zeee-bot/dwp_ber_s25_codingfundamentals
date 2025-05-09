# # Lesson 3

# # Operators, Conditions and Loops

# # 1. Basic Arithmetic Operations

# Write a Python program that takes two numbers as input and prints the results of:

# - Addition
# - Subtraction
# - Multiplication
# - Division

# ```bash
# # Example of expected output:
# The first number: 5
# The second number: 2
# Addition: 7
# Subtraction: 3
# Multiplication: 10
# Division: 2.5
# ```

print("Q1:")
print()

a = 5
b = 2

add_results = a + b 
print (add_results)

subt_results = a - b 
print (subt_results)

mult_results = a * b 
print (mult_results)

div_results = a / b 
print (div_results)

print()

# ## Bonus!

# If you'd like to try get a bit more fancy, use the `input()` function to get the user to manually add the two values instead of assigning them to the variables in your code.
# Find out more about the `input()` function by clicking [here](https://www.w3schools.com/python/ref_func_input.asp).

# a = int(input("Enter a number: "))
# print(type(a))

# b = int(input("Enter another number: "))
# print(type(b))

# print(a, b)

# add_results = a + b 
# print (add_results)

# subt_results = a - b 
# print (subt_results)

# mult_results = a * b 
# print (mult_results)

# div_results = a / b 
# print (div_results)

# # 2. Modulus and Exponentiation

# Write a Python program that takes a number and prints:

# - The remainder when divided by 3 (using the modulus operator %)
# - The number raised to the power of 2 (using the exponentiation operator \*\*)

print("Q2:")
print()

a = 7
print("The number is", a)

b = a%3
print(b)

b = a/3
print("The remainder when divided by 3 is", b)


# ```bash
# # Example of expected output:
# The number is: 7
# Remainder when divided by 3: 1
# Number raised to the power of 2: 49
# ```

# ## Bonus!

# If you'd like to try get a bit more fancy, use the `input()` function to get the user to manually add the two values instead of assigning them to the variables in your code.
# Find out more about the `input()` function by clicking [here](https://www.w3schools.com/python/ref_func_input.asp).
