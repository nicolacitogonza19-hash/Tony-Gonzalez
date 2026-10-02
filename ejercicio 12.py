a = float (input("Ingrese el valor del coeficiente a : "))
b = float (input("Ingrese el valor del coeficiente b : "))
c = float (input("Ingrese el valor del coeficiente c : "))
discriminante = b**2-4*a*c

if discriminante > 0:
    x1= (-b+discriminante**(1/2))/(2*a)
    x1= (-b+discriminante**(1/2))/(2*a)
    print ("Tiene dos raices reales distintas" )
elif discriminante == 0:
    x1= -b/(2*a)
    print ("Tiene dos raices reales iguales ")
else:
    parte_imaginaria = (abs(discriminante))**(1/2) / (2*a)
    print ("Tiene dos raices complejas")
