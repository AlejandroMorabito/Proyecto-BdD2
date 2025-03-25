from Registrar_venta import Registrar
from Generar_factura import Factura
from Buscar_ventas import Buscar

class Ventas():
    def Ventas(self):
        while True:
            print("")

            try:
                opc_GV = ["Registrar venta","Generar factura","Buscar ventas","Salir"]
                for index , o in enumerate(opc_GV):
                    print(f"{index+1}.- {o}")
                Selec_op_GV = int(input("Seleccione una opción: "))
                if Selec_op_GV < 1 or Selec_op_GV > len(opc_GV):
                    raise ValueError
            except ValueError:
                Selec_op_GV = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")
                print("")

            try:
                if Selec_op_GV == 1:
                    Registrar().Registrar()
                
                elif Selec_op_GV == 2:
                    Factura().Factura()
                
                elif Selec_op_GV == 3:
                    Buscar().Buscar()

                elif Selec_op_GV == 4:
                    break
            
            except UnboundLocalError:
                pass
