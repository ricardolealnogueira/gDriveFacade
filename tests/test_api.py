

import unittest
import datetime

from gDriveFacade.api.endpoints import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        """
        Prepara servidor web (Flask) para realização de testes
        """
        # Configura o Flask para testes
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False

        # Executa servidor de testes
        self.app = app.test_client()

    def test_gdrive_search(self):
        """
        Testa a API de busca de documentos por termo e id de documento
        """
        # Variáveis para a busca
        file_id = '1RrmV8yFnQ8WxdrtCvHjmEnv9TM6wo-lL75AVImhHLnk'
        word_in_file = 'teste'
        word_not_in_file = 'termo_muito_improvável_de_ocorrer_naturalmente_em_um_doc'

        # Padrão de URL do Endpoint da API para busca no gDrive por termo e id de documento
        gdrive_search_pattern = "/search-in-doc/{file_id}?word={word}"

        # Executa chamada à API que deve retornar 200
        success_url = gdrive_search_pattern.format(file_id=file_id, word=word_in_file)
        response = self.app.get(success_url)
        self.assertEqual(200, response.status_code)

        # Executa chamada à API que deve retornar 404
        failure_url = gdrive_search_pattern.format(file_id=file_id, word=word_not_in_file)
        response = self.app.get(failure_url)
        self.assertEqual(404, response.status_code)

    def test_gdrive_create(self):
        """
        Testa a API de criação de arquivos com título e texto
        """
        # Timestamp do momento pré-criação do arquivo
        now = datetime.datetime.now()

        # Variáveis para o teste
        file_name = f'teste_api_{now}.txt'
        file_data = f'Timestamp: {now}'

        # URL e parâmetros para testar a API de criação de arquivos
        url = '/file'
        parameters = {'titulo': file_name, 'descripcion': file_data}

        # Executa requisição POST para criação de arquivo de testes
        response = self.app.post(url, data=parameters)

        self.assertEqual(200, response.status_code)