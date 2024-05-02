puntaje = 0
print("¿Cuál de los siguientes animales vive en el agua? ")
print("perro")
print("cocodrilo")
print("conejo")
print("tiburón")
respuesta = input("Escriba su respuesta: ")
if respuesta == "cocodrilo":
    puntaje=+ 0.5
elif respuesta == "tiburón":
    puntaje=+1.0
else:
    puntaje = 0
print(f"puntaje obtenido: {puntaje}")
