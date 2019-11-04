# Python 3.6.7
FROM python:3.6.7-alpine3.6
# Pacotes necessários 
COPY requirement.txt /
# rodar instruções durante construção da imagem
RUN pip install -r requirement.txt
# Copia os arquivos para o diretório do Docker
COPY . /
ENTRYPOINT ["python"]
CMD ["gDriveFacade/start.py"]
