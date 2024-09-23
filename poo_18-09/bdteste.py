import sqlite3
conexao = sqlite3.connect("poo_18-09/Usuarios.db")
cursor = conexao.cursor()

#criar tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL, cpf TEXT NOT NULL)
                ''')
nome = "Cauê"
cpf = "123456789"
#insert
cursor.execute('''INSERT INTO user (nome,cpf) VALUES (?,?)''', (nome,cpf))
conexao.commit()

#update
nome = "Kenzo"
id1 = 7
cursor.execute('''UPDATE user set nome = ? where id = ?''', (nome,id1))
conexao.commit()

#select
cursor.execute('''SELECT * FROM user''')
for u in cursor.fetchall():
    print(u)

conexao.commit()
conexao.close()