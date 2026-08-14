from utils import load_data, load_template, add_note
from static.data.database import carregar_notas, adicionar_notas

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in carregar_notas()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    adicionar_notas(titulo, detalhes)