from pymongo import MongoClient
from urllib.parse import quote_plus
import json

class Registrar():
    def Registrar(self):
        usuario = "adaarellano"
        password = "12345"  # Reemplaza con tu contraseña real
        password_encoded = quote_plus(password)  # Codifica caracteres especiales
        connection_string = f"mongodb+srv://{usuario}:{password_encoded}@cluster.3awvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
        client = MongoClient(connection_string)
        db = client["TIENDA"]
        pagos = db["Pagos"]
        data = list(pagos.find({}))
        
        while True:
            print("")
            N = input("Nombre: ")
            if N != "":
                break
            elif N == "":
                print("El nombre no es valido\nPor favor vuelva a escibirlo")
                r = input("\nPresiona ENTER para volver")
        
        while True:
            print("")
            
            try:
                Monto = int(input("Monto del pago: "))
                break
            except ValueError:
                print("Monto invalido\nPor favor escibir de nuevo")
                r = input("\nPresiona ENTER para volver")
        
        
        while True:
            print("")

            try:
                opc_MP = ["Bolivares","Divisas"]
                print("Elige una moneda para pagar")
                for index , o in enumerate(opc_MP):
                    print(f"{index+1}.- {o}")
                Selec_op_MP = int(input("Seleccione una opción: "))
                if Selec_op_MP >= 1 and Selec_op_MP <= len(opc_MP):
                    break
                if Selec_op_MP < 1 or Selec_op_MP > len(opc_MP):
                    raise ValueError
            except ValueError:
                Selec_op_MP = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")

        while True:
            print("")

            try:
                opc_TP = ["PdV","PM","Zelle","Cash"]
                print("Elige el tipo de pago")
                for index , o in enumerate(opc_TP):
                    print(f"{index+1}.- {o}")
                Selec_op_TP = int(input("Seleccione una opción: "))
                if Selec_op_TP >= 1 or Selec_op_TP <= len(opc_TP):
                    break
                if Selec_op_TP < 1 or Selec_op_TP > len(opc_TP):
                    raise ValueError
            except ValueError:
                Selec_op_TP = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")

        while True:            
            print("")
            try:
                print("¿Va a pagar de contado?")
                opc_D2 = ["Contado","Credito"]
                print("Eliga su respuesta")
                for index , o in enumerate(opc_D2):
                    print(f"{index+1}.- {o}")
                Selec_op_D2 = int(input("Seleccione una opción: "))
                if Selec_op_D2 < 1 or Selec_op_D2 > len(opc_D2):
                    raise ValueError
                break
            except ValueError:
                print("Día no valido\nPor favor escibir un día valido")
                r = input("\nPresiona ENTER para volver")

        while True:
            print("")
            try:
                day =int(input("Coloca el dia (dd)"))
                if day < 1 or day > 31:
                    raise ValueError
                break
            except ValueError:
                print("Día no valido\nPor favor escibir un día valido")
                r = input("\nPresiona ENTER para volver")

        while True:
            print("")
            try:
                month =int(input("Coloca el mes (mm)"))
                if month < 1 or month > 12:
                    raise ValueError
                break
            except ValueError:
                print("Mes no valido\nPor favor escibir un mes valido")
                r = input("\nPresiona ENTER para volver")

        while True:
            print("")
            try:
                year =int(input("Coloca el año (yyyy)"))
                if year < 999:
                    raise ValueError
            except ValueError:
                print("Año no valido\nPor favor escibir un año valido")
                r = input("\nPresiona ENTER para volver")
            try:
                fecha = f"{day}/{month}/{year}"
                break
            except ValueError:
                print("Error en la fecha")
                r = input("\nPresiona ENTER para volver")


        pago = {
                "name": N,
                "monto": Monto,
                "moneda": opc_MP[Selec_op_MP-1],
                "tipo_pago": opc_TP[Selec_op_TP-1],
                "pago": opc_D2[Selec_op_D2-1],
                "fecha": fecha
                }
        
        # with open('Lista_de_pagos.txt', 'r') as pay:
        #     p = pay.read()
        # data2 = json.loads(p)
        # pay.close()

        # data2.append(pago)
        # y = json.dumps(data2,indent=2)
        # with open('Lista_de_pagos.txt', 'w') as pay:
        #     pay.write(y)

        resultado = pagos.insert_one(pago)
        print("Agregado")
        r = input("\nPresiona ENTER para volver")