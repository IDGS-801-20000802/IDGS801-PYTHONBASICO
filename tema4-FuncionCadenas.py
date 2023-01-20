
cadena="universidad Tecnologica de Leon"
print(cadena)
print(cadena.lower()) #minusculas en toda la cadena
print(cadena.upper())  #mayusculas en toda la cedena
print(cadena.title()) #mayusculas en la primera letra de cada palabra
print(cadena.find("de")) #es para buscar las letras que estan en las comillas en la cadena
print(cadena.count("a"))  #es para saber cuans a aparecen en el string

textoFinal=cadena.replace("a","4")  #va a remplazar todas las letra a por el 4
print(textoFinal)
cadenaNueva=cadena.split(" ") #separacion de palabras toda la cadena
print(cadenaNueva)