import json

class clients():
    def clients(self):
        Clients = open('Lista_de_clientes.txt', 'w')
        data = []
        y = json.dumps(data)
        Clients.write(y)