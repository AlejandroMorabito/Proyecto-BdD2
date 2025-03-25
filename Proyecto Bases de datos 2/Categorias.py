from pymongo import MongoClient
from urllib.parse import quote_plus
from Productos import product
import json
from pymongo import MongoClient
from urllib.parse import quote_plus

class Categoria():
    def Categoria(self):
        # with open('Lista_de_productos.txt', 'r') as products:
        #     p = products.read()
        # data = json.loads(p)

        usuario = "adaarellano"
        password = "12345"  # Reemplaza con tu contraseña real
        password_encoded = quote_plus(password)  # Codifica caracteres especiales
        connection_string = f"mongodb+srv://{usuario}:{password_encoded}@cluster.3awvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
        client = MongoClient(connection_string)
        db = client["TIENDA"]
        productos = db["Productos"]
        data = list(productos.find({}))
        C = []
        for dic in data:
            for i,j in dic.items():
                if i == "category":
                    if j not in C:
                        C.append(j)
        C.append("Salir")
        # Guarda todas las categorias que hay existen en una lista
        print("")

        while True:
            print("")
            # Te da a elegir entre las categorias que existen
            try:
                print("Elija la categoria")
                for index , o in enumerate(C):
                    print(f"{index+1}.- {o}")
                Selec_op_C = int(input("Seleccione una opción: "))
                if Selec_op_C < 1 or Selec_op_C > len(C):
                    raise ValueError
            except ValueError:
                Selec_op_C = 0
                print("Selección invalida")
                r = input("Presiona ENTER para volver")
            # Te muestra todos los productos que estan guardados con la categoria elegida
            try:
                if Selec_op_C >= 1 and Selec_op_C <= len(C)-1:
                    # with open('Lista_de_productos.txt', 'r') as products:
                    #     pr = products.read()
                    # data = json.loads(pr)
                    for dic in data:
                        for i,j in dic.items():
                            if j == C[Selec_op_C-1]:
                                n = dic["name"]
                                d = dic["description"]
                                p = dic["price"]
                                c = dic["category"]
                                q = dic["quantity"]
                                print(f"\n{n}:\n    {d}\n    $ {p}\n    Categoria: {c}\n    Disponibles: {q}")
                    r = input("\nPresiona ENTER para volver")
                
                elif Selec_op_C == len(C):
                    break
            except UnboundLocalError:
                pass