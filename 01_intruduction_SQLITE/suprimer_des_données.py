import sqlite3

conn = sqlite3.connect("database1.db")
c = conn.cursor()

# Création de la table si elle n'existe pas déjà
c.execute("""
CREATE TABLE IF NOT EXISTS employees
(   
    salaire int,
    prenom text,
    nom text
)
""")

# Insertion d'un enregistrement dans la table
c.execute("""
INSERT INTO employees (salaire, prenom, nom) VALUES (?, ?, ?)
""", (9000, "Glécia", "MAINDRON"))

# Mise à jour de l'enregistrement
d1 = {"salaire": 10000, "prenom": "Glécia", "nom": "MAINDRON"}

c.execute("""
UPDATE employees SET salaire=:salaire WHERE prenom=:prenom AND nom=:nom
""", d1)

# Vérification de la mise à jour
c.execute("SELECT * FROM employees WHERE prenom=:prenom AND nom=:nom", {"prenom": "Glécia", "nom": "MAINDRON"})
print(c.fetchall())  # Cela devrait afficher [(10000, 'Glécia', 'MAINDRON')]

c.execute("""
DELETE FROM employees WHERE prenom='Glécia'

""")

conn.commit()
conn.close()
