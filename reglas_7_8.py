#hay formas de ejecutar codigo de manera condicional

hay_rotura = False
# un condicional es una una funcion f(x->variable booleana verdadera) = y
# si la variable booleana recibida, es falsa, el if ignora lo que esta debajo(la barriga)

#regla 7: EL IF y el ese, son mutuamente exclusivos
#en castellano significa que: si entre al IF, JAMAS entrare al ese y viceversa

if((not hay_rotura)):
    print("camino rapido")
    print("yeah")
    hay_rotura = True
else:
    print("ewww")
    print("por el camino lento")


numero1 = 4
numero2 = 80

#regla 8: los IF, ELIF y el else, son mutuamente exclusivos
#en castellano significa que: si entre al IF, JAMAS entrare al ese y viceversa

if(numero1>numero2):
    print("numero 1 es mayor")
    numero1 = 80
elif(numero2 > numero1):
    print("numero 2 es el mayor")
else:
    print("son iguales")



print("LLegue a Girona")
