from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<type>')
def fr(type):
    if type == 'normal':
        double = []
        normal = ['Normal', 'Fire', 'Water', 'Grass', 'Electric',
                  'Ice', 'Fighting', 'Poison', 'Ground', 'Flying',
                  'Psychic', 'Bug', 'Dragon', 'Dark', 'Fairy']
        half = ['Rock', 'Steel']
        ineffective = ['Ghost']
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'fire':
        double = ['Grass', 'Ice', 'Bug', 'Steel']
        normal = ['Normal', 'Electric', 'Fighting', 'Poison', 'Ground',
                  'Flying', 'Psychic', 'Ghost', 'Dark', 'Fairy']
        half = ['Fire', 'Water', 'Rock', 'Dragon']
        ineffective = []
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'water':
        double = ['Fire', 'Ground', 'Rock']
        normal = ['Normal', 'Electric', 'Fighting', 'Poison', 'Flying',
                  'Psychic', 'Ghost', 'Dark', 'Fairy',
                  'Ice', 'Bug', 'Steel']
        half = ['Water', 'Grass', 'Dragon']
        ineffective = []
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'electric':
        double = ['Water', 'Flying']
        normal = ['Fire', 'Rock', 'Normal', 'Fighting', 'Poison',
                  'Psychic', 'Ghost', 'Dark', 'Fairy', 'Ice',
                  'Bug', 'Steel']
        half = ['Electric', 'Grass', 'Dragon']
        ineffective = ['Ground']
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'grass':
        double = ['Water', 'Ground', 'Rock']
        normal = ['Normal', 'Electric', 'Ice', 'Fighting',
                  'Psychic', 'Ghost', 'Dark', 'Fairy']
        half = ['Fire', 'Grass', 'Poison', 'Flying',
                'Bug', 'Dragon', 'Steel']
        ineffective = []
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'ice':
        double = ['Grass', 'Ground', 'Flying', 'Dragon']
        normal = ['Normal', 'Electric', 'Fighting', 'Poison',
                  'Psychic', 'Bug', 'Rock', 'Ghost',
                  'Dark', 'Fairy']
        half = ['Fire', 'Water', 'Ice', 'Steel']
        ineffective = []
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'fighting':
        double = ['Normal', 'Ice', 'Rock', 'Dark', 'Steel']
        normal = ['Fire', 'Water', 'Electric', 'Grass',
                  'Fighting', 'Ground', 'Dragon']
        half = ['Poison', 'Flying', 'Psychic', 'Bug', 'Fairy']
        ineffective = ['Ghost']
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'poison':
        double = ['Grass', 'Fairy']
        normal = ['Normal', 'Fire', 'Water', 'Electric', 'Ice',
                  'Fighting', 'Flying', 'Psychic', 'Bug', 'Dragon', 'Dark']
        half = ['Poison', 'Ground', 'Rock', 'Ghost']
        ineffective = ['Steel']
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'ground':
        double = ['Fire', 'Electric', 'Poison', 'Rock', 'Steel']
        normal = ['Normal', 'Water', 'Ice', 'Fighting', 'Ground',
                  'Psychic', 'Ghost', 'Dragon', 'Dark', 'Fairy']
        half = ['Grass', 'Bug']
        ineffective = ['Flying']
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'flying':
        double = ['Grass', 'Fighting', 'Bug']
        normal = ['Normal', 'Fire', 'Water', 'Ice', 'Poison',
                  'Ground', 'Flying', 'Psychic', 'Ghost', 'Dragon',
                  'Dark', 'Fairy']
        half = ['Electric', 'Rock', 'Steel']
        ineffective = []
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'psychic':
        double = ['Fighting', 'Poison']
        normal = ['Normal', 'Fire', 'Water', 'Electric', 'Grass',
                  'Ice', 'Ground', 'Flying', 'Bug', 'Rock',
                  'Ghost', 'Dragon', 'Fairy']
        half = ['Psychic', 'Steel']
        ineffective = ['Dark']
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'bug':
        double = ['Grass', 'Psychic', 'Dark']
        normal = ['Normal', 'Water', 'Electric', 'Ice', 'Ground',
                  'Bug', 'Rock', 'Dragon']
        half = ['Fire', 'Fighting', 'Poison', 'Flying', 'Ghost',
                'Steel', 'Fairy']
        ineffective = []
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'rock':
        double = ['Fire', 'Ice', 'Flying', 'Bug']
        normal = ['Normal', 'Water', 'Electric', 'Grass', 'Poison',
                  'Psychic', 'Rock', 'Ghost', 'Dragon', 'Dark',
                  'Fairy']
        half = ['Fighting', 'Ground', 'Steel']
        ineffective = []
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'ghost':
        double = ['Psychic', 'Ghost']
        normal = ['Fire', 'Water', 'Electric', 'Grass', 'Ice',
                  'Fighting', 'Poison', 'Ground', 'Flying', 'Bug',
                  'Rock', 'Dragon', 'Steel', 'Fairy']
        half = ['Dark']
        ineffective = ['Normal']
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'dragon':
        double = ['Dragon']
        normal = ['Psychic', 'Ghost', 'Fire', 'Water', 'Electric',
                  'Grass', 'Ice', 'Fighting', 'Poison', 'Ground',
                  'Flying', 'Bug', 'Rock', 'Dark', 'Normal']
        half = ['Steel']
        ineffective = ['Fairy']
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'dark':
        double = ['Psychic', 'Ghost']
        normal = ['Fire', 'Water', 'Electric', 'Grass', 'Ice',
                  'Poison', 'Ground', 'Flying', 'Bug', 'Rock',
                  'Normal', 'Dragon', 'Steel']
        half = ['Fighting', 'Dark', 'Fairy']
        ineffective = []
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'steel':
        double = ['Ice', 'Rock', 'Fairy']
        normal = ['Normal', 'Grass', 'Fighting', 'Poison', 'Ground',
                  'Flying', 'Psychic', 'Bug', 'Ghost', 'Dragon',
                  'Dark']
        half = ['Fire', 'Water', 'Electric', 'Steel']
        ineffective = []
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})

    elif type == 'fairy':
        double = ['Fighting', 'Dragon', 'Dark']
        normal = ['Normal', 'Water', 'Electric', 'Grass', 'Ice',
                  'Ground', 'Flying', 'Psychic', 'Bug', 'Rock',
                  'Ghost', 'Fairy']
        half = ['Fire', 'Poison', 'Steel']
        ineffective = []
        return jsonify({'Deal 2x in:': double,
                        'Deal 1x in:': normal,
                        'Deal 0.5x in:': half,
                        'Deal no damage:': ineffective})


app.run(host='0.0.0.0')
