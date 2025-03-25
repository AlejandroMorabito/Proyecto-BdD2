from Cliente import Cliente
from Fecha import Fecha
from Monto import Monto

class Buscar():
    def Buscar(self):
        while True:
            print("")

            try:
                opc_BV = ["Cliente","Fecha de la venta","Monto total de la venta","Salir"]
                print("Elige el filtro que con el que quieres buscar")
                for index , o in enumerate(opc_BV):
                    print(f"{index+1}.- {o}")
                Selec_op_BV = int(input("Seleccione una opción: "))
                if Selec_op_BV < 1 or Selec_op_BV > len(opc_BV):
                    raise ValueError
            except ValueError:
                Selec_op_BV = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")

            try:
                if Selec_op_BV == 1:
                    Cliente().cliente()
                
                elif Selec_op_BV == 2:
                    Fecha().Fecha()
                
                elif Selec_op_BV == 3:
                    Monto().Monto()

                elif Selec_op_BV == 4:
                    break
            except UnboundLocalError:
                pass