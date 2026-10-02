suma_positivos = 0
suma_negativos = 0
cantidad_positivos = 0

for i in range (5):
    numero = int ( input ("Ingrese un numero entero: "))
    if numero<0:
        suma_negativos = suma_negativos+numero
    elif numero>0:
        suma_positivos = suma_positivos+numero
        cantidad_positivos = cantidad_positivos+1

print ("SUMA NEGATIVOS : ", suma_negativos)

if cantidad_positivos >0:
    promedio = suma_positivos/cantidad_positivos
    print ("PROMEDIO : ", promedio)

else:
    ("No se agregaron numeros positivos")
    
    
