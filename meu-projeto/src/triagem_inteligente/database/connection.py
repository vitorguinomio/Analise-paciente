from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .. import config

# 1. O Motor: criado uma vez para toda a aplicação
engine = create_engine(config.DATABASE_URL)

# 2. A Fábrica de Sessões: usada para criar novas sessões sob demanda
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. A Função Utilitária (a que estava faltando)
def get_db_session():
    """
    Esta função é um gerador que fornece uma sessão de banco de dados
    e garante que ela seja sempre fechada no final.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()