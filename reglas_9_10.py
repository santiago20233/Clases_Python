#arreglos o listas o slices
# RAM representation
# value      | label |        type
# [4,0,84,7]    numbers         list

#storing several numbers at once
#on each list you have both -> indexes and values stored in those indexes
#indexes are 0-based numbers, that enumerate the slots
#          0 1 2 3
numbers = [548,4,0,8,7,84]


#how to print the first element?
abuela_en_bikini = numbers[0]

#how to modify the content of a list given the index?
numbers[2] = 84

#how to calculate the amount of elements on a list
cantidad = len(numbers)
print(cantidad)

#how to add elements to an existing list
numbers.append(3600)

#how to remove an element from a list?
numbers.remove(84)   #removes ONLY the first occurrence of an element
numbers.remove(4)
cantidad = len(numbers)


print(cantidad)
print(numbers)
numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)


numbers[2] = 12
print(numbers)
