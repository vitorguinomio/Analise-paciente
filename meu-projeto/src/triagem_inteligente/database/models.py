import datetime
from sqlalchemy import (Column, Integer, String, Date, DateTime, Enum, 
                        DECIMAL, ForeignKey, CheckConstraint)
from sqlalchemy.orm import declarative_base

base = declarative_base

class Paciente(Base):
    __tablename__ = "pacientes"

    # --- Colunas ---
    idpaciente = Column(Integer, primary_key=True)
    nome_completo = Column(String(255), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True, index=True)
    data_nascimento = Column(Date, nullable=False)
    sexo = Column(Enum('M', 'F', name='sexo_enum'), nullable=False)
    nacionalidade = Column(String(100))

    # --- Colunas de Auditoria e Soft Delete ---
    # Soft Delete: Em vez de apagar, marcamos como deletado.
    dthinsert = Column(DateTime, default=datetime.datetime.now, nullable=False)
    dthdelete = Column(DateTime, nullable=True) # Se for NULL, está ativo. Se tiver data, foi "deletado".

    # --- Regras da Tabela ---
    __table_args__ = (
        CheckConstraint('dthdelete IS NULL OR dthdelete >= dthinsert', name='check_dthdelete'),
    )