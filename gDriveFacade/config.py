"""
Arquivo de configuração contendo requisitos para utilização da API
"""

import os

# Escopo requerido pela aplicação
SCOPES = ['https://www.googleapis.com/auth/drive']

# Diretório raiz do projeto
ROOT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.path.pardir)

# Arquivo JSON com as credenciais de acesso à API do Google Drive
CREDENTIALS_FILE = os.path.join(ROOT_DIR, 'etc', 'credentials.json')

# Arquivo com o token obtido pelo OAuth será armazenado
TOKEN_FILE = os.path.join(ROOT_DIR, 'etc', 'token.pickle')

# Arquivo onde o token obtido pelo OAuth será armazenado
TEST_TOKEN_FILE = os.path.join(ROOT_DIR, 'etc', 'test.token.pickle')

# Porta utilizada pela API
PORTA_API = 8080