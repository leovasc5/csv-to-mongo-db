import os, time, json
from pymongo import MongoClient
import pandas as pd

def transferirDados(client, nomeBase, nomeColecao, caminho, separador):
    try:
        df = pd.read_csv(caminho, sep=separador, low_memory=False)
        print('Planilha encontrada!\nConteúdo:\n')
        print(df.head())
    except:
        os.system('cls')
        print('\nNenhuma planilha encontrada\nTente novamente...')
        time.sleep(2)
        os.system('cls')
        setCaminho(client, nomeBase, nomeColecao, separador)
    
    r = input('\nDeseja iniciar a transferência de dados em '+nomeBase+'?\n[s] Sim | [n] Não\n\nUser: ')
    
    if r == 's':
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

def setCaminho(client, nomeBase, nomeColecao, separador):
    os.system('cls')
    caminho = input('Caminho para a planilha: ')    
    transferirDados(client, nomeBase, nomeColecao, caminho, separador)