from pymongo import MongoClient
from urllib.parse import quote_plus
import json

class Tipo():
    def tipo(self):
        # with open('Lista_de_pagos.txt', 'r') as pay:
        #     p = pay.read()
        # data = json.loads(p)
        usuario = "adaarellano"
        password = "12345"  # Reemplaza con tu contraseña real
        password_encoded = quote_plus(password)  # Codifica caracteres especiales
        connection_string = f"mongodb+srv://{usuario}:{password_encoded}@cluster.3awvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
        client = MongoClient(connection_string)
        db = client["TIENDA"]
        pagos = db["Pagos"]
        data = list(pagos.find({}))
        N = []
        for dic in data:
            for i,j in dic.items():
                if i == "tipo_pago":
                    if j not in N:
                        N.append(j)
        N.append("Salir")

        while True:
            print("")

            try:
                print("Elija un tipo de pago")
                for index , o in enumerate(N):
                    print(f"{index+1}.- {o}")
                Selec_op_N = int(input("Seleccione una opción: "))
                if Selec_op_N < 1 or Selec_op_N > len(N):
                    raise ValueError

            except ValueError:
                Selec_op_N = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")

            try:
                if Selec_op_N >= 1 and Selec_op_N <= len(N)-1:
                    for dic in data:
                        for i,j in dic.items():
                            if j == N[Selec_op_N-1]:
                                
                                f = dic["fecha"]
                                n = dic["name"]
                                m = dic["monto"]
                                mp = dic["moneda"]
                                tp = dic["tipo_pago"]
                                
                                print(f"\nFecha: {f}\n    Nombre del cliente: {n}\n    Monto: $ {m}\n    Moneda de pago: {mp}\n    Tipo de pago: {tp}\n")
                    
                    r = input("\nPresiona ENTER para volver")
            
                elif Selec_op_N == len(N):
                    break

            except UnboundLocalError:
                pass