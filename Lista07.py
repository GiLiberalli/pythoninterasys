import pytest
import csv
import json
import requests

#Leitura de Script:

teste_informacoes_filme_lista07 = [

    ('tt0120737', 'The Lord of the Rings: The Fellowship of the Ring', '2001', 'Peter Jackson'),
    ('tt0110413', 'Léon: The Professional', '1994', 'Luc Besson'),
    ('tt0045152', "Singin' in the Rain", '1952', 'Gene Kelly')
]

@pytest.mark.parametrize('id,nome,ano,diretor', teste_informacoes_filme_lista07)

def testar_filmes_lista07(id,nome,ano,diretor):
    from requests import HTTPError
    try:
        response = requests.get(f'https://imdb-api.com/en/API/Title/k_heogps76/{id}')
        jsonResponse = response.json()
        id_movie = jsonResponse['id']
        title_movie = jsonResponse['title']
        year_movie = jsonResponse ['year']

        assert id_movie == id
        assert title_movie == nome
        assert year_movie == ano

    except HTTPError as http_fail:
        print(f'Um erro de HTTP aconteceu: {http_fail}')
    except Exception as fail:
        print(f'Falha Inesperada:{fail}')

#Leitura de CSV

informacoes_de_filmes = [

    (1,'Star Wars', 1979),
    (2, 'Planeta do Tesouro', 2002),
    (3, 'Walle', 2018)
]

def ler_nome_dos_filmes():
    teste_dados_csv = []
    nome_arquivo = 'Lista07.csv'
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
        print(f'Erro: {fail}')

def classificacoes_filmes(nota):
    media = 7
    if(nota>=media):
        return 'Good'
    else:
        return 'Bad'


@pytest.mark.parametrize('id,nome,ano,nota,resultado',ler_nome_dos_filmes())

def test_comparacoes_csv(id,nome,ano,nota,resultado):
    nota_filme = classificacoes_filmes(int(nota))
    assert nota_filme == resultado




