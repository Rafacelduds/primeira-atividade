from utils import load_data, load_template, add_note
from static.data.createdb import carregar_notas, adicionar_notas, deletar_notas, carregar_nota, atualizar_nota

def index():
    note_template = load_template('components/notes.html')
    notes_li = [
        note_template.format(id=dados['id'], title=dados['titulo'], content=dados['detalhes'])
        for dados in carregar_notas()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def update(id):
    note_template = load_template('update.html')
    dado = carregar_nota(id)

    return load_template('update.html').format(id=dado['id'], title=dado['titulo'], content=dado['detalhes'])

def submit(titulo, detalhes):
    adicionar_notas(titulo, detalhes)

def delete(id):
    deletar_notas(id)