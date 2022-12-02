def busca_mayor(elementos):
    mayor_temporal=-1

    for item in elementos:
        if(mayor_temporal<item):
            mayor_temporal=item

    return mayor_temporal


numbers=[3,6,1,4,7,9,3]
lista=[34.5,36.5,38.2,33.2]

mayor_numero=busca_mayor(numbers)
mayor_temperatura=busca_mayor(lista)

print(mayor_numero)
print(mayor_temperatura)

