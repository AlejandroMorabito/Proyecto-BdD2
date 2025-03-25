from pymongo import MongoClient
from urllib.parse import quote_plus
import json

class Correo():
    def Correo(self):
        # with open('Lista_de_clientes.txt', 'r') as clients:
        #     c = clients.read()
        # data = json.loads(c)
        usuario = "adaarellano"
        password = "12345"  # Reemplaza con tu contraseña real
        password_encoded = quote_plus(password)  # Codifica caracteres especiales
        connection_string = f"mongodb+srv://{usuario}:{password_encoded}@cluster.3awvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
        client = MongoClient(connection_string)
        db = client["TIENDA"]
        clientes = db["Clientes"]
        data = list(clientes.find({}))
        N = []
        for dic in data:
            for i,j in dic.items():
                if i == "correo":
                    if j not in N:
                        N.append(j)
        N.append("Salir")

        while True:
            print("")

            try:
                print("Elija un cliente")
                for index , o in enumerate(N):
                    print(f"{index+1}.- {o}")
                Selec_op_N = int(input("Seleccione una opción: "))
                if Selec_op_N < 1 or Selec_op_N > len(N):
                    raise ValueError

            except ValueError:
                Selec_op_N = 0
                print("Selección invalida")
                r = input("Presiona ENTER para volver")

            try:
                if Selec_op_N >= 1 and Selec_op_N <= len(N)-1:
                    # with open('Lista_de_clientes.txt', 'r') as clients:
                    #     c = clients.read()
                    # data = json.loads(c)
                    for dic in data:
                        for i,j in dic.items():
                            if j == N[Selec_op_N-1]:
                                n = dic["name"]
                                p = dic["persona"]
                                r = dic["Ced_rif"]
                                cr = dic["correo"]
                                d = dic["direccion"]
                                t = dic["telefono"]
                                print(f"\n{n}:\n    {p}\n    {r}\n    {cr}\n    {d}\n    {t}")
                    r = input("\nPresiona ENTER para volver")            

                elif Selec_op_N == len(N):
                    break

            except UnboundLocalError:
                pass