from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/') #Hauptseite für die Übersicht.
def main():
    return render_template("index.html")

# @app.route('/recipes') #Subseite für die Rezepte

def recipe():
    nutrition_facts = [
    {
        "name" : "Banane",
        "kcal" : "Chur",
        "prot" : "4.0",
        "fett" : "Calanda",
        "kohl" : 2.80
    },
    {
        "name" : "Banane",
        "kcal" : "Chur",
        "prot" : "4.0",
        "fett" : "Calanda",
        "kohl" : 2.80
    }

if __name__ == "__main__":
    app.run(debug=True, port=5000)
