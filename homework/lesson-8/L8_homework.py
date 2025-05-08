## Homework L8: Dictionaries 📚

## We have the list of tuples:

## ```py
european_cities = [("Istanbul", [15460000, "Kebab", "Hagia Sophia"]),
                 ("Moscow", [12678079, "Borscht", "Red Square"]),
                 ("London", [8982000, "Fish and Chips", "Big Ben"]),
                 ("St. Petersburg", [5383890, "Blini", "Hermitage Museum"]),
                ("Berlin", [3669491, "Currywurst", "Brandenburg Gate"]),
                ("Madrid", [3348536, "Paella", "Royal Palace of Madrid"]),
                ("Kiev", [2884000, "Borscht", "Saint Sophia's Cathedral"]),
                ("Paris", [2140526, "Croissant", "Eiffel Tower"])]

## 1. Create an empty dictionary: `european_cities_info`


## 2. Loop over the `european_cities` and unpack each tuple.     # ie, List each key-value pair from the dictionary, one after the other

european_cities_info = dict((x, y) for x, y in european_cities)  # This converts the tuple to a dictionary
print('european_cities_info', european_cities_info)

for k,v in european_cities_info.items():                         # The loop that sperates each key-value pair within the dictionary
  print(k," ",v)

##3. Print dictionary with the format City --> [Population, Dish, Landmark]

print(european_cities_info.keys())

#4. Sort the `european_cities_info` dictionary alphabetically by city (use sorted)
print(sorted(european_cities_info.keys()))

my_keys = list(european_cities_info.keys()) # ["Berlin", "Spain"]
my_keys_sorted = sorted(my_keys)

#for k in my_keys: 
 # print(european_cities_info[k][2])

#5. Safely print the 'Berlin' info from the `european_cities_info` dictionary

print(my_keys_sorted[0])

#6. Safely print the type of 'London' from the `european_cities_info` dictionary

