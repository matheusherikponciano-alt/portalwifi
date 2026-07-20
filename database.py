import mysql.connector

conexao = mysql.connector.connect(
    host="shuttle.proxy.rlwy.net",
    port=43070,
    user="root",
    password="opjBKVJFKIcoGcprRlrBrXQsrDoKPHiW",
    database="railway"
)

cursor = conexao.cursor()

print("Banco conectado com sucesso!")