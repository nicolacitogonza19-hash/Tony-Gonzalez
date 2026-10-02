cadena = input ("Ingrese una cadena : ")
contador = 0

for letra in cadena :
    if letra.isupper ():
        contador = contador+1

print ("La cadena tiene ", contador , "letras mayusculas")

