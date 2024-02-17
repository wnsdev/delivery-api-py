import json

for nome_do_restaurante, dados in dados_restaurantes.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)