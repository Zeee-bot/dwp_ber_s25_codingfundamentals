#Exercise 1 - List

## given this following list of scores:

scores = [15, 19, 17, 12, 17, 13]

## print the first score (by accessing it from the list)

print (scores[0])

## print the last score (by accessing it from the list)

print (scores[5])

## print the highest score (by accessing it from the list) (Hint: max(example_list))

print (max(scores))

## print the lowest score (by accessing it from the list) (Hint: min(example_list))

print (min(scores))

## add 21 to the list of scores (Hint: append(number_to_include))

scores.append (21)
print (scores)

## sort the scores in increasing order (Hint: sort())

scores.sort()
print(scores)

## bonus: remove one of the 17 (Hint: remove(number_to_remove), pop(index))

scores.remove(17)
scores.pop(4)
print(scores)


