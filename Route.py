from flask import Flask
app = Flask(__name__)
@app.route("/tirar-dado/<int : caras>")
def dado(caras):
    from random import randint
    n = randint(1,caras)
    return f"<p>tire un dado de {caras} caras ,salio {n}</p>"

