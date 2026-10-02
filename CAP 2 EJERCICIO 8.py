respuesta = input("¿Aprobaste el curso introductorio?: ")
promedio = float(input("Ingresa tu promedio: "))

aprobo_introductorio = respuesta.strip().lower() in ("sí", "si")

print(aprobo_introductorio and promedio >= 3.5)
