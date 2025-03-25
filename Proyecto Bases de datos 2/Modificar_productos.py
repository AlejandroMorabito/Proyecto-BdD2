from pymongo import MongoClient
from urllib.parse import quote_plus
from Productos import product
import json

class Modificar():
    def Modificar(self):
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
        
        while True:
            print("")
            # Te muestra todos los productos que ya existen y te da a elegir al que quieres modificar
            try:
                print("Elige un producto para modificar")
                for index , dic in enumerate(data):
                    id = dic["_id"]
                    n = dic["name"]
                    d = dic["description"]
                    p = dic["price"]
                    c = dic["category"]
                    q = dic["quantity"]
                    print(f"{index+1}.- {n}:\n    {d}\n    $ {p}\n    Categoria: {c}\n    Disponibles: {q}")
                print(f"{len(data)+1}.- Salir")
                Selec_op_MP = int(input("Seleccione una opción: "))
                if Selec_op_MP < 1 or Selec_op_MP > len(data)+1:
                    raise ValueError
                elif Selec_op_MP == len(data)+1:
                    break
            except ValueError:
                Selec_op_MP = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")

            try:
                if Selec_op_MP >= 1 and Selec_op_MP <= len(data):
                    M = []
                    for dic in data:
                        for i,j in dic.items():
                            if i not in M:
                                M.append(i)
                    M.append("Salir")
                    # Te da a elegir lo que quieres modificar del producto
                    while True:
                        print("")
                            
                        try:
                            print("Elija la que quiere modificar")
                            for index , o in enumerate(M):
                                print(f"{index+1}.- {o}")
                            Selec_op_M = int(input("Seleccione una opción: "))
                            if Selec_op_M < 1 or Selec_op_M > len(M):
                                raise ValueError
                        
                        except ValueError:
                            Selec_op_M = 0
                            print("Selección invalida")
                            r = input("\nPresiona ENTER para volver")
                        # Te permite escibir lo a lo que lo quieres cambiar y lo sobre escribe en el .txt
                        try:
                            if Selec_op_M >= 1 and Selec_op_M <= len(M)-1:
                                m = M[Selec_op_M-1]
                                # print(Selec_op_M)
                                # print(Selec_op_MP)
                                # print(m)
                                n = data[Selec_op_MP-1]
                                # print(n)
                                # print(n[m])
                                n[m]= input("Modificación: ")
                                # print(n[m])

                                y = json.dumps(data)
                                # with open('Lista_de_productos.txt', 'w') as products:
                                #     products.write(y)
                                
                                # resultado = productos.update_one(
                                #     {"_id": n[0]},  # Filtro por ID
                                #     {"$set": }  # Datos a actualizar
                                # )
                                
                                return print("Modificado")
                                
                            elif Selec_op_M == len(M):
                                break
                        except UnboundLocalError:
                            pass
            
            except UnboundLocalError:
                pass
