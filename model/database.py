import os, time, json
from pymongo import MongoClient
from pprint import pprint

from model.planilha import transferirDados

def createBase():
    client = connect(1)

    try:
        print('\Bancos de dados encontrados: ')
        print(client.list_database_names())
    except:
        print('\nNenhuma base encontrada\nTente novamente...')
        time.sleep(2)
        createBase()

    os.system('cls')
    nomeBase = input('Nome da nova base de dados: ')
    caminho = input('Caminho para a planilha: ')
    separador = input('Caractere separador da planilha: ')
    
    transferirDados(client, nomeBase, caminho, separador)

def action(mode, passDirect = None):
    if passDirect == None:
        global client
        client = connect(mode)
    os.system('cls')

    try:
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
            action(mode)

        if (key <= 0) or (key > (len(bases)+1)):
            print('\nErro, entrada inválida\nTente novamente...')
            time.sleep(2)
            action(mode)

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
            action(mode)

        if (key2 <= 0) or (key2 > (len(colecoes)+1)):
            print('\nErro, entrada inválida\nTente novamente...')
            time.sleep(2)
            action(mode)

        os.system('cls')
        print('Base escolhida: ' + colecoes[key2-1])

        if mode == 2:
            query = input('Query: ')
            res = client[bases[key-1]][colecoes[key2-1]].find(json.loads(query))
            os.system('cls')
            for i in res:
                pprint(i)

            again = int(input('\n1 - Realizar mais uma consulta \n2 - Encerrar o processo \n\nUser: '))
            if again == 1:
                action(mode, True)
            else:
                os.system('cls')
                print('Volte sempre! :)')
                time.sleep(3)
                exit()
        elif mode == 3:
                query = input('\nQuery: ')
                client[bases[key-1]][colecoes[key2-1]].insert(json.loads(query))
                os.system('cls')
                print("\nDocumento inserido com sucesso!")
                again = int(input('\n1 - Inserir mais um documento \n2 - Encerrar o processo \n\nUser: '))
                if again == 1:
                    action(key, True)
                else:
                    os.system('cls')
                    print('Volte sempre! :)')
                    time.sleep(3)
                    exit()
        elif mode == 4:
            os.system('cls')
            doc = input('Escreva a query identificadora: ')
            val = input('\nEscreva a query com os novos valores: ')
            client[bases[key-1]][colecoes[key2-1]].update(json.loads(doc), json.loads(val))
            os.system('cls')
            print("\nDocumento atualizado com sucesso!")
            again = int(input('\n1 - Atualizar mais um documento \n2 - Encerrar o processo \n\nUser: '))
            if again == 1:
                action(key, True)
            else:
                os.system('cls')
                print('Volte sempre! :)')
                time.sleep(3)
                exit()
        elif mode == 5:
            query = input('\nQuery: ')
            client[bases[key-1]][colecoes[key2-1]].remove(json.loads(query))
            os.system('cls')
            print("\nDocumento removido com sucesso!")
            again = int(input('\n1 - Remover mais um documento \n2 - Encerrar o processo \n\nUser: '))
            if again == 1:
                action(key, True)
            else:
                os.system('cls')
                print('Volte sempre! :)')
                time.sleep(3)
                exit()
    except:
        print('\nNenhuma base encontrada\nTente novamente...')
        time.sleep(2)
        action(mode)

def connect(mode):
    try:
        os.system('cls')
        nomeHost = input('Nome do host: ')
        porta = int(input('Porta do host: '))
        cl = MongoClient(nomeHost, porta)
        print('Procurando...\nAguarde, isso pode demorar um pouco...')
        os.system('cls')
        return(cl)
    except:
        os.system('cls')
        key = input('Algo deu errado...\n Tentar novamente? [s] Sim | [n] Não \nUser:')
        if key == 's':
            createBase() if mode == 1 else None
            action(mode) if mode >= 2 and key <= 5 else None