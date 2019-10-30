# -*- coding: utf-8 -*-
"""
Arquivo para autenticação do usuário e permissão de acesso aos serviços Google
"""

import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def acquire_google_oauth_token(scopes, credentials_file, token_file):
    """
    Retorna token de acesso OAuth aos serviços do Google. Caso o arquivo
    token_file não exista, o navegador é aberto para que o usuário selecione
    sua conta e conceda a permissão de acesso. O token é criado e armazenado
    para uso futuro.
    """

    # Inicializa variável que será usada para armazenar o token de acesso
    creds = None

    # Verifica se o token de acesso existe
    if os.path.exists(token_file):
        # Carrega o toek de acesso a partir do arquivo
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)

    # Caso o token de acesso não exista ou exista mas seja inválido
    if not creds or not creds.valid:

        # Caso o token exista mas esteja expirado (e seja "atualizável")
        if creds and creds.expired and creds.refresh_token:

            # Atualiza o token de acesso
            creds.refresh(Request())

        else:

            # Instancia processo de autenticação utilizando OAuth
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, scopes)

            # Executa servidor web local e redireciona o usuário para tela de autenticação do OAuth
            creds = flow.run_local_server(port=0)

        # Salva o token de acesso para uso futuro
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)

    return creds
