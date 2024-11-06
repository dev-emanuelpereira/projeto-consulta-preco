import yaml
import requests

def config():
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    bearer_token = config["usuario"]["bearer_token"]
    return bearer_token

def conectar_api():
    token = config()

    produto = str(input('Produto a ser avaliado '))
    quantidade = str(input('Quantos produtos quer que apareça? '))

    url = f"https://api.mercadolibre.com/sites/MLB/search?q={produto}&limit={quantidade}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    body = requests.get(url, headers=headers)
    return body

def consulta_produto(body):
    if body.status_code == 200:
        dados = body.json()
        if 'results' in dados:
            for produto in dados['results']:
                print(
                    f'''
-----------------------------
Nome: {produto['title']}
Valor: R$ {produto['price']}

Link: {produto['permalink']}
-----------------------------
                    '''
                )
        else:
            print("Nenhum resultado encontrado.")
    else:
        print("Erro na requisição:", body.status_code)
        return None