from config import Configuration
from app.repositories.expectativas_anuais_repository import ExpectativaAnualRepositorio
from app.services.expectativas_anuais_service import ExpectativaAnualService
from app.preprocessors.expectativas_anuais_preprocessador import ExpectativaAnualProcessor
from app.utils.seguranca import uri_valida

def main():
    
    if not uri_valida(Configuration.MONGO_URI):
        raise ValueError("MONGO_URI inválida!")

    repositorio = ExpectativaAnualRepositorio(Configuration.MONGO_URI, Configuration.MONGO_DB)
    pre_processador = ExpectativaAnualProcessor ()
    servico = ExpectativaAnualService(Configuration.BCB_API_URL, pre_processador)
    expectativas_anuais = servico.obtain_and_preprocessor()
    for registro in expectativas_anuais:
        repositorio.insert(registro)
    print("Dados inseridos com sucesso!")
    
if __name__ == "__main__":
    main()