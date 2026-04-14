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
    dtlancamento = (request.form["dtlancamento"])

    novo_filme = Filme(nome,sinopse,elenco,dtlancamento)
    filmes.append(novo_filme)

    return redirect("/")

@app.route("/remover/<int:id>")
def remover_filme(id):
    global filmes
    filmes = [filme for filme in filmes if filme.id != id]
    return redirect("/")

@app.route("/editar/<int:id>")
def editar_filme(id):
    filme = next((filme for filme in filmes if filme.id == id), None)
    if filme:
        return render_template("editar.html",filme=filme)
    return redirect("/")

@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar_filme(id):
    filme = next((filme for filme in filmes if filme.id == id), None)
    if filme:
        filme.nome = request.form["nome"]
        filme.sinopse = request.form["sinopse"]
        filme.elenco = request.form["elenco"]
        filme.dtlancamento = request.form ["dtlancamento"]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host="191.36.57.66")
