import os
from dotenv import load_dotenv

load_dotenv()

#Configuração do banco de dados para fazer conexão 
DB_CONFIG = {
    'dbname':   os.getenv('POSTGRES_DB'),
    'user':     os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'host':     os.getenv('DB_HOST', 'localhost'),  # Corrigido para não ser fixo
    'port':     os.getenv('DB_PORT', '5432')       # A chave 'port' é mais padrão
}


DB_URL = (
    f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
)

NLP_CONFIG = {
    'CLASSIFICATION_MODEL_NAME': "distilbert-base-uncased-finetuned-sst-2-english"
}