import sqlite3

connection = sqlite3.connect('banco_de_dados.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS contas_bancarias (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               titular TEXT NOT NULL,
               saldo FLOAT NOT NULL,
               cpf TEXT NOT NULL UNIQUE
               )''')

#cursor.execute('''INSERT INTO contas_bancarias
#              (titular, saldo, cpf) VALUES
#              ('nicolas', 234, '54913494880')''')

cursor.execute('''SELECT * FROM contas_bancarias''')
contas = cursor.fetchall()
for conta in contas:
    id, titular, saldo, cpf = conta
    print(f'''{id}
{titular}
{saldo}
{cpf}\n''')

connection.commit()

