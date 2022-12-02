#bucles 
#print("santi")
#print("santi")
#print("santi")
#while(condicion):
#   instrucciones a repetir
#   mientras la condicion sea verdadera

#while(True):
#   print("santi")
n=5
while(n>0):
    print("santi")
    n=n-1

numeros=[6,3,8,2,10]
#print(numeros[1])
cantidad=len(numeros)
indice=0

while(indice<cantidad):
    print(numeros[indice])
    indice=indice+1

print("al reves")

cantidad=len(numeros)-1
while(cantidad>=0):
    print(numeros[cantidad])
    cantidad=cantidad-1

#calcula el promedio de los elementos de la lista de numeros
acumulador=0
cantidad=len(numeros)
indice=0

while(indice<cantidad):
    acumulador=numeros[indice]+acumulador
    indice=indice+1

print(acumulador/cantidad)

lista=[-2,7,-4,9,4,-3]
cantidad=len(lista)
indice=0
amount_negativos=0
amount_positivos=0
while(indice<cantidad):
    if(lista[indice]<0):
        amount_negativos=amount_negativos+1
    else:
        amount_positivos=amount_positivos+1
    indice=indice+1

print(amount_positivos)
print(amount_negativos)

#dados 2 numeros a y b multiplicalos sin usar el operador * 

a=4
b=5
acumulador=0
while(b>0):
    acumulador=a+acumulador
    b=b-1
print(acumulador)


a=4
b=5
acumulador=1

while(b>0):
    acumulador=a*acumulador
    b=b-1
print(acumulador)

#dado numero a calculame su factorial

a=6
acumulador=1
while(a>0):
    acumulador=a*acumulador
    a=a-1

print(acumulador)
