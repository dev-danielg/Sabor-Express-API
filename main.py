from fastapi import FastAPI, Query
import requests

app = FastAPI()


@app.get("/api/restaurantes")
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios de um restaurante especificado na query.
    Se nenhum restaurante for informado na query,
    retorna os dados de todos os restaurantes

    '''
    url = (
        'https://guilhermeonrails.github.io/api-restaurantes/'
        'restaurantes.json'
    )
    response = requests.get(url)
    if response.status_code == 200:
        dados_restaurante = []
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    'Item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return {'Erro': f'{response.status_code}',
                'Descricao': {f'{response.text}'}}
