from Cedula_Rif import Cedula_Rif
from Correo import Correo

class Buscar():
    def Buscar(self):
        while True:
            print("")

            try:
                opc_BV = ["Cédula o RIF","Correo electrónico","Salir"]
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
                    Cedula_Rif().Cedula_Rif()
                
                elif Selec_op_BV == 2:
                    Correo().Correo()

                elif Selec_op_BV == 3:
                    break
            except UnboundLocalError:
                pass