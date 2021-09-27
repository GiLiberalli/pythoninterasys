# 1 - imports - bibliotecas
import pytest

# 2 - class - classe


# 3 - definitions - definições = métodos e funções
def print_hi(name):
    print(f'Oi, {name}')

def somar(numero1, numero2):
    return numero1 + numero2 #bug

def subtrair(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    else:
        return 'Não dividirás por zero'

#Testes Unitários/ Teste de Unidades

   #teste da função de somar

@pytest.mark.parametrize('numero1,numero2,resultado',[
    #valores
    (5, 4, 9), # teste 1
    (3, 2, 5), # teste 2
    (10,6, 16), # teste 3
])
def test_somar(numero1, numero2, resultado):
    assert somar(numero1,numero2) == resultado


      #1 - Configura/Prepara
       #numero1 = 8  #input / entrada
       #numero2 = 5  #input / entrada
       #resultado_esperado = 13  #output / saída

       #2 - Executa

       #resultado_atual = somar(numero1, numero2)

       #3 Check / Valida
       #assert resultado_atual == resultado_esperado

def test_somar_compacto():
    assert somar(8,5) == 13

def test_subtrair():
    assert  subtrair(4,5) == -1

if __name__ == '__main__':

    print_hi('Giovanna')

    # soma de 2 números
    resultado = somar(4,2)
    print(f'O resultado da soma: {resultado}')

    # subtração de 2 números
    resultado = subtrair(5,3)
    print(f'O resultado da subtração: {resultado}')

    # multiplicação
    resultado = multiplicar(2,4)
    print(f'O resultado da multiplicação: {resultado}')

    # divisão
    resultado = dividir(9,8)
    print(f'O resultado da divisão: {resultado}')



