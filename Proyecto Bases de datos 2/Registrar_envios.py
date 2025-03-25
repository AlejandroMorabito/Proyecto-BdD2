from pymongo import MongoClient
from urllib.parse import quote_plus
import json

class Registrar():
    def Registrar(self):
        # with open('Lista_de_envios.txt', 'r') as shipping:
        #     e = shipping.read()
        # data = json.loads(e)
        # shipping.close()
        usuario = "adaarellano"
        password = "12345"  # Reemplaza con tu contraseña real
        password_encoded = quote_plus(password)  # Codifica caracteres especiales
        connection_string = f"mongodb+srv://{usuario}:{password_encoded}@cluster.3awvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
        client = MongoClient(connection_string)
        db = client["TIENDA"]
        envios = db["Envios"]
        data = list(envios.find({}))

        while True:
            print("")
            N = input("Nombre del cliente: ")
            if N != "":
                break
            elif N == "":
                print("El nombre no es valido\nPor favor vuelva a escibirlo")
                r = input("\nPresiona ENTER para volver")

        while True:
            print("")

            try:
                opc_TP = ["MRW","Zoom","Delivery"]
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

            
        if opc_TP[Selec_op_TP-1] == "MRW":
            CE = 50
            DE = "Retiro en oficina"
        if opc_TP[Selec_op_TP-1] == "Zoom":
            CE = 40
            DE = "Retiro en oficina"
        if opc_TP[Selec_op_TP-1] == "Delivery":
            CE = 5
            DE = "Placa de la moto: GK026ZX"
        

        print("")
        while True:
            try:
                day =int(input("Coloca el dia (dd)"))
                if day < 1 or day > 31:
                    raise ValueError
                break
            except ValueError:
                print("Día no valido\nPor favor escibir un día valido")
                r = input("\nPresiona ENTER para volver")

        print("")
        while True:
            try:
                month =int(input("Coloca el mes (mm)"))
                if month < 1 or month > 12:
                    raise ValueError
                break
            except ValueError:
                print("Mes no valido\nPor favor escibir un mes valido")
                r = input("\nPresiona ENTER para volver")
        
        print("")
        while True:
            try:
                year =int(input("Coloca el año (yyyy)"))
                if year < 999:
                    raise ValueError
                break
            except ValueError:
                print("Año no valido\nPor favor escibir un año valido")
                r = input("\nPresiona ENTER para volver")
        
        fecha = f"{day}/{month}/{year}"    

        en = {
            "name": N,
            "envio": opc_TP[Selec_op_TP-1],
            "costo_envio": CE,
            "datos_envio": DE,
            "fecha": fecha
        }
        
        # print(fecha)
        # print(en)

        # shipping = open('Lista_de_envios.txt', 'r')
        # e = shipping.read()
        # data2 = json.loads(e)
        # shipping.close()

        # data2.append(en)
        # y = json.dumps(data2,indent=2)
        # shipping = open('Lista_de_envios.txt', 'w')
        # shipping.write(y)
        # shipping.close()

        resultado = envios.insert_one(en)
        print("Agregado")
        r = input("\nPresiona ENTER para volver")
