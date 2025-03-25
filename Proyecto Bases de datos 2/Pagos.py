import json

class pagos():
    def pagos(self):
        Pay = open('Lista_de_pagos.txt', 'w')
        data = []
        y = json.dumps(data)
        Pay.write(y)