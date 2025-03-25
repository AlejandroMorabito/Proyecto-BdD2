from pymongo import MongoClient
from urllib.parse import quote_plus
from Productos import product
import json

class Registrar():
    def Registrar(self):
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
        ventas = db["Ventas"]

        PC = []
        CP = []
        P = []
        Precios = []
        P_Subtotal = 0
        
        while True:
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
            try:
                fecha = f"{day}/{month}/{year}"
                break
            except ValueError:
                print("Error en la fecha")
                r = input("\nPresiona ENTER para volver")


        while True:
            print("")
            N = input("Nombre del Cliente: ")
            if N != "":
                break
            elif N == "":
                print("El nombre no es valido\nPor favor vuelva a escibirlo")
                r = input("\nPresiona ENTER para volver")
        
        while True:
            print("")

            try:
                print("Elige un producto que te quieras llevar")
                for index , dic in enumerate(data):
                    P.append(dic["name"])
                    Precios.append(int(dic["price"]))
                    n = dic["name"]
                    d = dic["description"]
                    p = dic["price"]
                    c = dic["category"]
                    q = dic["quantity"]
                    print(f"{index+1}.- {n}:\n    {d}\n    $ {p}\n    Categoria: {c}\n    Disponibles: {q}")
                print(f"{len(data)+1}.- Salir")
                Selec_op_P = int(input("Seleccione una opción: "))
                if Selec_op_P < 1 or Selec_op_P > len(data)+1:
                    raise ValueError
            except ValueError:
                Selec_op_P = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")

            try:
                if Selec_op_P >= 1 and Selec_op_P <= len(data):
                    PC.append(P[Selec_op_P-1])
                    while True:
                        try:
                            f = int(input("Cuntos va a llevar: "))
                            CP.append(f)
                            P_Subtotal += (Precios[Selec_op_P-1] * f)
                            break
                        except ValueError:
                            print("Número no valido\nPor favor escibir un número")
                            r = input("\nPresiona ENTER para volver")
                    
                elif Selec_op_P == len(data)+1:
                    break

            except UnboundLocalError:
                pass
        
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
                opc_ME = ["MRW","Zoom","Delivery"]
                print("Elige el método de envío")
                for index , o in enumerate(opc_ME):
                    print(f"{index+1}.- {o}")
                Selec_op_ME = int(input("Seleccione una opción: "))
                if Selec_op_ME >= 1 or Selec_op_ME <= len(opc_ME):
                    break
                if Selec_op_ME < 1 or Selec_op_ME > len(opc_ME):
                    raise ValueError
            except ValueError:
                Selec_op_ME = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")

        while True:
            print("")

            try:
                print("¿Usted es una persona juridica?")
                opc_D = ["Si","No"]
                print("Eliga su respuesta")
                for index , o in enumerate(opc_D):
                    print(f"{index+1}.- {o}")
                Selec_op_D = int(input("Seleccione una opción: "))
                if Selec_op_D < 1 or Selec_op_D > len(opc_D):
                    raise ValueError

                print("")
                print("¿Va a pagar de contado?")
                opc_D2 = ["Si","No"]
                print("Eliga su respuesta")
                for index , o in enumerate(opc_D2):
                    print(f"{index+1}.- {o}")
                Selec_op_D2 = int(input("Seleccione una opción: "))
                if Selec_op_D2 < 1 or Selec_op_D2 > len(opc_D2):
                    raise ValueError

                if Selec_op_D == 1 and Selec_op_D2 == 1:
                    D = 0.05
                    TP = "Juridica"
                    FP = "Contado"
                    break
                
                else:
                    D = 0
                    if Selec_op_D == 1:
                        TP = "Juridica"

                    elif Selec_op_D == 2:
                        TP = "Natural"

                    if Selec_op_D2 == 1:
                        FP = "Contado"

                    elif Selec_op_D2 == 2:
                        FP = "Credito"

                    break
            except ValueError:
                Selec_op_D = 0
                Selec_op_D2 = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")

        while True:
            print("")

            try:
                print("¿Usted va a pagar en divisas?")
                opc_D = ["Si","No"]
                print("Eliga su respuesta")
                for index , o in enumerate(opc_D):
                    print(f"{index+1}.- {o}")
                Selec_op_D = int(input("Seleccione una opción: "))
                if Selec_op_ME < 1 or Selec_op_ME > len(opc_ME):
                    raise ValueError

                if Selec_op_D == 1:
                    IGTF = 0.03
                    MP = "Divisas"
                    break
                
                if Selec_op_D == 2:
                    IGTF = 0
                    MP = "Bolivares"
                    break
            except ValueError:
                Selec_op_ME = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")
                
        TD = P_Subtotal*D
        T_IVA = P_Subtotal*0.16
        T_IGTF = P_Subtotal*IGTF


        v = {
            "fecha": fecha,
            "name": N,
            "prod_comp": PC,
            "cant_prod": CP,
            "tipo_pago": opc_TP[Selec_op_TP-1],
            "met_Env": opc_ME[Selec_op_ME-1],
            "desgl_Comp": {
                            "subtotal": int(P_Subtotal), 
                            "descuento": {
                                        "persona": TP,
                                        "pago": FP,
                                        "forma_pago": MP,
                                        "total_desc": int(TD)
                                        },
                            "iva": int(T_IVA),
                            "igtf": int(T_IGTF),
                            "total": int(P_Subtotal-TD+T_IVA+T_IGTF)
                        }
            }
        
        # with open('Lista_de_ventas.txt', 'r') as sales:
        #     s = sales.read()
        # data2 = json.loads(s)
        # sales.close()

        # data2.append(v)
        # y = json.dumps(data2,indent=2)
        # with open('Lista_de_Ventas.txt', 'w') as sale:
        #     sale.write(y)
        
        resultado = ventas.insert_one(v)
        print("Agregado")
        r = input("\nPresiona ENTER para volver")
