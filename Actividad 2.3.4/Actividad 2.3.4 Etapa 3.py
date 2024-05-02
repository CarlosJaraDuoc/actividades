nota1 = float(input("Ingrese 3 notas para sacar el promedio: "))
nota2 = float(input())
nota3 = float(input())
promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 4:
    print(f"Promedio: {promedio}")
    print("Aprobado.")
else:
    print(f"Promedio: {promedio}")
    print("No aprobado.")