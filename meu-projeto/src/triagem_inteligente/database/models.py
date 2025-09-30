import datetime
from sqlalchemy import (Column, Integer, String, Date, DateTime, Enum,
                        DECIMAL, ForeignKey, CheckConstraint)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Paciente(Base): 
    __tablename__ = "paciente"

    idusuario = Column(Integer, primary_key=True)
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

class Triagem(Base):
    __tablename__ = "triagen"

    idtriagem = Column(Integer, primary_key=True)
    idpaciente = Column(Integer, ForeignKey("pacientes.idpaciente"), nullable=False, index=True)
    data_atendimento = Column(DateTime, default=datetime.datetime.now, nullable=False)
    temperatura = Column(DECIMAL(3, 1), nullable=False)
    pressao_arterial = Column(String(7))
    saturacao_oxigenio = Column(Integer)
    queixa_principal = Column(String(500))

class Consulta(Base):
    __tablename__ = "consulta"
    idtriagem = Column(Integer, ForeignKey("triagens.idtriagem"), primary_key=True)
    resultado_llm = Column(String(255))
    descricao_medica = Column(String(500))
    dthinsert = Column(DateTime, default=datetime.datetime.now, nullable=False)