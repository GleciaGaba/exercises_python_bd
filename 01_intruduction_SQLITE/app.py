import sqlite3

conn = sqlite3.connect("database.db")  # connection avec la bd.

c = conn.cursor()  # Le curseur nous permet de créer des requêtes SQL.
c.execute("""
CREATE TABLE IF NOT EXISTS employees(
    salaire int,
    prenom text,
    nom text
)
""")

d = {"salaire": 800, "prenom": "Paul", "nom": "Dupond"}
c.execute("INSERT INTO employees VALUES (:salaire, :prenom, :nom)", d)

conn.commit()  # La fonction commit() est responsable d'envoyer tout ce qui a été exécuté.

conn.close()
