import time
import os
os.system("cls")
puntaje1 = 0
puntaje2 = 0
puntaje3 = 0
print("Bienvenido a un formulario simple sobre música ")
time.sleep(1)
print("Este formulario constará de 3 preguntas")
time.sleep(1)
print("1. ¿Cuál es la canción más popular del grupo británico de rock \"Radiohead\"?")
print("1. Creep")
print("2. Master of Puppets")
print("3. Bohemian Rhapsody")
print("4. Uprising")
respuesta = int(input("Escriba su respuesta: "))
if respuesta == 1:
    puntaje1=+ 5
else:
    puntaje1 = 0
os.system("cls")
time.sleep(1)
print("2. ¿Qué artista es considerado como el \"Rey del pop\"?")
print("1. Björk")
print("2. Huevito Rey")
print("3. Michael Jackson")
print("4. Taylor Swift")
respuesta = int(input("Escriba su respuesta: "))
if respuesta == 3:
    puntaje2=+ 5
else:
    puntaje2 = 0
print(f"puntaje obtenido: {puntaje2}")
os.system("cls")
time.sleep(1)
print("3. ¿Quien de estos artistas es el que más discos ha vendido en la historia?")
print("1. Led Zeppelin")
print("2. The Beatles")
print("3. Pink Floyd")
print("4. Madonna")
respuesta = int(input("Escriba su respuesta: "))
if respuesta == 2:
    puntaje3=+ 5
else:
    puntaje3 = 0
print(f"puntaje obtenido: {puntaje3}")
resultado = puntaje1 + puntaje2 + puntaje3
os.system("cls")
time.sleep(1)
print("Resultados: ")
time.sleep(1)
print(f"Pregunta 1: {puntaje1}")
time.sleep(1)
print(f"Pregunta 2: {puntaje2}")
time.sleep(1)
print(f"Pregunta 3: {puntaje3}")
time.sleep(1)
print(f"Nota final: {resultado}")
time.sleep(1)
if resultado == 15:
    print("Sabes mucho sobre música!")
elif resultado == 10:
    print("Tienes conocimientos aceptables sobre música...")
elif resultado == 5:
    print("No sabes mucho sobre música...")
else:
    print("No sabes nada sobre música...")
time.sleep(1)   
print ("Gracias por participar.")
