import requests
import json

class product():
    def product(self):
        #Crea un .txt, copia la informacion del api, le agrega la disponibilidad y lo guarda en el .txt
        r = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/e20c412e7e1dcc3b089b0594b5a42f30ac15e49b/products.json')
        products = open('Lista_de_productos.txt', 'w')
        
        pr = r.text
        data = json.loads(pr)

        for i in data:
            i.update({"quantity": 20})
        
        y = json.dumps(data,indent=2)
        
        products.write(y)
