"""
Arquivo de teste da API gDrive
"""


import os
import unittest
import datetime

from gDriveFacade.googleAPI.auth import acquire_google_oauth_token
from gDriveFacade.googleAPI.gdrive import create_text_file, exists_file_with_text_and_id
from gDriveFacade.config import SCOPES, CREDENTIALS_FILE, TEST_TOKEN_FILE


class TestGoogleAPI(unittest.TestCase):


    def test_token_acquisition(self):
        """
        Testa a aquisição de token de acesso à API do gDrive. Ao rodar este teste, o navegador
        é aberto automaticamente para que o usuário escolha sua conta do Google. A execução fica
        bloqueado aguardando a açao do usuário.
        """
        # Remove arquivo de token, caso exista
        if os.path.exists(TEST_TOKEN_FILE):
            os.remove(TEST_TOKEN_FILE)

        # Obtém credenciais
        creds = acquire_google_oauth_token(SCOPES, CREDENTIALS_FILE, TEST_TOKEN_FILE)

        # Verifica se as credenciais foram obtidas com sucesso
        self.assertIsNotNone(creds)

        # Verifica se o arquivo com as credenciais foi salvo corretamente
        self.assertTrue(os.path.exists(TEST_TOKEN_FILE))

    def test_gdrive_search(self):
        """
        Testa a busca em documento
        """
        # Variáveis para execução do teste de busca
        test_file_id = '1RrmV8yFnQ8WxdrtCvHjmEnv9TM6wo-lL75AVImhHLnk'
        word_in_file = 'teste'
        word_not_in_file = 'termo_muito_improvável_de_ocorrer_naturalmente_em_um_doc'

        # Obtém credenciais
        creds = acquire_google_oauth_token(SCOPES, CREDENTIALS_FILE, TEST_TOKEN_FILE)

        # Realiza busca em documento que sabidamente contém o texto
        search_result = exists_file_with_text_and_id(word_in_file, test_file_id, creds)
        self.assertTrue(search_result)

        # Realiza busca em documento que sabidamente não contém o texto
        search_result = exists_file_with_text_and_id(word_not_in_file, test_file_id, creds)
        self.assertFalse(search_result)

    def test_gdrive_create(self):
        """
        Testa a criação de arquivo
        """
        # Timestamp do momento pré-criação do arquivo
        now = datetime.datetime.now()

        # Variáveis para o teste
        file_name = f'teste_api_google_{now}.txt'
        file_data = f'Timestamp: {now}'

        # Obtém credenciais
        creds = acquire_google_oauth_token(SCOPES, CREDENTIALS_FILE, TEST_TOKEN_FILE)

        # Cria arquivo de testes
        result = create_text_file(file_name, file_data, creds)

        self.assertIsNotNone(result.get('id'))

