from flask import Flask
from flask import url_for
app = Flask(__name__)


@app.route('/hola/chau')
def hola():
     return 'hola'
## alado de  / se pone otro nombre opcional 
def chau():
    return 'chau'

@app.route("/")
def main():
     url_hola = url_for("hello")
     url_dado = url_for("dado" , caras=6)
     url_logo = url_for("static", filename="img/logo.jpg")
  
     return f"""
     <a href="{url_hola}">hola</a>
     <br>
     <a href="{url_for("bye")}">chau</a>
     <br>
     <a href="{url_logo}">logo</a>
     <br>
     <a href="{url_dado}">tirar_dado</a>
     """