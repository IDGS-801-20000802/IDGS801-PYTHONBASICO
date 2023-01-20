
tupla=(1,2,3)
print(tupla)
print(type(tupla))
tupla2=(7,"Roberto", True, 23.8, 16+7j)

print(tupla2)

print(tupla2[1])

print(tupla2[4]) #me trae el 4 elemento
print(tupla2[-1])  #me trae el ultimo elemento
print(tupla2[0:3])
print(tupla2[:3])
print(tupla2[3:])

a,b,c=tupla

print(a)
print(c)

tuplaN= tupla+tupla2
print(tuplaN)
print(tupla.count(2)) #cuenta el numero de apariciones de lo del oparentesis en la cadena

tupla[2]=23