#Devolución Dinero
user = input("Ingrese el usuario:")
pwd = input("Ingrese su password:")
if user == "duoc" and pwd == "123duoc":
    valorDev = int(input("Bienvenido, Ingrese el valor a devolver: "))
    if valorDev > 100000:
        print("Se dará la máxima urgencia a su devolución de dinero")
    else:
        print("El caso ha quedado registrado, le informaremos lo antes posible")
else:
    print ("Error en contraseña")

# Pregunta: ¿Qué mensaje nos imprimirá el sistema, si nos devuelve una devolución de dinero de $120.000, e ingresamos el user “duoc123”, y el pass “123duoc”?.
# Respuesta: Nos entregará el mensaje "Error en contraseña" ya que el user que el programa solicita es distinto al del que se propone en la pregunta.
# Si el user estuviera correcto, el mensaje que enviaria sería "Se dará la máxima urgencia a su devolución de dinero".
