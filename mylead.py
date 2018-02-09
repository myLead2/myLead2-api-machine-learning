from flask            import Flask, request, jsonify
from flask_cors       import CORS

app = Flask(__name__)
CORS(app)

from routes import *

if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)
    
    