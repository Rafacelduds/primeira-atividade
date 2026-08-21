from flask import Flask, render_template_string, request, redirect
import views
from static.data.createdb import criar_tabelas, atualizar_nota, favoritar_nota


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

@app.route('/delete/<int:id>')
def delete(id):
    if request.method == 'GET':
        views.delete(id)
        return redirect('/')
    else:
        return redirect('/')

@app.route('/update/<int:id>')
def update_page(id):
    if request.method == 'GET':
        return views.update(id)

@app.route('/update/<int:id>/salvar', methods=['POST'])
def update_confirm(id):
    if request.method == 'POST':
        titulo = request.form['titulo']
        detalhes = request.form['detalhes']

        atualizar_nota(id, titulo, detalhes)
        return redirect('/')
    return redirect('/')

@app.route('/favoritar/<int:id>')
def favoritar(id):
    favoritar_nota(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)