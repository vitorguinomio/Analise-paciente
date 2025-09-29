import datetime
from sqlalchemy import (Column, Integer, String, Date, DateTime, Enum, 
                        DECIMAL, ForeignKey, CheckConstraint)
from sqlalchemy.orm import declarative_base

base = declarative_base

class Paciente(base):
    __tablename__ = "pacientes"


    idpaciente = Column(Integer, primary_key=True)
    nome_completo = Column(String(255), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True, index=True)
    data_nascimento = Column(Date, nullable=False)
    sexo = Column(Enum('M', 'F', name='sexo_enum'), nullable=False)
    nacionalidade = Column(String(100))
    dthinsert = Column(DateTime, default=datetime.datetime.now, nullable=False)
    dthdelete = Column(DateTime, nullable=True)

    __table_args__ = (
        CheckConstraint('dthdelete IS NULL OR dthdelete >= dthinsert', name='check_dthdelete'),
    )


class Triagem(base):
    idtriagem = Column(Integer, primary_key=True)
    idpaciente = Column(Integer, ForeignKey("Paciente.idpaciente"), nullable=False)
    data_atendimento = Column(DateTime, default=datetime.datetime.now, nullable=False, index=True)
    temperatura = Column(Decimal(3,1), nullable=False)
    pressão_arterial = Column(String(7))
    saturação_oxigenio = Column(Integer)
    queixa_principal = (Column(String(500)))

class Consulta(base):
    __tablename__ = "consultas"

    idconculsta = Column(Integer, primary_key=True)
    idtriagem = Column(Integer, ForeignKey("Triagem.idtriagem"))
    resultado_llm = Column(String(255))
    descrição_medica = Column(String(500))
    dthinsert = Column(DateTime, default.datetime.datetime.now, nullable=False)

