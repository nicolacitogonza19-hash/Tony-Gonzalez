original = [10, 20, 30]

copia_asignacion = original
copia_metodo = original.copy()
copia_slicing = original[:]

copia_asignacion[0] = 999
copia_metodo[0] = 888
copia_slicing[0] = 777

print(original)          
print(copia_asignacion)  
print(copia_metodo)      
print(copia_slicing)    
