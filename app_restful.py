import json

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = "Desnvolvedor de ID {} não existe".format(id)
            response = {'status': 'error', 'mensagem': mensagem}
        except Exception:
            mensagem = "Erro desconhecido comunique o adm da API"
            response = {'status': 'error', 'mensagem': mensagem}
        return response

    def delete(self, id):
        desenvolvedores.pop(id)
        return ({'status': 'successo', 'mensagem': 'Registro Excluído com sucesso'})

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        if request.method == 'POST':
            dados = json.loads(request.data)
            posicao = len(desenvolvedores)
            dados[id] = posicao
            desenvolvedores.append(dados)
            # return desenvolvedores[posicao]
            return ({'status': 'successo', 'posicao': posicao, 'mensagem': 'Registro incluído com sucesso'})


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)
