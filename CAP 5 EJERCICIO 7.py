def imprimir_clave_valor(**kwargs):
    for clave, valor in kwargs.items():
        print("",clave,valor)


imprimir_clave_valor(nombre="Ana", edad=22, ciudad="Bucaramanga")
