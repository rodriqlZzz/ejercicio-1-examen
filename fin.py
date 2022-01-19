lista_coche = []

while True:
    marca_coche = input("marca coche: ")
    if marca_coche == "fin":
        break
    modelo = input("modelo: ")
    combustible = input("tipo combustible: ")
    cilindrada = input("cilindrada: ")
    linea= {}
    linea["marca coche: "] = marca_coche
    linea["modelo: "] = modelo
    linea["combustible: "] = combustible
    linea["cilindrada: "] = cilindrada
    lista_coche.append(linea)
print("\tLista de coches:\n", lista_coche)

lista_coches = []
