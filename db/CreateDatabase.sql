CREATE DATABASE IF NOT EXISTS
    dbpessoa;
USE dbpessoa;

CREATE TABLE pessoa (
    id_pessoa INTEGER NOT NULL auto_increment,
    nome_pessoa VARCHAR(50),
    data_nascimento DATE,
    PRIMARY KEY (id_pessoa)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO pessoa (nome_pessoa, data_nascimento) VALUES ('Neto', '2002-10-29');