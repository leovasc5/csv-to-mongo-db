import os, time, sys
from pymongo import MongoClient
from model.planilha import transferirDados

def createBase():
    os.system('cls')
    nomeHost = input('Nome do host: ')
    porta = int(input('Porta do host: '))

    try:
        client = MongoClient(nomeHost, porta)
        print('Procurando...\nAguarde, isso pode demorar um pouco...')
        print('\Bancos de dados encontrados: ')
        print(client.list_database_names())
    except:
        print('\nNenhuma base encontrada\nTente novamente...')
        time.sleep(2)
        createBase()

    os.system('cls')
    nomeBase = input('Nome da nova base de dados: ')
    nomeColecao = input('Nome da coleção onde serão armazenados os dados: ')
    caminho = input('Caminho para a planilha: ')
    separador = input('Caractere separador da planilha: ')
    
    transferirDados(client, nomeBase, nomeColecao, caminho, separador)