from flask import Flask

app = Flask(__name__)


@app.route('/hola/chau')
def hola():
     return 'hola'
## alado de  / se pone otro nombre opcional 
def chau():
    return 'chau'