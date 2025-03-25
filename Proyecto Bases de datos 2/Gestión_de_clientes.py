from Registrar_clientes import Registrar
# from Modificar_clientes import Modificar
# from Eliminar_clientes import Eliminar
from Buscar_clientes import Buscar

class G_Clientes():
    def G_Clientes(self):
        while True:
            print("")

            try:
                opc_GP = ["Registrar nuevos clientes","Buscar clientes","Salir"] #,"Modificar información de clientes","Eliminar clientes"
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
                    Registrar().Registrar()
                
                # elif Selec_op_GP == 2:
                    # Modificar().Modificar()
                
                # elif Selec_op_GP == 3:
                    # Eliminar().Eliminar()
                
                elif Selec_op_GP == 2:  # 4
                    Buscar().Buscar()

                elif Selec_op_GP == 3: # 5
                    break
            
            except UnboundLocalError:
                pass

