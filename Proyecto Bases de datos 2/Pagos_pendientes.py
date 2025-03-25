import json

class P_pendientes():
    def P_pendientes(self):
        with open('Lista_de_pagos.txt', 'r') as pay:
            p = pay.read()
        data = json.loads(p)
        CP = []
        for dic in data:
            for i,j in dic.items():
                if i == "pago":
                    if j == "Credito":
                        CP.append(dic["name"])
        
        print("Clientes con pagos pedientes por credito:")
        for i in CP:
            print(f"- {i}")
        
        r = input("\nPresiona ENTER para volver")

