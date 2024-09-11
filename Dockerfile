# Usa uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY requirements.txt .
COPY app.py .
COPY static/ static/
COPY templates/ templates/
COPY config/ config/
COPY utils/ utils/
COPY scripts/ scripts/

# Instala as dependências
RUN pip install -r requirements.txt

# Define o comando padrão para executar o aplicativo
CMD ["python", "app.py"]
