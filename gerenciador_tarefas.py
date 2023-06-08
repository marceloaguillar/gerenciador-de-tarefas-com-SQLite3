import sqlite3
import pandas as pd
import time

def formatar_data(data):
    if len(data) < 2:
        return data
    elif len(data) < 4:
        return data[:2] + '/' + data[2:]
    elif len(data) < 8:
        return data[:2] + '/' + data[2:4] + '/' + data[4:]
    else:
        return data[:2] + '/' + data[2:4] + '/' + data[4:8]

while True:
    #ACESSANDO LISTA DE TAREFAS
    conexao = sqlite3.connect('C:\\Users\\positivo\\Documents\\python\\portfolio\\gerenciador_de_tarefas\\tarefas.db')
    consulta = "SELECT * FROM Tarefas"
    df = pd.read_sql_query(consulta, conexao)
    lista = df.to_string(header=False,index=False)
    conexao.close()

    #CRIAR MENU DE OPÇÕES(ADICIONAR, ATUALIZAR STATUS, EXCLUIR)
    print('\n---------------------GERENCIADOR DE TAREFAS---------------------')
    print(f'\n{lista}\n')
    print('O QUE DESEJA? \n\n1-ADICIONAR TAREFA\n2-ATUALIZAR STATUS\n3-EXCLUIR TAREFA\n4-PESQUISA POR DATA')
    opcoes = ['1','2','3','4']

    escolha = input('\nDIGITE A OPÇÃO: ')
    if escolha not in opcoes:
        print('\nESCOLHA UMA DAS OPÇÕES DISPONÍVEIS')
        time.sleep(5)
        continue
    
    #CRIAR CADA OPÇÃO
    elif escolha == '1':
        print('\n--ADICIONAR TAREFA--\n')
        nome_tarefa = input('NOME: ').upper()
        prazo_tarefa = input('DATA LIMITE: ')
        prazo_formatado = formatar_data(prazo_tarefa)
        print('Data formatada:', prazo_formatado)

        conexao = sqlite3.connect('tarefas.db')
        cursor = conexao.cursor()
        cursor.execute('''INSERT INTO Tarefas (Tarefas, Prazo, Status) values (?,?, ?)''', (nome_tarefa,prazo_formatado, 'PENDENTE'))
        conexao.commit()
        cursor.close()
        print('\nADICIONADO COM SUCESSO')

        #RETONAR PARA MENU INICIAL
        nova_acao = input('\nDESEJA EFETUAR NOVAS AÇÕES? \n1-SIM \n2-NÃO \n\nDIGITE A OPÇÃO: ')
        opcoes2 = ['1', '2']
        if nova_acao not in opcoes2:
            print('\nESCOLHA UMA DAS OPÇÕES DISPONÍVEIS')
        else:
            pass

        if nova_acao == '1':
            pass
        else: 
            break

    elif escolha == '2':
        print('--ATUALIZAÇÃO DE STATUS--')
        print(f'\n{lista}\n')
        id_tarefa = input('DIGITE O ID DA TAREFA: ')

        conexao = sqlite3.connect('C:\\Users\\positivo\\Documents\\python\\portfolio\\gerenciador_de_tarefas\\tarefas.db')
        cursor = conexao.cursor()
        cursor.execute('''UPDATE Tarefas SET Status = ? WHERE ID = ?''', ('CONCLUIDA',id_tarefa))
        conexao.commit()
        cursor.close()
        print('\nATUALIZADO COM SUCESSO')

        #RETONAR PARA MENU INICIAL
        nova_acao = input('\nDESEJA EFETUAR NOVAS AÇÕES? \n1-SIM \n2-NÃO \n\nDIGITE A OPÇÃO: ')
        opcoes2 = ['1', '2']
        if nova_acao not in opcoes2:
            print('\nESCOLHA UMA DAS OPÇÕES DISPONÍVEIS')
        else:
            pass

        if nova_acao == '1':
            pass
        else: 
            break

    elif escolha == '3':
        print('\n----EXCLUIR TAREFA----')
        print(f'\n{lista}\n')
        id_tarefa = input('DIGITE O ID DA TAREFA: ')

        conexao = sqlite3.connect('C:\\Users\\positivo\\Documents\\python\\portfolio\\gerenciador_de_tarefas\\tarefas.db')
        cursor = conexao.cursor()
        cursor.execute('''DELETE FROM Tarefas WHERE ID = ?''', (id_tarefa))
        conexao.commit()
        cursor.close()
        print('\nTAREFA EXCLUÍDA')

        #RETONAR PARA MENU INICIAL
        nova_acao = input('\nDESEJA EFETUAR NOVAS AÇÕES? \n1-SIM \n2-NÃO \n\nDIGITE A OPÇÃO: ')
        opcoes2 = ['1', '2']
        if nova_acao not in opcoes2:
            print('\nESCOLHA UMA DAS OPÇÕES DISPONÍVEIS')
        else:
            pass

        if nova_acao == '1':
            pass
        else: 
            break

    elif escolha == '4':
        print('\n----PESQUISA POR DATA----')
        data = input('\nDIGITE A DATA: ')
        data_formatada = formatar_data(data)
        conexao = sqlite3.connect('C:\\Users\\positivo\\Documents\\python\\portfolio\\gerenciador_de_tarefas\\tarefas.db')
        consulta1 = "SELECT * FROM Tarefas WHERE Prazo = ?"
        df = pd.read_sql_query(consulta1, conexao, params=(data_formatada,))
        lista1 = df.to_string(header=False, index=False)
        conexao.close()

        index = df.index
        if len(index) == 0:
            print('\nNÃO EXISTEM TAREFAS PARA ESSE DIA')
        else:
            print(f'\nAS TAREFAS PARA A DATA DE {data_formatada} são: ')
            print()
            print(lista1)

        #RETONAR PARA MENU INICIAL
        nova_acao = input('\nDESEJA EFETUAR NOVAS AÇÕES? \n1-SIM \n2-NÃO \n\nDIGITE A OPÇÃO: ')
        opcoes2 = ['1', '2']
        if nova_acao not in opcoes2:
            print('\nESCOLHA UMA DAS OPÇÕES DISPONÍVEIS')
        else:
            pass

        if nova_acao == '1':
            pass
        else: 
            break
