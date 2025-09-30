# scripts/test_connection.py
import sys
import os
import datetime

# --- Bloco de Configuração do Path ---
# Adiciona o diretório raiz do projeto ao path do Python
# Isso é crucial para que o script encontre os módulos em 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ---------------------------------------

# Agora podemos importar os módulos da aplicação
from src.triagem_inteligente.database.connection import get_db_session
from src.triagem_inteligente.database.models import Paciente

def testar_insercao_paciente():
    """
    Função para testar a conexão e a inserção de um único paciente no banco.
    """
    print(">>> Iniciando teste de conexão e inserção...")
    
    # Pede uma nova sessão para a nossa função utilitária
    db_session_generator = get_db_session()
    db = next(db_session_generator)

    print(">>> Sessão com o banco de dados obtida.")

    try:
        print(">>> Criando um novo objeto Paciente...")
        
        # 1. Você cria um objeto Python normal, da classe Paciente
        novo_paciente = Paciente(
            nome_completo="Paciente Teste SQLAlchemy",
            cpf="99988877766",
            data_nascimento=datetime.date(1985, 10, 2),
            sexo='M',
            nacionalidade='Brasileira'
        )

        # 2. Você adiciona o objeto à sessão (área de trabalho)
        db.add(novo_paciente)

        # 3. Você "comita" a transação. O SQLAlchemy gera o INSERT e envia ao banco.
        db.commit()

        # 4. (Opcional) Atualiza seu objeto com os dados que o banco gerou (como o ID)
        db.refresh(novo_paciente)

        print("-" * 50)
        print(">>> SUCESSO! Paciente inserido no banco de dados.")
        print(f">>> ID Gerado: {novo_paciente.idusuario}")
        print(f">>> Nome: {novo_paciente.nome_completo}")
        print("-" * 50)

    except Exception as e:
        print(f">>> FALHA! Ocorreu um erro: {e}")
        db.rollback() # Reverte a transação em caso de erro
    finally:
        print(">>> Fechando a sessão com o banco de dados.")
        db.close()

# --- Bloco de Execução Principal ---
# Garante que a função só será executada quando o script for chamado diretamente
if __name__ == "__main__":
    testar_insercao_paciente()