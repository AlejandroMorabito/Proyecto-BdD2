from Cliente_pagos import Cliente
from Fecha_pago import Fecha
from Tipo import Tipo
from Moneda import Moneda  

class Buscar():
    def Buscar(self):
        while True:
            print("")

            try:
                opc_BP = ["Cliente","Fecha","Tipo de pago","Moneda de pago","Salir"]
                print("Elige el filtro que con el que quieres buscar")
                for index , o in enumerate(opc_BP):
                    print(f"{index+1}.- {o}")
                Selec_op_BP = int(input("Seleccione una opción: "))
                if Selec_op_BP < 1 or Selec_op_BP > len(opc_BP):
                    raise ValueError
            except ValueError:
                Selec_op_BP = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")

            try:
                if Selec_op_BP == 1:
                    Cliente().cliente()
                
                elif Selec_op_BP == 2:
                    Fecha().fecha()
                
                elif Selec_op_BP == 3:
                    Tipo().tipo()
                
                elif Selec_op_BP == 4:
                    Moneda().moneda()

                elif Selec_op_BP == 5:
                    break
            except UnboundLocalError:
                pass