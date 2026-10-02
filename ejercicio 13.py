letra = input ("Ingrese una letra : ")
vocales = ("a" , "e" , "i" , "o", "u", "A", "E", "I", "O", "U")

if len (letra) !=1:
    print ("no se puede ingresar mas de un caracter")

elif letra in vocales:
    print ("Es vocal")

else:
    print ("No es vocal")
