print ("MENU")
print ("marque 1 para sumar")
print ("marque 2 para restar")
print ("marque 3 para multiplicar")
print ("marque 4 para dividir")
print ("marque 5 para par o impar")
print ("marque 6 para calcular porcentaje")
print ("marque 7 para razones trigonometricas")

import math

opcion = input("Elija una opcion : ")

if opcion == "1":
    n1 = float (input("Ingrese el primer valor : "))
    n2 = float (input("Ingrese el segunfo valor : "))
    print ("Resultado : ", n1+n2)

elif opcion == "2":
    n1 = float (input("Ingrese el primer valor : "))
    n2 = float (input("Ingrese el segunfo valor : "))
    print ("Resultado : ", n1-n2)

elif opcion == "3":
    n1 = float (input("Ingrese el primer valor : "))
    n2 = float (input("Ingrese el segunfo valor : "))
    print ("Resultado : ", n1*n2)

elif opcion == "4":
    n1 = float (input("Ingrese el primer valor : "))
    n2 = float (input("Ingrese el segunfo valor : "))
    print ("Resultado : ", n1/n2)

elif opcion == "5":
    numero = float (input("Ingrese un numero : "))
    if numero % 2 == 0:
        print ("El numero es par")
    else:
        print ("El numero es impar")

elif opcion == "6":
    valor = float(input("Ingrese el valor : "))
    porcentaje = float(input ("Ingrese el porcentaje : "))
    print ("Resultado : ", (valor*porcentaje)/100)

elif opcion == "7":
    grados = float (input ( "Ingrese el angulo en grados : "))
    radianes = math.radians (grados)
    print ("Seno : ", math.sin (radianes))
    print ("Coseno : ", math.cos (radianes))
    print ("tangente : ", math.tan (radianes))

else:
    print ("Opcion no valida")
    
                  
