from Agregar_productos import Agregar
from Buscar_productos import Buscar
# from Modificar_productos import Modificar
# from Eliminar_productos import Eliminar

class Gestión():
    def gestión(self):
        while True:
            print("")

            try:
                opc_GP = ["Agregar nuevos productos","Buscar productos","Salir"] #,"Modificar información de producto existente","Eliminar productos"
                for index , o in enumerate(opc_GP):
                    print(f"{index+1}.- {o}")
                Selec_op_GP = int(input("Seleccione una opción: "))
                if Selec_op_GP < 1 or Selec_op_GP > len(opc_GP):
                    raise ValueError
            except ValueError:
                Selec_op_GP = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")
                print("")

            try:
                if Selec_op_GP == 1:
                    Agregar().Agregar()
                
                elif Selec_op_GP == 2:
                    Buscar().Buscar()
                
                elif Selec_op_GP == 3:
                #     Modificar().Modificar()
                
                # elif Selec_op_GP == 4:
                #     Eliminar().Eliminar()

                # elif Selec_op_GP == 5:
                    break
            
            except UnboundLocalError:
                pass
