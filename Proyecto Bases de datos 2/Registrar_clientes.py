from pymongo import MongoClient
from urllib.parse import quote_plus
import json

class Registrar():
    def Registrar(self):
        # with open('Lista_de_clientes.txt', 'r') as clients:
        #     c = clients.read()
        # data = json.loads(c)
        # clients.close()
        usuario = "adaarellano"
        password = "12345"  # Reemplaza con tu contraseña real
        password_encoded = quote_plus(password)  # Codifica caracteres especiales
        connection_string = f"mongodb+srv://{usuario}:{password_encoded}@cluster.3awvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
        client = MongoClient(connection_string)
        db = client["TIENDA"]
        clientes = db["Clientes"]
        data = list(clientes.find({}))

        PC = []
        CP = []
        P = []
        Precios = []
        P_Subtotal = 0
        
        while True:
            print("")
            N = input("Nombre y Apellido o Razón Social: ")
            if N != "":
                break
            elif N == "":
                print("El nombre no es valido\nPor favor vuelva a escibirlo")
                r = input("\nPresiona ENTER para volver")
        
        while True:
            print("")

            try:
                opc_TP = ["Natural","Juridico"]
                print("Elige tu tipo de persona")
                for index , o in enumerate(opc_TP):
                    print(f"{index+1}.- {o}")
                Selec_op_TP = int(input("Seleccione una opción: "))
                if Selec_op_TP >= 1 and Selec_op_TP <= len(opc_TP):
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
                Ced_RIF=int(input("Cédula o RIF: "))
                break
            except ValueError:
                print("Cédula o RIF invalido\nPor favor escibir de nuevo")
                r = input("\nPresiona ENTER para volver")
        
        while True:
            print("")

            try:
                Correo = input("Correo electrónico: ")
                if "@" in Correo and ".com" in Correo and Correo.isalpha:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Correo invalido\nPor favor escibir de nuevo")
                r = input("\nPresiona ENTER para volver")
            
        while True:
            print("")

            try:
                Dirección = input("Dirección de envío: ")
                break
            except ValueError:
                print("Dirección invalida\nPor favor escibir de nuevo")
                r = input("\nPresiona ENTER para volver")

        while True:
            print("")

            try:
                Teléfono=int(input("Teléfono: "))
                break
            except ValueError:
                print("Teléfono invalido\nPor favor escibir de nuevo")
                r = input("\nPresiona ENTER para volver")


        cl = {
            "name": N,
            "persona": opc_TP[Selec_op_TP-1],
            "Ced_rif": Ced_RIF,
            "correo": Correo,
            "direccion": Dirección,
            "telefono": Teléfono
            }
        
        # with open('Lista_de_clientes.txt', 'r') as clients:
        #     c = clients.read()
        # data2 = json.loads(c)
        # clients.close()

        # data2.append(cl)
        # y = json.dumps(data2,indent=2)
        # with open('Lista_de_clientes.txt', 'w') as client:
        #     client.write(y)

        resultado = clientes.insert_one(cl)
        print("Agregado")
        r = input("Presiona ENTER para volver")
