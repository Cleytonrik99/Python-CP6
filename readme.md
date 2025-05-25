*TABELA DE ENDPOINTS*

| Método   | Endpoint                                                             | Descrição                                               |
|----------|----------------------------------------------------------------------|---------------------------------------------------------|
| GET      | http://localhost:8080/jogos                                          | Retorna todos os jogos no banco de dados                |
| GET      | http://localhost:8080/jogos/<int:id>                                 | Retorna o jogo com ID correspondente                    |
| GET      | http://localhost:8080/jogos/ano/<int:ano>                            | Retorna todos os jogos com o ano correspondente         |
| POST     | http://localhost:8080/jogos                                          | Insere um novo jogo no banco de dados                   |
| PATCH    | http://localhost:8080/jogos/<int:id>                                 | Atualiza as informações do jogo com o id correspondente |


**EXEMPLO DE JSON PARA POST E PATCH**

{
    "ano": [Ano do Jogo],
    "desenvolvedora": "[Desenvolvedora do Jogo]",
    "nome": "[Nome do Jogo]"
}