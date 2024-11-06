from resources.Consulta import consulta_produto, conectar_api

dados = conectar_api()
consulta_produto(dados)