import os
from dotenv import load_dotenv

load_dotenv()

# Configuração do banco de dados para fazer conexão
DB_CONFIG = {
    'dbname':   os.getenv('POSTGRES_DB'),
    'user':     os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'host':     os.getenv('DB_HOST'),
    'port':     os.getenv('DB_PORT')
}

# --- BLOCO DE VALIDAÇÃO ---
# Verifica se alguma das variáveis essenciais veio como None (não encontrada)
required_vars = ['dbname', 'user', 'password', 'host', 'port']
missing_vars = [key for key, value in DB_CONFIG.items() if value is None and key in required_vars]

if missing_vars:
    # Se alguma variável estiver faltando, para a execução com um erro claro
    raise ValueError(f"Erro: As seguintes variáveis de ambiente não foram definidas: {', '.join(missing_vars)}. "
                    "Verifique seu arquivo .env e a seção 'environment' no docker-compose.yml.")

# A variável deve se chamar DATABASE_URL para ser consistente com connection.py
DATABASE_URL = (
    f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
)

print(f"DEBUG: Conectando com a URL: postgresql+psycopg2://{DB_CONFIG['user']}:****@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}")


NLP_CONFIG = {
    'CLASSIFICATION_MODEL_NAME': "distilbert-base-uncased-finetuned-sst-2-english"
}