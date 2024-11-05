import requests

def fazer_consulta(token):
    product_id = None
    url = f"https://api.mercadolibre.com/items/{product_id}"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        product_data = response.json()
        price = product_data['price']
        print(f"Preço do produto {product_id}: R${price}")
    else:
        print("Erro ao obter dados do produto.")