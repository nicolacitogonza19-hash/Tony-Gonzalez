pelicula = {
    "titulo": "Interestelar",
    "director": "Christopher Nolan",
    "año": 2014,
}


print(pelicula["titulo"])
print(pelicula["director"])
print(pelicula["año"])


pelicula["genero"] = "Ciencia ficción"


pelicula["año"] = 2015


del pelicula["director"]

print(pelicula)
