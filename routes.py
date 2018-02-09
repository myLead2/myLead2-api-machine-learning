from flask import Flask, request, jsonify, render_template
from mylead import app
from controller.Queue import *

#verifica a fila
@app.route('/varify/queue', methods=['GET'])
def verifyQueue():
    if(queue.getStatus()):
        return ({"status": "busy", "data": queue.getStatus()})    
    
    return ({"status": "free", "data": queue.getStatus()})    


#recebe data para limpar
@app.route('/data/cleaning', methods=['POST'])
def toDataCleaning():

    data  = request.get_json()
    print(data)
    return jsonify({'status': 'error', 'message': 'Sem ocorrencias', 'data': {}})
#informa se a fila ta vazia
#retorna data limpa para guardar no banco