from pymongo import MongoClient
from urllib.parse import quote_plus
from Productos import product
import json
from pymongo import MongoClient
from urllib.parse import quote_plus

class Nombre():
    def Nombre(self):
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
        N = []
        for dic in data:
            for i,j in dic.items():
                if i == "name":
                    if j not in N:
                        N.append(j)
        N.append("Salir")
        # Guarda en una lista los nombres de todos los productos guardados
        while True:
            print("")
            # Te da a elegir entre los produstos existentes
            try:
                print("Elija un nombre")
                for index , o in enumerate(N):
                    print(f"{index+1}.- {o}")
                Selec_op_N = int(input("Seleccione una opción: "))
                if Selec_op_N < 1 or Selec_op_N > len(N):
                    raise ValueError
            except ValueError:
                Selec_op_N = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")
            # Te muestra los datos del producto elegido
            try:
                if Selec_op_N >= 1 and Selec_op_N <= len(N)-1:
                    # with open('Lista_de_productos.txt', 'r') as products:
                    #     pr = products.read()
                    # data = json.loads(pr)
                    for dic in data:
                        for i,j in dic.items():
                            if j == N[Selec_op_N-1]:
                                n = dic["name"]
                                d = dic["description"]
                                p = dic["price"]
                                c = dic["category"]
                                q = dic["quantity"]
                                print(f"\n{n}:\n    {d}\n    $ {p}\n    Categoria: {c}\n    Disponibles: {q}")
                    
                    r = input("\nPresiona ENTER para volver")
                
                elif Selec_op_N == len(N):
                    break
            except UnboundLocalError:
                pass