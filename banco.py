import oracledb

def get_conexao():
    return oracledb.connect(user="rm560485", password="fiap25", dsn="oracle.fiap.com.br/orcl")

def ler_banco():
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute("SELECT * from jogos order by id_jogo")
            captura = cur.fetchall()
    
    lista_jogos = []

    for jogos in captura:
        id_jogo = jogos[0]
        nome_jogo = jogos[1]
        desenvolvedora_jogo = jogos[2]
        ano_jogo = jogos[3]
        lista_jogos.append({"id": id_jogo, "nome": nome_jogo, "desenvolvedora": desenvolvedora_jogo, "ano": ano_jogo})
    
    print(lista_jogos)

    return lista_jogos

ler_banco()