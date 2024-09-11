from flask import Flask, render_template, request, redirect, url_for
from utils.cloud_utils import upload_file
from utils.iot_utils import connect_mqtt

app = Flask(__name__)

# Dados fictícios para eventos
eventos = [
    {'nome': 'Culto de Louvor', 'data': '10/09/2024', 'descricao': 'Culto especial de louvor e adoração.'},
    {'nome': 'Reunião de Oração', 'data': '15/09/2024', 'descricao': 'Reunião semanal de oração.'}
]

@app.route('/')
def index():
    return render_template('index.html', eventos=eventos)

@app.route('/add_event', methods=['POST'])
def add_event():
    nome = request.form['nome']
    data = request.form['data']
    descricao = request.form['descricao']
    
    # Adicionar evento à lista (ou banco de dados)
    eventos.append({
        'nome': nome,
        'data': data,
        'descricao': descricao
    })
    
    return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload_file_view():
    file = request.files['file']
    if file:
        upload_file(file, file.filename)
        return redirect(url_for('index'))
    return "Falha no upload"

if __name__ == '__main__':
    app.run(debug=True)
