"""
Processamento das requisições GET e POST
"""

from flask import Flask, request, jsonify

from gDriveFacade.googleAPI.auth import acquire_google_oauth_token
from gDriveFacade.googleAPI.gdrive import exists_file_with_text_and_id, create_text_file
from gDriveFacade.config import SCOPES, CREDENTIALS_FILE, TOKEN_FILE

app = Flask(__name__)

# Número máximo de caracteres permitido pelo gDrive em nomes de arquivos
MAX_GDRIVE_FILE_NAME_SIZE = 32767

@app.route('/search-in-doc/<string:id>')
def gdrive_search(id):
    """
    Processa URL no formato GET /search-in-doc/<string:id>?word=termo_de_busca
    """
    try:
        # Obtém valor do parâmetro word passado na URL
        word = request.args.get('word')

        # Obtém credenciais
        creds = acquire_google_oauth_token(SCOPES, CREDENTIALS_FILE, TOKEN_FILE)

        # Realiza busca no documento
        search_result = exists_file_with_text_and_id(word, id, creds)

        # Retorna código de status de acordo com o resultado da busca
        if search_result:
            return '', 200
        else:
            return '', 404

    # Caso ocorra qualquer erro no processamento da requisição
    except Exception as e:

        # Retorna código de status 500 ("No caso de não poder cria-lo ")
        return '', 500

@app.route('/file', methods=['POST'])
def gdrive_create_text_file():
    """
    Processa requisição POST
    """
    # Obtém valor dos parâmetros passados na requisição POST
    file_name = request.form['titulo']
    file_text = request.form['descripcion']

    # Retorna código 404 caso os parâmetros tenham sido informados de forma inadequada
    if len(file_name) > MAX_GDRIVE_FILE_NAME_SIZE:
        return '', 404

    # Obtém credenciais
    creds = acquire_google_oauth_token(SCOPES, CREDENTIALS_FILE, TOKEN_FILE)

    # Cria arquivo com os parâmetros especificados
    file = create_text_file(file_name, file_text, creds)

    # Prepara resposta em formato JSON
    response = jsonify({'id': file.get('id'), 'titulo':file_name, 'descripcion':file_text})

    return response