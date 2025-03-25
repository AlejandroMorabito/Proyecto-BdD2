from Productos import product
import json

class Eliminar():
    def Eliminar(self):
        with open('Lista_de_productos.txt', 'r') as products:
            p = products.read()
        data = json.loads(p)
        
        while True:
            print("")
            # Te da a elegir entre todos los productos guardados
            try:
                print("Elige un producto para Eliminar")
                for index , dic in enumerate(data):
                    n = dic["name"]
                    d = dic["description"]
                    p = dic["price"]
                    c = dic["category"]
                    q = dic["quantity"]
                    print(f"{index+1}.- {n}:\n    {d}\n    $ {p}\n    Categoria: {c}\n    Disponibles: {q}")
                print(f"{len(data)+1}.- Salir")
                Selec_op_EP = int(input("Seleccione una opción: "))
                if Selec_op_EP < 1 or Selec_op_EP > len(data)+1:
                    raise ValueError
            except ValueError:
                Selec_op_EP = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")
            # Elimina el producto elegido y sobre escribe el .txt
            try:
                if Selec_op_EP >= 1 and Selec_op_EP <= len(data):
                    data.pop(Selec_op_EP-1)
                    y = json.dumps(data)
                    with open('Lista_de_productos.txt', 'w') as products:
                        products.write(y)
                    print("Eliminado")
                    r = input("\nPresiona ENTER para volver")
                    
                elif Selec_op_EP == len(data)+1:
                    break
            except UnboundLocalError:
                pass
            
            except UnboundLocalError:
                pass