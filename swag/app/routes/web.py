from flask import Blueprint, Flask, render_template, request, redirect, url_for, make_response, session, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from ...db import db
from ...db.models import User
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os 

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# Point de départ : ce fichier (web.py) dans swag/app/routes
CURRENT_DIR = os.path.dirname(__file__)  # => .../swag/app/routes

# Remonter à la racine du projet SWAG-APP
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, '..', '..', '..'))  # => .../SWAG-APP

# Construire le chemin vers uploads/
UPLOAD_FOLDER = os.path.join(PROJECT_ROOT, 'uploads')

# Optionnel : créer le dossier s'il n'existe pas
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class AppCard:
    def __init__(self, id, title, description, img_url, img_alt):
        self.id = id
        self.title = title
        self.description = description
        self.img_url = img_url
        self.img_alt = img_alt


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


web = Blueprint("web", __name__)




@web.route('/uploads/<filename>')
def uploaded_file(filename):
    filename = secure_filename(filename)  # protection sécurité
    return send_from_directory(UPLOAD_FOLDER, filename)




@web.route("/", methods=["GET"])
def index():
    if session and session["username"]:
        return redirect(url_for('web.dashboard'))
    return render_template("index.html")



@web.route("/signup", methods=["GET"])
def signup():
    if session and session["username"]:
        return redirect(url_for("web.dashboard")) 
    if request.headers.get("HX-Request"):      
        return render_template("fragments/signup.html")
    return render_template("pages/signun_page.html")


@web.route("/login", methods=["GET"])
def login():
    if session and session["username"]:
        return redirect(url_for("web.dashboard"))
    if request.headers.get("HX-Request"):      
        return render_template("fragments/login.html")
    return render_template("pages/login_page.html")

@web.route("/dashboard", methods=["GET"])
def dashboard():
    if session and session["username"]:
        email = session["username"]
        user = db.session.execute(db.select(User).filter_by(email)).scalar()
        if user:
            return render_template("fragments/dashboard.html", user=user)
    session["error"] = {'title': 'Bad Request', 'message':'Invalid Data'}
    return redirect(url_for("web.error"))


@web.route("/users/create", methods=["POST"])
def user_create():

    if 'photo' not in request.files:
        flash('No photo part')
        return redirect(request.url)
    file = request.files['photo']
    if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
    password = request.form.get("password")
    user = User(
            email=request.form["email"],
            firstname=request.form["firstname"],
            lastname=request.form["lastname"],
            photo_url=filename

    )
    user.password=password
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("web.login"))

@web.route("/auth/login", methods=["POST"])
def auth_login():

    email = request.form.get("email")
    password = request.form.get("password")
    keep_connection = request.form.get("keep-connection")
    print(f"🎾 keep connection: {keep_connection}")

    user = db.session.execute(db.select(User).filter_by(email)).scalar()
    if user.check_password(password):
        resp = make_response(redirect(url_for("web.dashboard")))
        #resp.set_cookie("user_email", email)
        session["username"] = email
        return resp
    session["error"] = {'title': 'Bad Request', 'message':'You have failed to log in'}
    return redirect(url_for("web.error"))



@web.route("/admin/dashboard")
def admin_dashboard():
    if session and session["username"]:
        email = session["username"]
        user = db.session.execute(db.select(User).filter_by(email)).scalar()
        if user.role == "admin":
            users = db.session.execute(db.select(User).order_by(User.username)).scalars()
            return render_template("fragments/admin.html", users, users)
        else:
            session["error"] = { 'title': 'Not Allowed', 'message': 'You are not an administrator'}
            return redirect(url_for('web.error'))




@web.route("/home", methods=["GET"])
def home():
    hero_cards_list = [
        AppCard(1, "Men", "Description for Men", "https://images.pexels.com/photos/18398385/pexels-photo-18398385.jpeg", "two men"),
        AppCard(2, "Women", "Description for Women", "https://images.pexels.com/photos/1152994/pexels-photo-1152994.jpeg", "a woman touching her hair"),
        AppCard(3, "Children", "Description for Children", "https://images.pexels.com/photos/32627917/pexels-photo-32627917.jpeg", "a child in a bedroom"),
    ]
    if request.headers.get("HX-Request"):
        return render_template("fragments/home.html", cards=hero_cards_list)
    return render_template("pages/home_page.html", cards=hero_cards_list)

@web.route("/logout", methods=["GET"])
def logout():
    session.pop("username", None)
    resp = make_response(redirect(url_for("web.login")))
    #resp.set_cookie("user_email", "", expires=0)
    return resp


@web.route("/error", methods=["GET"])
def error():
    error = session.pop("error", {'title': 'Unknown Error', 'message': 'An unknown error occurred.'})
    return render_template("fragments/error.html", error=error)


@web.errorhandler(404)
def page_not_found(error):
    return render_template("fragments/not_found.html"), 404
