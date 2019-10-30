"""
Arquivo com as funções para busca em documento e criação de arquivo.
"""

import os
import tempfile

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


def exists_file_with_text_and_id(text, file_id, creds):
    # Constroi interface de acesso à API do gDrive
    service = build('drive', 'v3', credentials=creds)

    # Executa chamada à API do gDrive
    results = service.files().list(
        pageSize=10,
        fields="nextPageToken, files(id, name)",
        q=f"fullText contains '{text}'"
    ).execute()

    # Extrai lista de arquivos do resultado
    files = results.get('files', [])

    # Para cada arquivo encontrados
    for f in files:

        # Retorna True caso o ID do arquivo seja igual ao id passado como parâmetro
        if f['id'] == file_id:
            return True

    # Retorna False, caso o id especificado não esteja dentre os IDs dos arquivos encontrados
    return False


def create_text_file(file_name, file_text, creds):
    """
    Função de criação de arquivos
    """
    # Constroi interface de acesso à API do gDrive
    service = build('drive', 'v3', credentials=creds, cache_discovery=False)

    # Cria um arquivo temporário para realização do upload
    arquivo_temporario = os.path.join(tempfile.gettempdir(), 'temp.txt')

    # Grava o conteúdo no arquivo
    with open(arquivo_temporario, 'w+') as f:
        f.write(file_text)

    # Instancia objeto com os dados do arquivo que será upado
    file_data = MediaFileUpload(arquivo_temporario, mimetype='text/plain')

    # Metadados do arquivo que será criado
    file_metadata = {'name': file_name}

    # Cria arquivo no gDrive
    file = service.files().create(body=file_metadata, media_body=file_data, fields='id').execute()

    return file
