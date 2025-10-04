from src.triagem_inteligente.database.connection import get_db_session
from src.triagem_inteligente.database.models import Paciente
from faker import Faker
fake = Faker("pt_BR")
import random


def testar_insercao_paciente():
    """
    Função para fazer inserção automatica no banco de dados
    """

    print("Print Iniciando teste de conexão...")

    db_session_generator = get_db_session()
    db = next (db_session)

    print(">>> Criando um objeto Paciente...")

    try:
        num_insert = int(input("Quanatas pessoas vocês quer inserir no banco de dados"))

        for _ in range(num_insert):
            
            novos_pacientes = Paciente(
                nome_completo= fake.name().upper(),
                cpf = fake.cpf(),
                data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=90),
                sexo = fake.random_element(elements=("M", "F")).upper(),
                nacionalidade = fake.country().upper()
            )

            print(novos_pacientes[0])
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

