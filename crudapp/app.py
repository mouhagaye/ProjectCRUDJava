from flask import Flask,render_template,request,redirect,url_for
import requests
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')
    
@app.route('/agence')
def agence():
    res = requests.get("http://localhost:9191/agences")
    res = list(res.json())
    context = res
    return render_template('agence.html',contexts=context)

@app.route('/ajouterAgence', methods=['POST'])
def ajouterAgence():
    code = request.form['code']
    adresse = request.form['adresse']
    nom = request.form['nom']
    telephone = request.form['telephone']

    x = requests.post('http://localhost:9191/addAgence',json = {"code": code, "adresse": adresse, "nom": nom, "telephone":telephone})

    return redirect(url_for('agence'))


@app.route('/deleteAgence/<code>', methods=['GET'])
def deleteAgence(code):

    url = 'http://localhost:9191/deleteAgence/'+code
    x = requests.delete(url)

    print(url)

    return redirect(url_for('agence'))


@app.route('/editAgence', methods=['POST'])
def editAgence():
    code = request.form['code']
    adresse = request.form['adresse']
    nom = request.form['nom']
    telephone = request.form['telephone']

    x = requests.put('http://localhost:9191/updateAgence',json = {"code": code, "adresse": adresse, "nom": nom, "telephone":telephone})
    print(x)

    return redirect(url_for('agence'))

@app.route('/editAgenceVue', methods=['GET'])
def editAgenceVue():

    return render_template('agence.html',id="editAgence")


if __name__ == '__main__':
    app.run()