import os, time, json
from pymongo import MongoClient
import pandas as pd

def transferirDados(client, nomeBase, caminho, separador):
    try:
        df = pd.read_csv(caminho, sep=separador, low_memory=False)
        print('Planilha encontrada!\nConteúdo:\n')
        print(df.head())
    except:
        os.system('cls')
        print('\nNenhuma planilha encontrada\nTente novamente...')
        time.sleep(2)
        os.system('cls')
        setCaminho(client, nomeBase, separador)

    if len(df.columns[df.columns.str.contains('unnamed', case = False)]) == 0:
        r = input('\nDeseja iniciar a transferência de dados em '+nomeBase+'?\n[s] Sim | [n] Não\n\nUser: ')

        if r == 's':
            nomeColecao = input('Nome da coleção onde serão armazenados os dados: ')
            df = pd.read_csv(caminho, sep=separador, low_memory=False)
            df.to_json('assets/temp.json', orient='records')
            with open('assets/temp.json') as f:
                client = MongoClient('localhost', 27017)
                file_data = json.load(f)
                db = client[nomeBase]
                print('Transferindo...')
                db[nomeColecao].insert(file_data)
                os.system('cls')
                client.close()
        else:
            print('\nTransferência cancelada...\nAté a próxima :)')
            time.sleep(2)
            exit()
    else:
        os.system('cls')
        key = int(input("Foi encontrada colunas 'separadoras' dentro da planilha. \n1 - Ignorar colunas vazias e criar base de dados com apenas uma coleção \n2 - Inserir cada parte dividida dentro de uma nova coleção \nUser: "))
        if key == 1:
            df = pd.read_csv(caminho, sep=separador, low_memory=False)
            columns = []
            temp_column = []
            n = 0

            for i in list(df.columns):
                if 'Unnamed' in i:
                    n+=1  
                else:
                    if n == 0:
                        temp_column.append(i)
                    else:
                        columns+=temp_column
                        temp_column.clear()
                        temp_column.append(i)
                        n = 0
            columns+=temp_column

            df = pd.read_csv(caminho, sep=separador, usecols=columns)
            r = input('\nDeseja iniciar a transferência de dados em '+nomeBase+'?\n[s] Sim | [n] Não\n\nUser: ')

            if r == 's':
                os.system('cls')
                nomeColecao = input('Nome da coleção onde serão armazenados os dados: ')
                df.to_json('assets/temp.json', orient='records')
                with open('assets/temp.json') as f:
                    file_data = json.load(f)
                    db = client[nomeBase]
                    print('Transferindo...')
                    db[nomeColecao].insert(file_data)
                    client.close()
                os.system('cls')
                os.remove("assets/temp.json")
                print('Transferência realizada com sucesso!')
            else:
                print('\nTransferência cancelada...\nAté a próxima :)')
                time.sleep(2)
                exit()
        elif key == 2:
            columns = []
            temp_column = []
            n = 0

            for i in list(df.columns):
                if 'Unnamed' in i:
                    n+=1  
                else:
                    if n == 0:
                        temp_column.append(i)
                    else:
                        columns.append(temp_column)
                        temp_column = []
                        temp_column.append(i)
                        n = 0
            columns+=[temp_column]
            os.system('cls')

            dfs = []
            colecoes = []
            for j in columns:
                dfs.append(pd.read_csv(caminho, sep=separador, usecols = j, low_memory=False))
                colecoes.append(input('\nColunas: ' + str(j) + '\nNome da coleção: '))

            os.system('cls')
            r = input('\nDeseja iniciar a transferência de dados em '+nomeBase+'?\n[s] Sim | [n] Não\n\nUser: ')
            
            if r == 's':
                n = 0
                for k in dfs:
                    k.to_json('assets/temp.json', orient='records')
                    with open('assets/temp.json') as f:
                        file_data = json.load(f)
                        db = client[nomeBase]
                        print('Transferindo...')
                        db[colecoes[n]].insert(file_data)
                        client.close()
                    os.system('cls')
                    os.remove("assets/temp.json")
                    print('Transferência realizada com sucesso!')
                    n+=1

def setCaminho(client, nomeBase, separador):
    os.system('cls')
    caminho = input('Caminho para a planilha: ')    
    transferirDados(client, nomeBase, caminho, separador)