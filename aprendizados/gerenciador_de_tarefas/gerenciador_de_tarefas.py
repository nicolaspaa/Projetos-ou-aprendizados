import sqlite3
import os

with sqlite3.connect('tarefas.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS to_do_list (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,                  
                    description TEXT NOT NULL,
                    status BOOLEAN NOT NULL DEFAULT 0
                    )''')
    
    while True:
        acao = int(input('''Você deseja:
adicionar tarefa? digite 1
remover tarefa? digite 2
ver lista de afazeres? digite 3
limpar a lista inteira? digite 4
'''))

        if acao == 1:
            titulo = str(input('titulo: '))
            if not titulo:
                print('Não pode ser vazio\n')
                continue
            
            descricao = str(input('descricao: '))
            if not descricao:
                print('Não pode ser vazio\n')
                continue

            andamento = str(input('andamento: s/n: '))
            andamento_tf = 1 if andamento == 's' else 0

            cursor.execute('''INSERT INTO to_do_list (title, description, status) VALUES (?, ?, ?)''', (titulo, descricao, andamento_tf)) 
            connection.commit()


        elif acao == 2:
            try:
                taskID = int(input('Qual o número da tarefa a ser removida? '))
            except ValueError:
                print('Digite um valor inteiro')
                continue

            cursor.execute('DELETE FROM to_do_list WHERE id = ?', (taskID,))
            connection.commit()
            
            if cursor.rowcount == 1:
                print('tarefa deletada')  
            else: 
                print('tarefa inexistente')


        elif acao == 3:
            cursor.execute('''SELECT * FROM to_do_list''')
            tarefas = cursor.fetchall()
            
            for tarefa in tarefas:
                id, titulo, descricao, andamento_escrito = tarefa
                andamento_escrito = 'em andamento' if andamento_tf == 1 else 'não começada'

                print(f'''Tarefa número {id}:
    Título - {titulo}
    Descrição - {descricao}
    Status - {andamento_escrito}
                
''')

 
        elif acao == 4:
            cursor.execute('DELETE FROM to_do_list')
            cursor.execute('UPDATE sqlite_sequence SET seq = 0 WHERE name = "to_do_list"')
            connection.commit()


        else:
            print('Essa opção não existe')

   
        usuario_usando = str(input('''Deseja continuar? s/n: '''))
        os.system('cls')


        if usuario_usando != 's':
            break

