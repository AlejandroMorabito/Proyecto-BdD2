from pymongo import MongoClient
from urllib.parse import quote_plus
from Productos import product
import json
from pymongo import MongoClient
from urllib.parse import quote_plus

class Precio():
    def Precio(self):
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
        P = []
        for dic in data:
            for i,j in dic.items():
                if i == "price":
                    if j not in P:
                        P.append(j)
        P.sort()
        # Guarda todas los precios que hay existen en una lista
        while True:
            print("")
            # Te da a elegir entre los precios que existen
            try:
                print("Elija el precio")
                for index , o in enumerate(P):
                    print(f"{index+1}.- $ {o}")
                print(f"{len(P)+1}.- Salir")
                Selec_op_P = int(input("Seleccione una opción: "))
                if Selec_op_P < 1 or Selec_op_P > len(P)+1:
                    raise ValueError
            except ValueError:
                Selec_op_P = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")
            # Te muestra todos los productos que estan guardados con el precio elegido
            try:
                if Selec_op_P >= 1 and Selec_op_P <= len(P):
                    # with open('Lista_de_productos.txt', 'r') as products:
                    #     pr = products.read()
                    # data = json.loads(pr)
                    for dic in data:
                        for i,j in dic.items():
                            if j == P[Selec_op_P-1]:
                                n = dic["name"]
                                d = dic["description"]
                                p = dic["price"]
                                c = dic["category"]
                                q = dic["quantity"]
                                print(f"\n{n}:\n    {d}\n    $ {p}\n    Categoria: {c}\n    Disponibles: {q}")
                    r = input("\nPresiona ENTER para volver")
                
                elif Selec_op_P == len(P)+1:
                    break
            except UnboundLocalError:
                pass