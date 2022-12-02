#bucle tipo for 
numbers=[3,2,7,1,4,7,89,4,32]

for index in range(0,len(numbers)):
    print(index,numbers[index])


names=["santi","dimas","paco"]

for item in names:
    print(item)

for mi_abuela,tu_abuela in enumerate(names):
    print(mi_abuela,tu_abuela)

#dado una lista de numeros encuentra el mayor 

numbers=[3,2,7,1,4,7,89,4,32]
mayor_temporal=-1

for item in numbers:
    if(mayor_temporal<item):
        mayor_temporal=item

print(mayor_temporal)
    
#dado una lista de elementos y un numero x dime en que posicion esta x y si no esta imprime -1

numbers=[3,2,7,1,4,7,89,4,32]
x=94
result=[]

for index in range(0,len(numbers)):
    if(numbers[index]==x):
        result.append(index)
        

print(result)

#dada una lista de numeros ordenada, y un numero x dime en que posicion esta x y si no esta imprime -1

numbers=[1,2,3,4,5,6,7,8,9]
x=4
result=-1


for index in range(0,len(numbers)):
    if(numbers[index]==x):
        result=index

print(result)


for index in range((0,len(numbers))/2):
    if(numbers[index]==x):
        result=index

print(result)