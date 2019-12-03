from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

from libs import datenbank

app = Flask("Velotag")

@app.route("/")
@app.route("/index")
def index():
    daten = datenbank.datenbank_lesen()
    return render_template("index.html", datenbank=daten)

@app.route("/hinzuguegen", methods=['GET', 'POST'])
def hinzufuegen():
    if (request.method == 'POST'):
        datenbank.eintrag_speichern_von_formular(request.form)
        return redirect("/")

    return render_template("hinzufuegen.html")

# @app.route("/datenbank", methods=['GET', 'POST'])
# def datenbank():
    # if (request.method == 'GET'):
    # daten = datenbank.datenbank_lesen()
    # return render_template("datenbank.html", datenbank=daten)

if __name__ == "__main__":
    app.run(debug=True, port=5000)