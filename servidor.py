from flask import Flask, render_template_string, request, redirect
import views
from static.data.createdb import criar_tabelas


app = Flask(__name__)

criar_tabelas()

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        titulo = request.form['titulo']
        detalhes = request.form['detalhes']

        views.submit(titulo, detalhes)
        return redirect('/')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)