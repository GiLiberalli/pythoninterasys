# 1 - imports
import json
import pytest
import csv
import requests

teste_dados_novos_usuarios = [

    (1, 'Juca', 'Pirama', 'juca@interasys.com.br') ,             # usuario 1
    (2, 'Agatha', 'Cristine', 'agatha@interasys.com.br')         # usuario 2
]

teste_dados_usuarios_atuais = [

    (1, 'George', 'Bluth', 'george.bluth@reqres.in') ,
    (2, 'Janet', 'Weaver', 'janet.weaver@reqres.in')         # usuario 2
]


# CRUD/ ICAE                   #Traduções
# Aplicações   APIS            APIs
# Create       Post            Incluir/Publicar
# Reach / Research  Get        Consultar/Pegar
# Update  Put                  Atualizar
# Delete  Delete               Excluir

@pytest.mark.parametrize('id,nome,sobrenome,email', teste_dados_usuarios_atuais)

def testar_dados_usuarios(id, nome, sobrenome, email, json_response=None):  # função que testa o algo
    from requests import HTTPError
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        jsonResponse = response.json()
        id_obtido = jsonResponse['data']['id']
        nome_obtido = jsonResponse['data']['first_name']
        sobrenome_obtido = jsonResponse['data']['last_name']
        email_obtido = jsonResponse['data']['email']

        print(f'id: {id_obtido} - nome: {nome_obtido} - sobrenome: {sobrenome_obtido} - email: {email_obtido}')
        print(json.dumps(json_response, indent=2, sort_keys=True))

        assert id_obtido == id
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email

    except HTTPError as http_fail :  # Para o ISTQB, descobriu rodando que é falha
        print(f'Um erro de HTTP aconteceu: {http_fail}')
    except Exception as fail:
        print(f'Falha Inesperada:{fail}')


 #funcion que testa
 #função que faz algo --> Fora do meu computador
 #API que vamos usar para fazer o teste:
 # https://reqres.in/api/users

#Leitor do arquivo csv:

def ler_dados_do_csv():
    teste_dados_csv = []
    nome_arquivo = 'usuarios.csv'
    try:
       with open(nome_arquivo,newline='') as csvfile:
           dados = csv.reader(csvfile,delimiter = ',')
           next(dados)
           for linha in dados:
               teste_dados_csv.append(linha)
       return teste_dados_csv
    except FileNotFoundError:
        print('Arquivo Não Encontrado')
    except Exception as fail:
        print(f'Falha Imprevista: {fail}')


