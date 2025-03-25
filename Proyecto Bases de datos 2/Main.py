from Productos import product
from Ventas import sales
from Clientes import clients
from Pagos import pagos
from Envios import envios
from Gestión_de_productos import Gestión
from Gestión_de_ventas import Ventas
from Gestión_de_clientes import G_Clientes
from Gestión_de_pagos import G_Pagos
from Gestión_de_envios import G_Envios
#from Estaditicas import estadisticas

class main():
    def main(self):
                
        while True:
            print("")
            
            try:
                opciones = ["Gestión de productos","Gestión de ventas","Gestión de clientes","Gestión de pagos","Gestión de envíos","Salir"] #,"Indicadores de gestión (estadísticas)"
                for index , o in enumerate(opciones):
                    print(f"{index+1}.- {o}")
                Selec_op = int(input("Seleccione una opción: "))
                if Selec_op < 1 or Selec_op > len(opciones):
                    raise ValueError
            except ValueError:
                Selec_op = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")
            
            try:
                if Selec_op == 1:
                    Gestión().gestión()
                
                elif Selec_op == 2:
                    Ventas().Ventas()
                
                elif Selec_op == 3:
                    G_Clientes().G_Clientes()
                
                elif Selec_op == 4:
                    G_Pagos().G_Pagos()
                
                elif Selec_op == 5:
                    G_Envios().G_Envios()
                
                elif Selec_op == 6:
                #     estadisticas().estadisticas()
                
                # elif Selec_op == 7:
                    break
            
            except UnboundLocalError:
                pass
