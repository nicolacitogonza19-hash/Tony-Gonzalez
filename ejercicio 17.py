n = int (input ("Cuantos estudiantes desea ingresar : "))
estu = []

for i in range (n):
         nombre = input("Ingrese el nombre del estudiante : ")
         estu.append (nombre)

consulta = input ("Que nombre desea buscar : ")

if consulta in estu:
         print ("El estudiante : " , consulta , "si esta en la lista")

else:
     print ("El estudiante : " , consulta , "no esta en la lista")
