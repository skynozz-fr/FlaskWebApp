from flask import Flask, render_template, request, redirect, url_for
from database import MySQLDatabase


app = Flask(__name__)


# Liste contenant l'utilisateur connecté
utilisateur_connecte = []


# Connexion à la base de données MySQL
db = MySQLDatabase(host="localhost", user="votre_utilisateur", password="votre_mot_de_passe", database="FlaskSql")


# Route pour la page d'accueil
@app.route('/', methods=['GET'])
def index():
    # Vérifier si un utilisateur est connecté
    if utilisateur_connecte:
        message = "Bonjour " + utilisateur_connecte[0]
    else:
        message = "Bonjour utilisateur anonyme"
    return render_template('index.html', message=message, utilisateur_connecte=utilisateur_connecte)


# Route pour la page d'inscription
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Vérifier si les mots de passe correspondent
        if password != confirm_password:
            return render_template('form/signup.html', error="Les mots de passe ne correspondent pas")

        # Vérifier si l'utilisateur existe déjà dans la base de données
        db.connect()
        user = db.execute("SELECT * FROM users WHERE email = %s", (email,)).fetchone()
        if user:
            db.close()
            return render_template('form/signup.html', error="Cet utilisateur existe déjà")
        else:
            # Enregistrer l'utilisateur dans la base de données
            db.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
            db.commit()
            db.close()

        # Rediriger vers la page de connexion
        return redirect(url_for('login'))

    # Afficher le formulaire d'inscription
    return render_template('form/signup.html', error=None)


# Route pour la page de connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        email = request.form['email']
        password = request.form['password']

        # Vérifier si l'utilisateur existe dans la base de données
        db.connect()
        user = db.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password)).fetchone()
        db.close()

        if user:
            # Vérifier si l'utilisateur n'est pas déjà connecté
            if email not in utilisateur_connecte:
                # Ajouter l'utilisateur à la liste des utilisateurs connectés
                utilisateur_connecte.append(email)
            # Rediriger vers la page d'accueil
            return redirect(url_for('index'))
        else:
            # Afficher un message d'erreur si l'utilisateur n'existe pas
            return render_template('form/login.html', error="Adresse e-mail ou mot de passe incorrect")

    # Afficher le formulaire de connexion
    return render_template('form/login.html', error=None)


# Route pour la déconnexion
@app.route('/logout', methods=['GET'])
def logout():
    # Vider la liste de l'utilisateur connecté
    utilisateur_connecte.clear()
    # Rediriger vers la page d'accueil
    return redirect(url_for('index'))


# Routes pour les erreurs 404 et 403
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/errors.html', error_code=404), 404


@app.errorhandler(403)
def forbidden(e):
    return render_template('errors/errors.html', error_code=403), 403


# Route pour les autres erreurs
@app.errorhandler(Exception)
def handle_exception(e):
    return render_template('errors/errors.html', error_code=500), 500


if __name__ == "__main__":
    app.run(debug=True)