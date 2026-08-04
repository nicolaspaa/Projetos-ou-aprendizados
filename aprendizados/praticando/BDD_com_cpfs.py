import sqlite3
import random

connection = sqlite3.connect('BDD2.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tabela_de_cpfs (
               id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
               cpfs TEXT NOT NULL UNIQUE   
               )''')

#cursor.execute('''INSERT INTO tabela_de_cpfs
#               (cpf) VALUES
#               ('549.134.948-80')''')

def gerar_cpf():
    return [random.randint(0, 9) for _ in range(11)]
 
 
def calcular_digito(cpf_parcial):
    tamanho = len(cpf_parcial)
    soma = sum(cpf_parcial[i] * (tamanho + 1 - i) for i in range(tamanho))
    resto = (soma * 10) % 11
    return 0 if resto == 10 else resto
 
 
def validar_cpf(cpf):
    primeiros_9 = cpf[:9]
    digito1 = calcular_digito(primeiros_9)
    digito2 = calcular_digito(primeiros_9 + [digito1])
    return digito1 == cpf[9] and digito2 == cpf[10]
 
 
def formatar_cpf(cpf):
    numeros = ''.join(str(d) for d in cpf)
    return f"{numeros[0:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:11]}"
 
while True:
    criar_cpf = str(input('Gerar cpf? '))
    if criar_cpf == 'sim':
        cpf = gerar_cpf()
        existe = validar_cpf(cpf)
        cpf_formatado = formatar_cpf(cpf)
    
        if existe:
            print(f"{formatar_cpf(cpf)} - esse CPF existe")
        else:
            print(f"{formatar_cpf(cpf)} - esse CPF não existe")

        resposta = str(input('Deseja adicionar ao banco de dados? '))
        if resposta == 'sim':
            cursor.execute(f'''INSERT INTO tabela_de_cpfs
                           (cpfs) VALUES
                           (?)''', (cpf_formatado,))
            connection.commit()

        elif resposta == 'nao':
            continue
        else:
            break
    else:
        break
    
print('bye')
connection.close()
    
    