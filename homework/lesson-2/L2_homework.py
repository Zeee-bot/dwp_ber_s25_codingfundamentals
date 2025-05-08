## Lesson 2
# Introduction to Python: Variables, Data Types & Booleans  
                                                           
## 1. Variables and Basic Data Types
#a. Assign the number 10 to a variable named `my_number`.

my_number = 10
print(my_number)

#b. Assign the string "Hello, Python!" to a variable named `my_string`.

my_string = "Hello, Python"
print(type(my_string))

#c. Assign the float 3.14 to a variable named `my_float`.

my_float = 3.14
print(type(my_float))

#Print each variable: `my_number`, `my_string`, and `my_float`.

## 2. Working with Different Data Types
# **a. String concatenation**

# - Create two string variables: `first_name` and `last_name`.

first_name = "Zeenat"
last_name = "Ebrahim"

# - Concatenate them with a space in between to form a full name and assign this to a variable named `full_name`.

full_name = first_name + " " + last_name

# - Print the full_name.

print(full_name)


# **b. Arithmetic Operations**
# - Create two integer variables: `a = 5` and `b = 3`.

a = 5
b = 3

# - Perform addition, subtraction, multiplication, and division on these variables, e.g., a+b, a-b, a*b, a/b, and save each result
#  to `add_result`, `sub_result`, `mult_result`, `div_result`

add_result = a + b
print(add_result)

sub_result = a - b
print(sub_result)

mult_result= a * b
print(mult_result)

div_result= a / b             # includes a remainder
print(div_result)             # OR
print(type(div_result))       

div_result= a // b            # excludes a remainder
print(div_result)
print(type(div_result))       # both results are a float

# - Print the results of each operation.


## 3. Booleans and Comparisons

# **a. Creating booleans**
# - Assign the result of 5 > 3 to a variable named `is_greater`.

a = 5
b = 3

is_greater = 5 > 2
print(is_greater)

# - Assign the result of 5 == 3 to a variable named `is_equal`.

is_equal = 5 == 2
print(is_equal)

# - Assign the result of 5 < 3 to a variable named `is_smaller`.

is_smaller = 5 < 2
print(is_smaller)

# - Print the values of `is_greater`, `is_equal`, and `is_smaller`.

# **b. Boolean Operations**

# Create two boolean variables: `bool1 = True` and `bool2 = False`.

bool1 = True
bool2 = False

# Perform logical AND, OR, and NOT operations on these variables and print the results.

# **c. Comparison between data types**

# Given three variables:
# ```
pi = 3.14
pi_pi = '3.14'
pi_pi_pi = "3.14"
# ```
# 1. Are `pi` and `pi_pi` equal? If not, why?

#No pi is an float & pi_pi is a string
print(type(pi))
print(type(pi_pi))
print(type(pi_pi_pi))

# 2. Are `pi_pi` and `pi_pi_pi` equal? If not, why?
#Yes, both are strings

## 4. Type checking and conversion.
# **a. Type checking**

# For each variable `pi`, `pi_pi`, `pi_pi_pi`, use the type() function to print its data type.

# **b. Type conversion**

# - Create a string variable `my_str = "123"`.

my_str = "123"
print(type(my_str))

# - Convert it to an integer and store it in a variable named `my_int`.

my_int = int(my_str)
print(my_int)
print(type(my_int))

# - Convert `my_int` to a float and store it in a variable named `my_float_converted`.

my_float_converted = float(my_int)
print(my_float_converted)
print(type(my_float_converted))

# - Print all three variables.

## 5. Challenge

# - Define a variable `celsius` and assign it a temperature value in Celsius.

celcius = 30

# - Use the formula (celsius * 9/5) + 32 to convert the temperature to Fahrenheit.

farenheit = (celcius * 9/5)
print(celcius)
print(farenheit)

# - Store the result in a variable named `fahrenheit`.
# - Print the original temperature in Celsius and the converted temperature in Fahrenheit.