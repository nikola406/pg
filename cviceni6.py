import sys
import requests
import json


url = 'https://www.jcu.cz/cz/'
url1 = 'https://data.carnewschina.com/suggest?q='
url2 = 'http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt'


def get_model_names(prefix):
    
    return []



if __name__ == "__main__":
    # responce = requests.get(url)
    # if responce.status_code == 200:
    #     print(responce.content)

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} prefix")
        sys.exit()

    prefix = sys.argv[1]
    models = get_model_names(prefix)
    for model in models:
        print(model)