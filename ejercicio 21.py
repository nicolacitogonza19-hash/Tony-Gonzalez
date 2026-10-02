print ("Menu")
print ("1. Ingresar Carro")
print ("2. Ingresar Moto")
print ("3. Total de carros y motos")
print ("4. Dinero recaudado")

opcion = input ("Elija una opcion : ")
continuar = True

while continuar:
    if opcion == "1":
        hora_de_entrada= float (input ("Ingrese la hora de entrada : "))
        hora_de_salida = float (input ("Ingrese la hora de salida : "))
    
