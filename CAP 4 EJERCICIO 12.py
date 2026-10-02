saldo = 500

while True:
    retiro = float(input(f"Saldo actual: ${saldo}. ¿Cuánto deseas retirar? (0 para salir): "))

    if retiro == 0:
        break
    elif retiro < 0:
        print("Monto inválido, ingresa un valor positivo")
    elif retiro > saldo:
        print("Saldo insuficiente")
        break
    else:
        saldo -= retiro
        print("Retiro exitoso. Saldo actualizado: ",saldo)

print("Gracias por usar el cajero. Saldo final :",saldo)
