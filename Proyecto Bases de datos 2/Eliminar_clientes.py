import json

class Eliminar():
    def Eliminar(self):
        with open('Lista_de_clientes.txt', 'r') as clients:
            cl = clients.read()
        data = json.loads(cl)
        
        while True:
            print("")

            try:
                print("Elige un producto para Eliminar")
                for index , dic in enumerate(data):
                    n = dic["name"]
                    p = dic["persona"]
                    r = dic["Ced_rif"]
                    cr = dic["correo"]
                    d = dic["direccion"]
                    t = dic["telefono"]
                    print(f"\n{index+1}.- {n}:\n    {p}\n    $ {r}\n    {cr}\n    {d}\n    {t}")
                print(f"{len(data)+1}.- Salir")
                Selec_op_EP = int(input("Seleccione una opción: "))
                if Selec_op_EP < 1 or Selec_op_EP > len(data)+1:
                    raise ValueError
            except ValueError:
                Selec_op_EP = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")

            try:
                if Selec_op_EP >= 1 and Selec_op_EP <= len(data):
                    data.pop(Selec_op_EP-1)
                    y = json.dumps(data)
                    with open('Lista_de_clientes.txt', 'w') as clients:
                        clients.write(y)
                    print("Eliminado")
                    r = input("\nPresiona ENTER para volver")

                    
                elif Selec_op_EP == len(data)+1:
                    break
            except UnboundLocalError:
                pass
            
            except UnboundLocalError:
                pass