import json

def load_data(notes):
    with open(f'static/data/{notes}', 'r') as file:
        return json.load(file)

def load_template(template):
    with open(f'static/templates/{template}', 'r') as file:
        return file.read()

def add_note(note, filename):
    notes = load_data(f'{filename}')
    notes.append(note)

    with open(f'static/data/{filename}', 'w') as file:
        json.dump(notes, file)