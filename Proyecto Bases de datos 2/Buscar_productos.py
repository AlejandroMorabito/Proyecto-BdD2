from Productos import product
from Categorias import Categoria
from Precio import Precio
from Nombre import Nombre
from Disponibilidad import Disponibilidad

class Buscar():
    def Buscar(self):
        while True:
            print("")

            try:
                opc_BP = ["Categoría", "Precio", "Nombre","Disponibilidad en inventario","Salir"]
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
                    Categoria().Categoria()
                
                elif Selec_op_BP == 2:
                    Precio().Precio()
                
                elif Selec_op_BP == 3:
                    Nombre().Nombre()

                elif Selec_op_BP == 4:
                    Disponibilidad().Disponibilidad()

                elif Selec_op_BP == 5:
                    break
            except UnboundLocalError:
                pass