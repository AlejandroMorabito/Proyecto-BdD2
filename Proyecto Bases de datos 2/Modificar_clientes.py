import json

class Modificar():
    def Modificar(self):
        with open('Lista_de_clientes.txt', 'r') as clients:
            c = clients.read()
        data = json.loads(c)
        
        while True:
            print("")

            try:
                print("Elige un producto para modificar")
                for index , dic in enumerate(data):
                    n = dic["name"]
                    p = dic["persona"]
                    r = dic["Ced_rif"]
                    cr = dic["correo"]
                    d = dic["direccion"]
                    t = dic["telefono"]
                    print(f"\n{index+1}.- {n}:\n    {p}\n    $ {r}\n    {cr}\n    {d}\n    {t}")
                print(f"{len(data)+1}.- Salir")
                Selec_op_MP = int(input("Seleccione una opción: "))
                if Selec_op_MP < 1 or Selec_op_MP > len(data)+1:
                    raise ValueError
                elif Selec_op_MP == len(data)+1:
                    break
            except ValueError:
                Selec_op_MP = 0
                print("Selección invalida")
                r = input("\nPresiona ENTER para volver")

            try:
                if Selec_op_MP >= 1 and Selec_op_MP <= len(data):
                    M = []
                    for dic in data:
                        for i,j in dic.items():
                            if i not in M:
                                M.append(i)
                    M.append("Salir")

                    while True:
                        print("")
                            
                        try:
                            print("Elija la que quiere modificar")
                            for index , o in enumerate(M):
                                print(f"{index+1}.- {o}")
                            Selec_op_M = int(input("Seleccione una opción: "))
                            if Selec_op_M < 1 or Selec_op_M > len(M):
                                raise ValueError
                        
                        except ValueError:
                            Selec_op_M = 0
                            print("Selección invalida")
                            r = input("\nPresiona ENTER para volver")

                        try:
                            if Selec_op_M >= 1 and Selec_op_M <= len(M)-1:
                                m = M[Selec_op_M-1]
                                n = data[Selec_op_MP-1]
                                n[m]= input("Modificación: ")
                                y = json.dumps(data)
                                with open('Lista_de_clientes.txt', 'w') as clients:
                                    clients.write(y)
                                return print("Modificado")
                                
                            elif Selec_op_M == len(M):
                                break
                        except UnboundLocalError:
                            pass
            
            except UnboundLocalError:
                pass
