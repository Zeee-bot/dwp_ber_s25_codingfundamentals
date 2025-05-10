# # 3. What are the problems with this conditional? How can you fix it?
# weather = "sunny"
# if weather = "rainy":
#   print("Let's go to the museum!")
# else if weather == "snowy":
#   print("Let's go skiing!")
# else:
#   print("Let's stay home!")
# elif weather == "sunny":
#   print("Let's go to the beach!")

weather = "sunny"
if weather == "rainy":
  print("Let's go to the museum!")
elif weather == "snowy":
  print("Let's go skiing!")
elif weather == "sunny":
  print("Let's go to the beach!")
else:
  print("Let's stay home!")
print()

#   # 4. We want to print all even numbers from 1 to 100.
# # but this loop doesn't print even numbers correctly for some reason.
# # Can you find why and fix it?
# for n in range(1, 100):
#   if n / 2 == 0:
#     print(n)

for n in range(1, 101):
  if n % 2 == 0:
    print(n)

print()    

# # 5. This code below does not execute properly. Try to figure out why.
# def multiply(a, b):
#   a * b

#result =  multiply(10, 10)
#print(result)

def multiply(a, b):
    return a * b

result =  multiply(3, 7)
print(result)
print()


### EXERCISES:


# The code below picks a random number between 1-100,
# and assigns it to the variable called "number". 
# Write code that prints out:
# - "wow it's exactly zero!" if the number is 0
# - "it's a small number" if the number is less than 10
# - "getting bigger" if the number is less than 50
# - "it's a big number" in any other case
import random
number = random.randint(1, 100)
print(number)

if number == 0:
    print("wow it's exactly zero!")
elif number < 10:
    print("it's a small number")
elif number < 50:
    print( "getting bigger")
else:
    print("it's a big number")
print()


# For each fruit in the fruits list, display "It's a {fruit}" on the screen.
#fruits = ["banana", "apple", "cherry", "pear"]

fruits = ["banana", "apple", "cherry", "pear"]

for fruit in fruits:
   print(f"It's a", {fruit})
print()



# Slightly change your code to only print if the fruit length is smaller or equal to 5 characters

fruits = ["banana", "apple", "cherry", "pear"]

for fruit in fruits:
   if len (fruit) <= 5:
    print(f"It's a", {fruit})

print()

# You are given the following string:
# magic_word = "abracadabra"

# Loop over each character in the string and print all the 'a's they are in the magic word:

magic_word = "abracadabra"       #--->string
magic_word_list = list(magic_word)
print(magic_word_list)

for character in magic_word_list:
   if character == "a":
        print(character)

print()

#for character, index in magic_word:
#  if character == a
# print(f"{character}, {index}")

    #print(f'{character},{index}')
        

# Print the indices of all the 'a's in the magic word:
# Example: "aba" -> 0 and 2 (first and third letter)

# Finds the largest number in the list
#numbers = [3,8,1,7,2,9,5,4]

numbers = [3,8,1,7,2,9,5,4]

x = max(numbers)
print(x)
print()




# Compute the sum of all elements in the following list:
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

total_sum = sum(lst)
print(total_sum)
print()



# Write code that merges the two dictionaries below into one
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Hint: "Google is your best friend"
#dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1_list = list(dict1)
print(dict1_list)


# For the output dictionary, look over the key and values and print the key/value pairs:


