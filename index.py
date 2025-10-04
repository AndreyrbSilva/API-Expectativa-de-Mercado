from config import Configuration

from app.repositories.expectativas_anual_repository import ExpectativaAnualRepositorio
from app.services.expectativas_anual_service import ExpectativaAnualService
from app.preprocessors.expectativas_anual_preprocessor import ExpectativaAnualProcessor

from app.repositories.expectativas_selic_repository import ExpectativasSelicRepository
from app.services.expectativas_selic_service import ExpectativasSelicService
from app.preprocessors.expectativas_selic_preprocessor import ExpectativasSelicProcessor

from app.repositories.expectativas_trimestral_repository import ExpectativasTrimestralRepository
from app.services.expectativas_trimestral_service import ExpectativasTrimestralService
from app.preprocessors.expectativas_trimestral_preprocessor import ExpectativasTrimestralProcessor

from app.repositories.expectativas_mensal_repository import ExpectativasMensalRepository
from app.services.expectativas_mensal_service import ExpectativasMensalService
from app.preprocessors.expectativas_mensal_preprocessor import ExpectativasMensalProcessor

from app.utils.seguranca import uri_valida

def main():
    
    if not uri_valida(Configuration.MONGO_URI):
        raise ValueError("MONGO_URI inválida!")

    repositorio_anual = ExpectativaAnualRepositorio(Configuration.MONGO_URI, Configuration.MONGO_DB)
    pre_processador_anual = ExpectativaAnualProcessor()
    servico_anual = ExpectativaAnualService(Configuration.BCB_API_ANUAL, pre_processador_anual)

    expectativas_anuais = servico_anual.obtain_and_preprocessor()
    for registro in expectativas_anuais:
        repositorio_anual.insert(registro)
    print("Dados Anuais inseridos com sucesso!")

    repositorio_selic = ExpectativasSelicRepository(Configuration.MONGO_URI, Configuration.MONGO_DB)
    pre_processador_selic = ExpectativasSelicProcessor()
    servico_selic = ExpectativasSelicService(Configuration.BCB_API_SELIC, pre_processador_selic)

    expectativas_selic = servico_selic.obtain_and_preprocessor()
    for registro in expectativas_selic:
        repositorio_selic.insert(registro)
    print("Dados Selic inseridos com sucesso!")

    repositorio_trimestral = ExpectativasTrimestralRepository(Configuration.MONGO_URI, Configuration.MONGO_DB)
    pre_processador_trimestral = ExpectativasTrimestralProcessor()
    servico_trimestral = ExpectativasTrimestralService(Configuration.BCB_API_TRIMESTRAL, pre_processador_trimestral)

    expectativas_trimestrais = servico_trimestral.obtain_and_preprocessor()
    for registro in expectativas_trimestrais:
        repositorio_trimestral.insert(registro)
    print("Dados Trimestrais inseridos com sucesso!")

    repositorio_mensal = ExpectativasMensalRepository(Configuration.MONGO_URI, Configuration.MONGO_DB)
    pre_processador_mensal = ExpectativasMensalProcessor()
    servico_mensal = ExpectativasMensalService(Configuration.BCB_API_MENSAL, pre_processador_mensal)

    expectativas_mensais = servico_mensal.obtain_and_preprocessor()
    for registro in expectativas_mensais:
        repositorio_mensal.insert(registro)
    print("Dados Mensais inseridos com sucesso!")


if __name__ == "__main__":
    main()