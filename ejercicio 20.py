numero_anterior = int (input ("Ingrese un numero entero : "))

continuar = True

while continuar:
    numero_nuevo = int (input ("Ingrese un nuevo numero : "))

    if numero_nuevo>numero_anterior:
                    numero_anterior = numero_nuevo
    else:
        print ("Ese numero es menor o igual al anterior ")
        continuar = False
