#L7 Homework | Shopping List

#Create a program that:

#Asks users to enter items for their shopping list
#Keeps asking for items until they type 'done'
#Shows the complete list at the end


# while loops used for repetive tasks when a condition is met. 
# end the loop


#shopping_list = []

#while input(str("Enter a shopping item or 'done' to finish: ")):
 #   shopping_list.append(item)
  #print (shopping_list)

shopping_list = []

while (True):
    item = input(str("Enter a shopping item or 'done' to finish: "))
    if (item == "done"):
        break

    shopping_list.append(item)
print()    
print("🛒 Your shopping list :" + str(shopping_list))
print()
print("Total items: " + str(len(shopping_list)))


