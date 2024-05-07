cantPasajes = 1
pasajes = 1
total = 0
print("Bienvenido al programa de venta de pasajes.")
while pasajes == True:
    try:
        pasajes = int(input("Cuantos pasajes deseas?: "))
    except ValueError:
        print("Ingrese un número válido")
for pasajes in range(1, pasajes+1):
    try:
        precio = float(input(f"Ingrese precio del pasaje n°{cantPasajes}: "))
        cantPasajes += 1
        total += precio
    except ValueError:
        print("Debes ingresar un número correcto")
        break
print (f"Total de ingresos por la venta de pasajes: ${total} ")
