def leer_numeros():
    entrada = input("Ingresa números separados por comas (ej: 3, 8, 15): ")
    return [int(numero.strip()) for numero in entrada.split(",")]


def calcular_estadisticas(lista):
    minimo = min(lista)
    maximo = max(lista)
    promedio = sum(lista) / len(lista)
    return minimo, maximo, promedio


def mostrar_resultado(minimo, maximo, promedio):
    print("El valor mínimo es ",minimo)
    print("El valor máximo es " ,maximo)
    print(f"El promedio es {promedio:.2f}")


numeros = leer_numeros()
minimo, maximo, promedio = calcular_estadisticas(numeros)
mostrar_resultado(minimo, maximo, promedio)
