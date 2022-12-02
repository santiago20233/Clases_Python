def binary_search(elementos_ordenados,item_to_search):
    item_position=-1
    inicio=0
    final=len(elementos_ordenados)-1

    while(inicio<final):
        medio=(inicio+final)//2
        if(elementos_ordenados[medio]==item_to_search):
            item_position=medio
            break
        if(elementos_ordenados[medio]<item_to_search):
            inicio=medio+1
        else:
            final=medio-1

    return item_position

def buscar(elemento,lista):
    item_position=-1
    for index in range(len(lista)):
        if(elemento==lista[index]):
            item_position=index
            break

    return item_position

def promedio(elementos):
    acumulador=0
    for item in elementos:
        acumulador=item+acumulador

    return acumulador/len(elementos)


notas=[1,2,3,4,5,6,7,8,9]

posicion=binary_search(notas,2)
print(posicion)

posicion=buscar(8,notas)
print(posicion)

average=promedio(notas)
print(average)