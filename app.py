from flask import Flask, url_for 
from flask import  render_template
import sqlite3
 

app = Flask(__name__)
db = None

def dict_factory(cursor, row):
   """Arma un diccionario con los valores de la fila."""
   fields = [column[0] for column in cursor.description]
   return {key: value for key, value in zip(fields, row)}


def abrirConexion():
     global db
     db = sqlite3.connect("instance/datos.sqlite") 
     db.row_factory = dict_factory

def cerrarConexion():
    global db
    db.close()
    db = None
@app.route("/agregar-usuario/")
def testCrear():
    nombre = ""
    email = ""
    abrirConexion()
    cursor = db.cursor()
    consulta = "INSERT INTO usuarios(usuario, email)VALUES (?, ?);"
    cursor.execute(consulta,(nombre,email))
    db.commit()
    cerrarConexion()
    return f"registro agregado {[nombre]}"
    
@app.route('/test/db')
def testDB():
     abrirConexion()
     cursor = db.cursor()
     res = cursor.execute("SELECT COUNT(*) AS cant FROM usuarios;")
     res = cursor.fetchone()
     registros = res["cant"]
     cerrarConexion()
     return f"Hay {registros} registros en la tabla de usuarios "


@app.route("/hola")
def hola():
     return 'hola'
## alado de  / se pone otro nombre opcional 
@app.route("/chau")
def chau():
    return 'chau'

@app.route("/")
def main():
     url_hola = url_for("hola")
     url_dado = url_for("dado" , caras=6)
     url_logo = url_for("static", filename="img/logo5f.jpg")
  
     return f"""
     <a href="{url_hola}">hola</a>
     <br>
     <a href="{url_for("chau")}">chau</a>
     <br>
     <a href="{url_logo}">logo</a>
     <br>
     <a href="{url_dado}">tirar_dado</a>

     """

@app.route("/tirar-dado/<int:caras>")
def dado(caras):
    from random import randint
    n = randint(1,caras)
    return f"<p>tire un dado de {caras} caras ,salio {n}</p>"



@app.route("/mostrar-datos-plantilla/<int:id>")
def datos_plantilla(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT id, usuario, email FROM usuarios WHERE id = ? ;",(id,))
    res = cursor.fetchone()
    cerrarConexion()
    usuario = None 
    email = None
    if res != None:
        usuario=res['usuario']
        email=res['email']
    return render_template("datos.html" , id=id , usuario=usuario , email=email)    


