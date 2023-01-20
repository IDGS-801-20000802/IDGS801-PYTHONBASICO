#programa que le pida al usuario un numero y se imprima la tabla del numero que inserto 


tabla = int(input("dime cual numero quieres multiplicar"))
for x in range(1,11):
 print("La tabla es : {} * {} = {}".format(tabla, x, (tabla*x)))