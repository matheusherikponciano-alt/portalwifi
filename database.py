import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wifi_true"
)

cursor = conexao.cursor()

print("Banco conectado com sucesso!")