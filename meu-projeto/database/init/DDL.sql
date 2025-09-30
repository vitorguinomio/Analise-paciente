-- Active: 1759243430723@@127.0.0.1@5432@triagem_db
CREATE TABLE Paciente(
    idusuario SERIAL PRIMARY KEY,
    nome_completo VARCHAR(255),
    cpf CHAR(11) UNIQUE,
    data_nascimento DATE,
    nacionalidade VARCHAR(255),
    sexo CHAR(1) CHECK (sexo IN ('M','F','O')),/* M = masculino, F = feminino, O = outro */
    dthinsert TIMESTAMP DEFAULT NOW(),
    dthdelete TIMESTAMP CHECK(dthdelete >= dthinsert OR dthdelete IS NULL), -- validação do delete lógico, a data de insart não pode ser menor 
    statusdelete BOOLEAN DEFAULT FALSE -- DELETE LÓGICO
);

CREATE TABLE triagem(
    idtriagem SERIAL PRIMARY KEY,
    idpaciente INTEGER,
    data_atendimento TIMESTAMP DEFAULT NOW(),
    temperatura DECIMAL(3,1),
    pressao_arterial CHAR(7),
    saturação_oxigenio INTEGER,
    FOREIGN KEY (idpaciente) REFERENCES paciente(idusuario)
);

CREATE table consulta(
    idconsulta SERIAL PRIMARY KEY,
    idtriagem INTEGER,
    idpaciente INTEGER,
    resultado_llm VARCHAR(255),
    descricação_medica VARCHAR(500),
    dthinsert TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY (idtriagem) REFERENCES triagem(idtriagem),
    FOREIGN KEY (idpaciente) REFERENCES paciente(idusuario)
);
