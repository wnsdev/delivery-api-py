import requests
from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/api/hello')

def hello_world():
    '''
    Endpoint que nos livra da maldição.
    '''
    return {'Hello': 'World'}


@app.get('/api/restaurantes')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint que exibe o cardápio dos restaurantes.
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)

    match response.status_code: 
        case 200:
            dados_json = response.json()
            
            if restaurante is None:
                return {'Dados': dados_json}
            
            dados_restaurantes = []
            for item in dados_json:
                if item['Company'] == restaurante:
                    dados_restaurantes.append({
                        'item': item['Item'],
                        'price': item['price'],
                        'description': item['description']
                    })
            return {'Restaurante:': restaurante, 'Cardapio': dados_restaurantes}
        case _:
            return {
                'Erro': f'{response.status_code} - {response.text}'
            }