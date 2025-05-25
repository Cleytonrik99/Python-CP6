CREATE TABLE JOGOS (
    id_jogo NUMBER(11) GENERATED AS IDENTITY PRIMARY KEY,
    nome_jogo VARCHAR2(100) NOT NULL,
    desenvolvedora VARCHAR2(100) NOT NULL,
    ano NUMBER(4) NOT NULL
);

INSERT INTO JOGOS (nome_jogo, desenvolvedora, ano) VALUES ('Sifu', 'Sloclap', 2023);
INSERT INTO JOGOS (nome_jogo, desenvolvedora, ano) VALUES ('Resident Evil 4 Remake', 'Capcom', 2023);
INSERT INTO JOGOS (nome_jogo, desenvolvedora, ano) VALUES ('Resident Evil 7', 'Capcom', 2017);
INSERT INTO JOGOS (nome_jogo, desenvolvedora, ano) VALUES ('Hollow Knight', 'Team Cherry', 2017);
INSERT INTO JOGOS (nome_jogo, desenvolvedora, ano) VALUES ('Katana Zero', 'Askiisoft', 2019);
INSERT INTO JOGOS (nome_jogo, desenvolvedora, ano) VALUES ('Blasphemous', 'The Game Kitchen', 2019);
INSERT INTO JOGOS (nome_jogo, desenvolvedora, ano) VALUES ('Buckshot Roulette', 'Mike Klubnika', 2024);
INSERT INTO JOGOS (nome_jogo, desenvolvedora, ano) VALUES ('Senuas Saga: Hellblade II', 'Ninja Theory', 2024);
INSERT INTO JOGOS (nome_jogo, desenvolvedora, ano) VALUES ('Enigma do Medo', 'Dumativa', 2025);
INSERT INTO JOGOS (nome_jogo, desenvolvedora, ano) VALUES ('Blue Prince', 'Dogubomb', 2025);
INSERT INTO JOGOS (nome_jogo, desenvolvedora, ano) VALUES ('DOOM: The Dark Ages', 'id Software', 2025);

COMMIT;