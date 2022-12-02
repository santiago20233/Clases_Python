# RAM representation
# value      | label |        type
#

trajo_mandarinas = False

trajo_naranjas = True

#felicidad_santi = trajo_mandarinas and trajo_naranjas

#ALGEBRA BOOLEANA

# convenio: 0-False 1-Verdadero 

#OPERADOR AND
#    a | b | result a and b -> &&
#    0   0   0
#    0   1   0
#    1   0   0
#    1   1   1


#OPERADOR OR
#    a | b | result a or b -> ||
#    0   0   0
#    0   1   1
#    1   0   1
#    1   1   1    -> Contrario a la mente humana


#OPERADOR NOT
# a | result nor a -> !a
# 0    1
# 1    0

tengo_novia = True
hay_lluvia = False
estoy_lleno = True
#print(felicidad_santi) hay que definir primero
felicidad_santi =  tengo_novia and ((not hay_lluvia) or estoy_lleno) 
print(felicidad_santi)
felicidad_santi = not(hay_lluvia)
print(felicidad_santi)
