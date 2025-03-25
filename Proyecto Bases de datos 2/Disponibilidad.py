from pymongo import MongoClient
from urllib.parse import quote_plus
from Productos import product
import json
from pymongo import MongoClient
from urllib.parse import quote_plus

class Disponibilidad():
    def Disponibilidad(self):
        # with open('Lista_de_productos.txt', 'r') as products:
        #     pr = products.read()
        # data = json.loads(pr)
        usuario = "adaarellano"
        password = "12345"  # Reemplaza con tu contraseña real
        password_encoded = quote_plus(password)  # Codifica caracteres especiales
        connection_string = f"mongodb+srv://{usuario}:{password_encoded}@cluster.3awvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
        client = MongoClient(connection_string)
        db = client["TIENDA"]
        productos = db["Productos"]
        data = list(productos.find({}))
        D = []
        for dic in data:
            for i,j in dic.items():
                if i == "quantity":
                    if j not in D:
                        D.append(j)
        D.sort()
        # Guarda la disponibilidad de todos los productos
        while True:
            print("")
            # Te presenta la disponibilidad de los distintos productos
            try:
                print("Elija una cantidad")
                for index , o in enumerate(D):
                    print(f"{index+1}.- {o}")
                print(f"{len(D)+1}.- Salir")
                Selec_op_D = int(input("Seleccione una opción: "))
                if Selec_op_D < 1 or Selec_op_D > len(D)+1:
                    raise ValueError
            except ValueError:
                Selec_op_D = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")
            # Te muestra todos los productos que tienen la cantidad elegida
            try:
                if Selec_op_D >= 1 and Selec_op_D <= len(D):
                    # with open('Lista_de_productos.txt', 'r') as products:
                    #     pr = products.read()
                    # data = json.loads(pr)
                    for dic in data:
                        for i,j in dic.items():
                            if j == D[Selec_op_D-1]:
                                n = dic["name"]
                                d = dic["description"]
                                p = dic["price"]
                                c = dic["category"]
                                q = dic["quantity"]
                                print(f"\n{n}:\n    {d}\n    $ {p}\n    Categoria: {c}\n    Disponibles: {q}")
                    r = input("Presiona ENTER para volver")
                
                elif Selec_op_D == len(D)+1:
                    break
            except UnboundLocalError:
                pass