contrasena_correcta = "CAMILA123"
contrasena = input("Ingresa la contraseña: ")

while contrasena != contrasena_correcta:
    print("Contraseña incorrecta. Intenta de nuevo.")
    contrasena = input("Ingresa la contraseña: ")

print("Acceso concedido.")
