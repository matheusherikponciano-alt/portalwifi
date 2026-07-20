from flask import Flask, render_template, request
from database import conexao, cursor
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():

    if request.method == "POST":

        nome = request.form["nome"]
        cpf = request.form["cpf"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        cep = request.form["cep"]
        rua = request.form["rua"]
        bairro = request.form["bairro"]
        cidade = request.form["cidade"]

        aceite = 1

        data = datetime.now()

        sql = """
        INSERT INTO usuarios
        (Nome, CPF, Email, Telefone, CEP, Rua, Bairro, Cidade, aceite_lgpd, data_cadastro)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        valores = (
            nome,
            cpf,
            email,
            telefone,
            cep,
            rua,
            bairro,
            cidade,
            aceite,
            data
        )

        cursor.execute(sql, valores)

        conexao.commit()

        return render_template("sucesso.html")

    return render_template("index.html")

import os

if __name__ == "_main_":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
