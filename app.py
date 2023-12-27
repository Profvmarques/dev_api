from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id': '0',
     'nome': 'Vinícius',
     'habilidades': ['Python', 'Flask', 'Django']
     },
    {'id': '1',
     'nome': 'André',
     'habilidades': ['Python', 'Flask', 'Django']
     },
]

#devolve um desenvolvedor, altera e exclui
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "Desnvolvedor de ID {} não existe".format(id)
            response = {'status': 'error', 'mensagem': mensagem}
        except Exception:
            mensagem = "Erro desconhecido comunique o adm da API"
            response = {'status': 'error', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'successo', 'mensagem': 'Registro Excluído com sucesso'})

@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados[id] = posicao
        desenvolvedores.append(dados)
        return jsonify({'status': 'successo', 'posicao':posicao, 'mensagem': 'Registro incluído com sucesso'})
    if request.method == 'GET':
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)
