from src import app, models
from flask import render_template


@app.route('/')
@app.route("/accueil")
def accueil():
    liste_chambres = models.Chambre.query.all()
    return render_template(
        'accueil.html',
        title='Nos chambres',
        chambres=liste_chambres
    )


@app.route('/chambre/<id_chambre>')
def chambre(id_chambre):
    selected_chambre = models.Chambre.query.filter_by(id_chambre=id_chambre).first()
    return render_template(
        'chambre.html',
        title=selected_chambre.nom_chambre,
        chambre=selected_chambre
    )


@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title='Nous contacter'
    )
