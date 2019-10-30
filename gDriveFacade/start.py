"""
Executar este arquivo para utilizar a API
"""

import os


import sys
sys.path.append('./')

import webbrowser

from gDriveFacade.api.endpoints import app
from gDriveFacade.config import PORTA_API, ROOT_DIR

if __name__ == '__main__':

    # Abre navegador e redireciona para página HTML para permitir que o usuário utilize a API
    url = os.path.join(ROOT_DIR, 'web', 'index.html')
    webbrowser.open(url, new=2)  # open in new tab

    # Executa servidor Flask na porta indicada no arquivo config.py
    app.run(port=PORTA_API)

