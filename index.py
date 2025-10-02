from config import Configuration
from app.repositories.expectativas_selic_repository import ExpectativasSelicRepository
from app.services.expectativas_selic_service import ExpectativasSelicService
from app.preprocessors.expectativas_selic_preprocessor import ExpectativasSelicProcessor
from app.utils.seguranca import uri_valida

def main():
    # Validação da URI do banco
    if not uri_valida(Configuration.MONGO_URI):
        raise ValueError("MONGO_URI inválida!")

    repositorio = ExpectativasSelicRepository(Configuration.MONGO_URI, Configuration.MONGO_DB)
    pre_processador = ExpectativasSelicProcessor()
    servico = ExpectativasSelicService(Configuration.BCB_API_URL, pre_processador)
    expectativas_selic = servico.obtain_and_preprocessor()
    for registro in expectativas_selic:
        repositorio.insert(registro)
    print("Dados inseridos com sucesso!")   

if __name__ == "__main__":
    main()