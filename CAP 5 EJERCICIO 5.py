contador = 0


def incrementar():
    global contador
    contador += 1
    print("Contador dentro de la función: " ,contador)


incrementar()
incrementar()
print("Contador fuera de la función: " ,contador)
