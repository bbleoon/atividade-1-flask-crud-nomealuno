#import datetime.date
from flask import Flask, jsonify,request, render_template, redirect
from filme import Filme

app = Flask(__name__)

filmes = []

@app.route("/", methods=["GET"])
def pagina_inicial():
    return render_template("index.html", filmes = filmes)

@app.route("/filme", methods=["GET"])
def listar_filmes():
    return jsonify([filme.to_dict() for filme in filmes])

@app.route("/cadastro", methods=["POST"])
def adicionar_filme():
    nome = request.form["nome"]
    sinopse = request.form["sinopse"]
    elenco = request.form["elenco"]
    #dtlancamento = date(request.form["dtlancamento"])
    dtlancamento = (request.form["dtlancamento"])

    novo_filme = Filme(nome,sinopse,elenco,dtlancamento)
    filmes.append(novo_filme)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
