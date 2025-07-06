from flask import Flask, request, redirect, render_template
from database import session
from models import Agendamento
from datetime import datetime

app = Flask(__name__)
# ROTAS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agendamento')
def agendamento_page():
    return render_template('agendamento.html')

@app.route('/concluido')
def concluido():
    agendamento_id = request.args.get('id')
    return render_template('agendamento-concluido.html', agendamento_id=agendamento_id)


@app.route('/revisar/<int:agendamento_id>')
def revisar(agendamento_id):
    agendamento = session.query(Agendamento).filter_by(id=agendamento_id).first()
    if not agendamento:
        return "Agendamento não encontrado", 404
    return render_template('revisar.html', agendamento=agendamento)


@app.route('/agendar', methods=['GET', 'POST'])
def agendar():
    if request.method == 'POST':
        nome = request.form['nome']
        data = datetime.strptime(request.form['data'], "%Y-%m-%d").date()
        horario = request.form['horario']
        unidade = request.form['unidade']

        agendamento = Agendamento(
            nome=nome,
            data=data,
            horario=horario,
            unidade=unidade
        )
        session.add(agendamento)
        session.commit()

        # Salva o ID em sessão ou query string
        return redirect(f'/concluido?id={agendamento.id}')  # <-- Alteração AQUI
    return render_template('agendamento.html')


if __name__ == '__main__':
    app.run(debug=True)
