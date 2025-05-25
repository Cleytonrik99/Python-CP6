# Sobre o projeto
#  Sua tarefa é desenvolver uma API usando python que representa um CRU de um recurso.
#  Faz parte do trabalho o grupo definir o recurso que será implementado. Alguns recursos
#  não podem ser implementados: veículo, pergunta, pessoa, produto, endereço e mensagem.
#  Procure algum outro tipo de elemento/recurso para fazer a implementação.


# Requisitos
#  • o recurso precisa ter no mínimo 4 campos
#  • o campo id é um campo obrigatório e deve ser definido pelo banco de dados
#  • pelo menos um campo do tipo String
#  • pelo menos um campo do tipo numérico
#  • pelo menos duas funções de consulta 
#     -recupera um recurso pelo id 
#     –recupera um conjunto de recursos através de um parâmetro que você deve definir


# Cleyton Enrike de Oliveira  
#   RM: 560485


from flask import Flask, jsonify, request
from banco import *

app = Flask("API de jogos")

@app.route("/jogos", methods=["GET"])
def get_jogos():
    jogos = ler_banco()

    return (jsonify(jogos), 200)



@app.route("/jogos/<int:id>", methods=["GET"])
def get_jogo_by_id(id:int):
    jogos = ler_banco()

    for jogo in jogos:
        if jogo["id"] == id:
            return (jsonify(jogo), 200)
    
    info = {
        "msg": f"Nenhum jogo com id={id} encontrado",
        "status": 404
    }
    return (jsonify(info), 404)



@app.route("/jogos/ano/<int:ano>", methods=["GET"])
def get_jogo_by_ano(ano:int):
    jogos = ler_banco()

    lista = []

    for jogo in jogos:
        if jogo["ano"] == ano:
            lista.append(jogo)
    
    if len(lista) > 0:
        return (jsonify(lista), 200)
    else:
        info = {"msg": "Nenhum jogo encontrado", "status": 404}
        return (jsonify(info), 404)



@app.route("/jogos", methods=["POST"])
def inserir_jogo():
    jogos = ler_banco()

    insercao = request.get_json()

    if not insercao.get("nome") or not insercao.get("ano") or not insercao.get("desenvolvedora"):
        info = {"msg": "Não foi encontrada uma das informações necessárias (é necessário, nome, ano e desenvolvedora)", "status": 406}
        return (info, 406)
    
    for i in jogos:
        if i["nome"] == insercao["nome"]:
            info = {"msg": "Já existe um jogo com o mesmo nome", 
                    "status": 406}
            return (info, 406)

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(
                "INSERT INTO jogos (nome_jogo, desenvolvedora, ano) VALUES (:1, :2, :3)",
                (insercao["nome"], insercao["desenvolvedora"], insercao["ano"])
            )
            con.commit()
    
    info = {"msg": "Jogo recebido", "status": 201}
    return jsonify(info), 201



@app.route("/jogos/<int:id>", methods=["PATCH"])
def atualizar_jogo(id:int):
    jogos = ler_banco()

    insercao = request.get_json()

    if not insercao.get("nome") or not insercao.get("ano") or not insercao.get("desenvolvedora"):
        info = {"msg": "Não foi encontrada uma das informações necessárias (é necessário, nome, ano e desenvolvedora), não foi possível atualizar as informações", "status": 406}
        return (info, 406)

    for jogo in jogos:
        if jogo["id"] == id:
            with get_conexao() as con:
                with con.cursor() as cur:
                    cur.execute(
                        "UPDATE jogos SET nome_jogo = :1, desenvolvedora = :2, ano = :3 WHERE id_jogo = :4",
                        (insercao["nome"], insercao["desenvolvedora"], insercao["ano"], id)
                    )
                    con.commit()
            info = {"msg": "Jogo atualizado", "status": 200}
            return (jsonify(info), 200)

    info = {"msg": f"Nenhum jogo com id={id} encontrado", "status": 404}
    return (jsonify(info), 404)



app.run(debug=True)