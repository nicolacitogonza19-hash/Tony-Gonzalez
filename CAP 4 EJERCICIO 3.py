num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operador = input("Ingresa el operador (+, -, *, /): ")

if operador == "+":
    print("Resultado: ", num1 + num2)
elif operador == "-":
    print("Resultado: " ,num1 - num2)
elif operador == "*":
    print("Resultado: ",num1 * num2)
elif operador == "/":
    if num2 != 0:
        print("Resultado: ", num1 / num2)
    else:
        print("Error: no se puede dividir entre cero.")
else:
    print("Error: operador no válido.")
