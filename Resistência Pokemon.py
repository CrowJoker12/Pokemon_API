from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<tipo>')
def fr(tipo):
    if tipo == 'normal':
        dobro = []
        normal = ['Normal', 'Fogo', 'Agua', 'Grama', 'Eletrico',
                  'Gelo', 'Lutador', 'Veneno', 'Terra', 'Voador',
                  'Psiquico', 'Inseto', 'Dragao', 'Trevas', 'Fada']
        metade = ['Pedra', 'Aco']
        inefetivo = ['Fantasma']
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'fogo':
        dobro = ['Grama', 'Gelo', 'Inseto', 'Aco']
        normal = ['Normal', 'Eletrico', 'Lutador', 'Veneno', 'Terra',
                  'Voador', 'Psiquico', 'Fantasma', 'Trevas', 'Fada']
        metade = ['Fogo', 'Agua', 'Pedra', 'Dragao']
        inefetivo = []
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'agua':
        dobro = ['Fogo', 'Terra', 'Pedra']
        normal = ['Normal', 'Eletrico', 'Lutador', 'Veneno', 'Voador',
                  'Psiquico', 'Fantasma', 'Trevas', 'Fada',
                  'Gelo', 'Inseto', 'Aco']
        metade = ['Agua', 'Grama', 'Dragao']
        inefetivo = []
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'eletrico':
        dobro = ['Agua', 'Voador']
        normal = ['Fogo', 'Pedra', 'Normal', 'Lutador', 'Veneno',
                  'Psiquico', 'Fantasma', 'Trevas', 'Fada', 'Gelo',
                  'Inseto', 'Aco']
        metade = ['Eletrico', 'Grama', 'Dragao']
        inefetivo = ['Terra']
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'grama':
        dobro = ['Agua', 'Terra', 'Pedra']
        normal = ['Normal', 'Eletrico', 'Gelo', 'Lutador',
                  'Psiquico', 'Fantasma', 'Trevas', 'Fada']
        metade = ['Fogo', 'Grama', 'Veneno', 'Voador',
                  'Inseto', 'Dragao', 'Aco']
        inefetivo = []
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'gelo':
        dobro = ['Grama', 'Terra', 'Voador', 'Dragao']
        normal = ['Normal', 'Eletrico', 'Lutador', 'Veneno',
                  'Psiquico', 'Inseto', 'Pedra', 'Fantasma',
                  'Trevas', 'Fada']
        metade = ['Fogo', 'Agua', 'Gelo', 'Aco']
        inefetivo = []
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'lutador':
        dobro = ['Normal', 'Gelo', 'Pedra', 'Trevas', 'Aco']
        normal = ['Fogo', 'Agua', 'Eletrico', 'Grama',
                  'Lutador', 'Terra', 'Dragao']
        metade = ['Veneno', 'Voador', 'Psiquico', 'Inseto', 'Fada']
        inefetivo = ['Fantasma']
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'veneno':
        dobro = ['Grama', 'Fada']
        normal = ['Normal', 'Fogo', 'Agua', 'Eletrico', 'Gelo',
                  'Lutador', 'Voador', 'Psiquico', 'Inseto', 'Dragao', 'Trevas']
        metade = ['Veneno', 'Terra', 'Pedra', 'Fantasma']
        inefetivo = ['Aco']
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'terra':
        dobro = ['Fogo', 'Eletrico', 'Veneno', 'Pedra', 'Aco']
        normal = ['Normal', 'Agua', 'Gelo', 'Lutador', 'Terra',
                  'Psiquico', 'Fantasma', 'Dragao', 'Trevas', 'Fada']
        metade = ['Grama', 'Inseto']
        inefetivo = ['Voador']
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'voador':
        dobro = ['Grama', 'Lutador', 'Inseto']
        normal = ['Normal', 'Fogo', 'Agua', 'Gelo', 'Veneno',
                  'Terra', 'Voador', 'Psiquico', 'Fantasma', 'Dragao',
                  'Trevas', 'Fada']
        metade = ['Eletrico', 'Pedra', 'Aco']
        inefetivo = []
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'psiquico':
        dobro = ['Lutador', 'Veneno']
        normal = ['Normal', 'Fogo', 'Agua', 'Eletrico', 'Grama',
                  'Gelo', 'Terra', 'Voador', 'Inseto', 'Pedra',
                  'Fantasma', 'Dragao', 'Fada']
        metade = ['Psiquico', 'Aco']
        inefetivo = ['Trevas']
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'inseto':
        dobro = ['Grama', 'Psiquico', 'Trevas']
        normal = ['Normal', 'Agua', 'Eletrico', 'Gelo', 'Terra',
                  'Inseto', 'Pedra', 'Dragao']
        metade = ['Fogo', 'Lutador', 'Veneno', 'Voador', 'Fantasma',
                  'Aco', 'Fada']
        inefetivo = []
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'pedra':
        dobro = ['Fogo', 'Gelo', 'Voador', 'Inseto']
        normal = ['Normal', 'Agua', 'Eletrico', 'Grama', 'Veneno',
                  'Psiquico', 'Pedra', 'Fantasma', 'Dragao', 'Trevas',
                  'Fada']
        metade = ['Lutador', 'Terra', 'Aco']
        inefetivo = []
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'fantasma':
        dobro = ['Psiquico', 'Fantasma']
        normal = ['Fogo', 'Agua', 'Eletrico', 'Grama', 'Gelo',
                  'Lutador', 'Veneno', 'Terra', 'Voador', 'Inseto',
                  'Pedra', 'Dragao', 'Aco', 'Fada']
        metade = ['Trevas']
        inefetivo = ['Normal']
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'dragao':
        dobro = ['Dragao']
        normal = ['Psiquico', 'Fantasma', 'Fogo', 'Agua', 'Eletrico',
                  'Grama', 'Gelo', 'Lutador', 'Veneno', 'Terra',
                  'Voador', 'Inseto', 'Pedra', 'Trevas', 'Normal']
        metade = ['Aco']
        inefetivo = ['Fada']
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'trevas':
        dobro = ['Psiquico', 'Fantasma']
        normal = ['Fogo', 'Agua', 'Eletrico', 'Grama', 'Gelo',
                  'Veneno', 'Terra', 'Voador', 'Inseto', 'Pedra',
                  'Normal', 'Dragao', 'Aco']
        metade = ['Lutador', 'Trevas', 'Fada']
        inefetivo = []
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'aco':
        dobro = ['Gelo', 'Pedra', 'Fada']
        normal = ['Normal', 'Grama', 'Lutador', 'Veneno', 'Terra',
                  'Voador', 'Psiquico', 'Inseto', 'Fantasma', 'Dragao',
                  'Trevas']
        metade = ['Fogo', 'Agua', 'Eletrico', 'Aco']
        inefetivo = []
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})

    elif tipo == 'fada':
        dobro = ['Lutador', 'Dragao', 'Trevas']
        normal = ['Normal', 'Agua', 'Eletrico', 'Grama', 'Gelo',
                  'Terra', 'Voador', 'Psiquico', 'Inseto', 'Pedra',
                  'Fantasma', 'Fada']
        metade = ['Fogo', 'Veneno', 'Aco']
        inefetivo = []
        return jsonify({'Causa 2x a:': dobro,
                        'Causa 1x a': normal,
                        'Causa 0.5x a:': metade,
                        'Nao causa dano:': inefetivo})


app.run(host='0.0.0.0')
