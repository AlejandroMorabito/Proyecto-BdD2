from pymongo import MongoClient
from urllib.parse import quote_plus
from Productos import product
import json

class Agregar():
    def Agregar(self):
        # Copia la información que hay en el documento .txt
        # with open('Lista_de_productos.txt', 'r') as products:
        #     p = products.read()
        # data = json.loads(p)
        # products.close()

        usuario = "adaarellano"
        password = "12345"  # Reemplaza con tu contraseña real
        password_encoded = quote_plus(password)  # Codifica caracteres especiales
        connection_string = f"mongodb+srv://{usuario}:{password_encoded}@cluster.3awvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
        client = MongoClient(connection_string)
        db = client["TIENDA"]
        productos = db["Productos"]
        data = list(productos.find({}))

        # Guarda todas las categorias ya existentes
        C = []
        for dic in data:
            for i,j in dic.items():
                if i == "category":
                    if j not in C:
                        C.append(j)
        # Te da a elegir la categoria en la que quieres guardar el producto nuevo
        print("")
        try:
            print("Elija la categoria del nuevo producto")
            for index , o in enumerate(C):
                print(f"{index+1}.- {o}")
            Selec_op_C = int(input("Seleccione una opción: "))
            if Selec_op_C < 1 or Selec_op_C > len(C):
                raise ValueError
        except ValueError:
            Selec_op_C = 0
            print("Selección invalida")
            r = input("Presiona ENTER para volver")
        # Te preguna los datos del nuevo profucto
        r =   {
                "name": input("Nombre del producto: "),
                "description": input("Descripción: "),
                "price": input("Precio: "),
                "category": C[Selec_op_C-1],
                "quantity": input("Cantidad disponible: ")
                }
        # Comprueba si todos los ambitos son validos para cuardarlos
        while True:
            if r["name"] != "":
                break
            elif r["name"] == "":
                print("El nombre no es valido\nPor favor vuelva a escibirlo")
                r["name"]= input("Nombre del producto: ")
        
        while True:
            if r["description"] != "":
                break
            elif r["description"] == "":
                print("El nombre no es valido\nPor favor vuelva a escibirlo")
                r["description"]= input("Nombre del producto: ")
        
        while True:
            try:
                r["price"]=int(r["price"])
                break
            except ValueError:
                print("El precio no es un número\nPor favor escibir un número")
                r["price"]= input("Precio: ")

        while True:
            try:
                r["quantity"]=int(r["quantity"])
                break
            except ValueError:
                print("La disponibilidad no es un número\nPor favor escibir un número")
                r["quantity"]= input("Disponible: ")
        # Agrega el producto nuevo a la lista ya existente
        resultado = productos.insert_one(r)

        # data.append(r)
        # y = json.dumps(data,indent=2)
        # # Sobre escribe los datos anteriores con los nuevos
        # with open('Lista_de_productos.txt', 'w') as products:
        #     products.write(y)
        
        print("Agregado")
        g = input("\nPresiona ENTER para volver")
