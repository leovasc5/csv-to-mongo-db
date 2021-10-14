from json.encoder import JSONEncoder
import os, time, json
from pymongo import MongoClient
from pprint import pprint

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

def consulta():
    os.system('cls')
    nomeHost = input('Nome do host: ')
    porta = int(input('Porta do host: '))

    try:
        if 1 == 1:
            client = MongoClient(nomeHost, porta)
            print('Procurando...\nAguarde, isso pode demorar um pouco...')
            os.system('cls')
            print('Escolha uma das bases de dados encontradas: ')
            bases = client.list_database_names()
            n = 0

            for i in bases:
                print(str(n+1)+ ' - ' + i)
                n+=1

            try:
                key = int(input('\nUser: '))
            except:
                print('\nErro, entrada inválida\nTente novamente...')
                time.sleep(2)
                consulta()

            if (key <= 0) or (key > (len(bases)+1)):
                print('\nErro, entrada inválida\nTente novamente...')
                time.sleep(2)
                consulta()

            os.system('cls')
            colecoes = client[bases[key-1]].collection_names()
            n = 0

            for i in colecoes:
                print(str(n+1) + ' - ' + i + '\n')
                n+=1

            try:
                key2 = int(input('Escolha a coleção: '))
            except:
                print('\nErro, entrada inválida\nTente novamente...')
                time.sleep(2)
                consulta()

            if (key2 <= 0) or (key2 > (len(colecoes)+1)):
                print('\nErro, entrada inválida\nTente novamente...')
                time.sleep(2)
                consulta()

            print('Base escolhida: ' + colecoes[key2-1])
            print(client[bases[key-1]][colecoes[key2-1]])
            query = input('\nQuery: ')

            try:
                res = client[bases[key-1]][colecoes[key2-1]].find(json.loads(query))
                os.system('cls')
                for i in res:
                    pprint(i)

                again = int(input('\n1 - Fazer mais uma consulta \n2 - Encerrar o processo \n\nUser:'))
                if again == 1:
                    consulta()
                else:
                    os.system('cls')
                    print('Volte sempre! :)')
                    time.sleep(3)
                    exit()

            except:
                os.system('cls')
                print('Não foi possível realizar a query :(')
                print('\nTente novamente...')
                time.sleep(3)
                consulta()

    except:
        print('\nNenhuma base encontrada\nTente novamente...')
        time.sleep(2)
        consulta()

def insercao():
    os.system('cls')
    nomeHost = input('Nome do host: ')
    porta = int(input('Porta do host: '))

    try:
        if 1 == 1:
            client = MongoClient(nomeHost, porta)
            print('Procurando...\nAguarde, isso pode demorar um pouco...')
            os.system('cls')
            print('Escolha uma das bases de dados encontradas: ')
            bases = client.list_database_names()
            n = 0

            for i in bases:
                print(str(n+1)+ ' - ' + i)
                n+=1

            try:
                key = int(input('\nUser: '))
            except:
                print('\nErro, entrada inválida\nTente novamente...')
                time.sleep(2)
                consulta()

            if (key <= 0) or (key > (len(bases)+1)):
                print('\nErro, entrada inválida\nTente novamente...')
                time.sleep(2)
                consulta()

            os.system('cls')
            colecoes = client[bases[key-1]].collection_names()
            n = 0

            for i in colecoes:
                print(str(n+1) + ' - ' + i + '\n')
                n+=1

            try:
                key2 = int(input('Escolha a coleção: '))
            except:
                print('\nErro, entrada inválida\nTente novamente...')
                time.sleep(2)
                insercao()

            if (key2 <= 0) or (key2 > (len(colecoes)+1)):
                print('\nErro, entrada inválida\nTente novamente...')
                time.sleep(2)
                insercao()

            print('Base escolhida: ' + colecoes[key2-1])
            print(client[bases[key-1]][colecoes[key2-1]])
            query = input('\nQuery: ')

            try:
                client[bases[key-1]][colecoes[key2-1]].insert(json.loads(query))
                os.system('cls')
                print("\nDocumento inserido com sucesso!")
                again = int(input('\n1 - Inserir mais um documento \n2 - Encerrar o processo \n\nUser: '))
                if again == 1:
                    insercao()
                else:
                    os.system('cls')
                    print('Volte sempre! :)')
                    time.sleep(3)
                    exit()

            except:
                os.system('cls')
                print('Não foi possível realizar a query :(')
                print('\nTente novamente...')
                time.sleep(3)
                insercao()

    except:
        print('\nNenhuma base encontrada\nTente novamente...')
        time.sleep(2)
        insercao()