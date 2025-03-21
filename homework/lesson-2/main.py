# Lesson 2 

#Introduction to Python: Variables, Data Types & Booleans
#1. Variables and Basic Data Types
    #a. Assign the number 10 to a variable named my_number.
    #b. Assign the string "Hello, Python!" to a variable named my_string.
    #c. Assign the float 3.14 to a variable named my_float.
    #Print each variable: my_number, my_string, and my_float

my_number = 10
my_string = "Hello, Python!"
my_float = 3.14
print (my_number, my_string, my_float)

#2. Working with Different Data Types
#a. String concatenation

#Create two string variables: first_name and last_name.
#Concatenate them with a space in between to form a full name and assign this to a variable named full_name.
#Print the full_name.

first_name = "Zeenat"
last_name = "Ebrahim"
full_name = first_name +" "+  last_name
print(full_name)

#b. Arithmetic Operations

#Create two integer variables: a = 5 and b = 3.
#Perform addition, subtraction, multiplication, and division on these variables, 
# e.g., a+b, a-b, a*b, a/b, and save each result to add_result, sub_result, mult_result, div_result
#Print the results of each operation.

a = 5
b = 3

add_result = a+b 
sub_result = a-b
mult_result = a*b
div_result = a/b
print (add_result, sub_result, mult_result, div_result) 

#3. Booleans and Comparisons
#a. Creating booleans

#Assign the result of 5 > 3 to a variable named is_greater.
#Assign the result of 5 == 3 to a variable named is_equal.
#Assign the result of 5 < 3 to a variable named is_smaller.
#Print the values of is_greater, is_equal, and is_smaller.

is_greater = 5 > 3
is_equal = 5 == 3
is_smaller = 5 < 3

print (is_greater, is_equal, is_smaller)

#b. Boolean Operations

# Create two boolean variables: bool1 = True and bool2 = False. 
# Perform logical AND, OR, and NOT operations on these variables and print the results.

bool1 = True 
bool2 = False


#c. Comparison between data types

#Given three variables:

#pi = 3.14
#pi_pi = '3.14'
#pi_pi_pi = "3.14"

#Are pi and pi_pi equal? If not, why?

##pi  != pi_pi
#pi is not eqaul to pi_pi since pi is an integer and pi_pi is a string

#Are pi_pi and pi_pi_pi equal? If not, why?
##pi  == pi_pi
#pi_pi is eqaul to pi_pi_pi since both variables are strings

#4. Type checking and conversion.
#a. Type checking

#For each variable pi, pi_pi, pi_pi_pi, use the type() function to print its data type.

#b. Type conversion

#Create a string variable my_str = "123".
#Convert it to an integer and store it in a variable named my_int.
#Convert my_int to a float and store it in a variable named my_float_converted.
#Print all three variables.

pi = 3.14
pi_pi = '3.14'
pi_pi_pi = "3.14"

type (pi)