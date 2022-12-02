lista=[5,23,8,2]

def mezclar(elmts_ordenados1,startL,endL,startR,endR):
    bolsa=[]
    p1=startL
    p2=startR
    while(p1<endL)and (p2<endR):
        if(elmts_ordenados1[p1]<elmts_ordenados1[p2]):
            bolsa.append(elmts_ordenados1[p1])
            p1=p1+1
        else:
            bolsa.append(elmts_ordenados1[p2])
            p2=p2+1
    
    if(p1>len(elmts_ordenados1)):
        while(p2<len(elmts_ordenados1)):
            bolsa.append(elmts_ordenados1[p2])
            p2=p2+1
    else:
        while(p1<len(elmts_ordenados1)):
            bolsa.append(elmts_ordenados1[p1])
            p1=p1+1

    elmts_ordenados1.clear()
    elmts_ordenados1.extend(bolsa)



    #    bolsa.extend(elmts_ordenados2)
def merge(elementos,start,end):
    if(len(elementos)==1):
        return 
    medio=(start+end)/2
    merge(elementos,start,medio)
    merge(elementos,medio,end)
    mezclar(elementos,start,medio,medio,end)

def merge_sort(elementos):
    start=0
    end=len(elementos)-1
    merge(elementos,start,end)

#ordenamiento burbuja bubble sort 
def bubble_sort(elementos):
    for i in range(len(elementos)):
        for j in range(len(elementos)):
            if(elementos[i]<elementos[j]):
                tmp=elementos[j]
                elementos[j]=elementos[i]
                elementos[i]=tmp
                print(elementos)

bubble_sort(lista)
print(lista)

numeros1=[1,5,9,12]
numeros2=[4,9,11,30]

#respuesta_ordenada=mezclar(numeros1,numeros2)
merge_sort(lista)
print(lista)