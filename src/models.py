from src import app, db
from flask_sqlalchemy import SQLAlchemy

class Chambre(db.Model):
    id_chambre = db.Column(db.Integer, primary_key=True)
    nom_chambre = db.Column(db.String(50), nullable=False)
    prix = db.Column(db.Float(10), nullable=True)
    lit = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(200), nullable=True)
    image_chambre = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'{self.id_chambre} : {self.nom_chambre} : {self.prix} : {self.lit} : {self.description} : {self.image_chambre}'
