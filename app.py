import os, time, sys, inspect
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir)

from model.database import createBase

os.system('cls')
try:
    key = int(input('Escolha uma opção: \n1 - Criar Base \n2 - Realizar Consulta \n3 - Realizar Inserção \n4 - Realizar Atualização (via ID) \n5 - Realizar Remoção\n6 - Sair\nUser: '))
except:
    print('Ocorreu um erro\nO App será reiniciado')
    time.sleep(2)
    os.startfile(__file__)
    sys.exit()

createBase() if key == 1 else None