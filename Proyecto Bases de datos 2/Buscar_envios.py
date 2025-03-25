from Cliente_envios import Cliente
from Fecha_envios import Fecha

class Buscar():
    def Buscar(self):
        while True:
            print("")

            try:
                opc_BP = ["Cliente","Fecha","Salir"]
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
                    break
            except UnboundLocalError:
                pass