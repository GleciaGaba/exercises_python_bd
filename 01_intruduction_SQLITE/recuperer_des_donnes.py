import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom text,
    nom text
)
""")

c.execute("SELECT * FROM employees WHERE prenom='Paul'")
donnees = c.fetchall()  # La fonction fetchall() nous permet de récupérer tous les résultats de la requête exécutée
# avec la fonction execute.
print(donnees)
conn.commit()
conn.close()

