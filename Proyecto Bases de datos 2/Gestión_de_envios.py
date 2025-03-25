from Registrar_envios import Registrar
from Buscar_envios import Buscar

class G_Envios():
    def G_Envios(self):
        while True:
            print("")

            try:
                opc_GP = ["Registrar envios","Buscar envios","Salir"]
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
                
                elif Selec_op_GP == 2:
                    Buscar().Buscar()

                elif Selec_op_GP == 3:
                    break
            
            except UnboundLocalError:
                pass