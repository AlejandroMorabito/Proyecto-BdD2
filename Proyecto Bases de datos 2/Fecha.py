from pymongo import MongoClient
from urllib.parse import quote_plus
import json

class Fecha():
    def Fecha(self):
        # with open('Lista_de_ventas.txt', 'r') as sales:
        #     s = sales.read()
        # data = json.loads(s)
        usuario = "adaarellano"
        password = "12345"  # Reemplaza con tu contraseña real
        password_encoded = quote_plus(password)  # Codifica caracteres especiales
        connection_string = f"mongodb+srv://{usuario}:{password_encoded}@cluster.3awvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
        client = MongoClient(connection_string)
        db = client["TIENDA"]
        ventas = db["Ventas"]
        data = list(ventas.find({}))
        N = []
        for dic in data:
            for i,j in dic.items():
                if i == "fecha":
                    if j not in N:
                        N.append(j)
        N.append("Salir")

        while True:
            print("")

            try:
                print("Elija un fecha")
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
                    # with open('Lista_de_ventas.txt', 'r') as sales:
                    #     s = sales.read()
                    # data = json.loads(s)
                    for dic in data:
                        for i,j in dic.items():
                            if j == N[Selec_op_N-1]:
                                
                                f = dic["fecha"]
                                n = dic["name"]
                                pc = dic["prod_comp"]
                                cp = dic["cant_prod"]
                                tp = dic["tipo_pago"]
                                me = dic["met_Env"]
                                dc = dic["desgl_Comp"]
                                st = dc["subtotal"]
                                d = dc["descuento"]
                                p = d["persona"]
                                pago = d["pago"]
                                mp = d["forma_pago"]
                                td = d["total_desc"]
                                iva = dc["iva"]
                                igtf = dc["igtf"]
                                total = dc["total"]

                                
                                print(f"\nFecha: {f}\n    Nombre del comprador: {n}\n    Persona {p}\n    Forma de pago: {pago}\n    Moneda de pago: {mp}")
                
                                for index , l in enumerate(pc):
                                    print(f"    {l} .......... x{cp[index]}")
                                print(f"    Tipo de pago: {tp}\n    Forma de envio: {me}\n    Subtotal: $ {st}\n    Total del descuento: $ {td}\n    IVA a pagar: $ {iva}\n    IGTF: $ {igtf}\n    Total a pagar: $ {total}")


                                if p == "Juridica" and pago == "Credito":
                                    print("Puede pagar en cuotas de 15 o 30 días")
                    r = input("\nPresiona ENTER para volver")
            
                elif Selec_op_N == len(N):
                    break

            except UnboundLocalError:
                pass