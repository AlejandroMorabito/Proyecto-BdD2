import json

class envios():
    def envios(self):
        Shipping = open('Lista_de_envios.txt', 'w')
        data = []
        y = json.dumps(data)
        Shipping.write(y)