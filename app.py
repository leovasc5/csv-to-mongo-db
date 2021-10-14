import os, time, sys, inspect
from model.database import createBase, consulta, insercao

os.system('cls')
try:
    key = int(input('Escolha uma opção: \n1 - Criar Base \n2 - Realizar Consulta \n3 - Realizar Inserção \n4 - Realizar Atualização (via ID) \n5 - Realizar Remoção\n6 - Sair\n\nUser: '))
except:
    print('Ocorreu um erro\nO App será reiniciado')
    time.sleep(2)
    os.startfile(__file__)
    sys.exit()

createBase() if key == 1 else None
consulta() if key == 2 else None
insercao() if key == 3 else None