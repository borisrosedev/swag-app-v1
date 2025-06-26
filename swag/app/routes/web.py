from flask import Blueprint, Flask, render_template, request, redirect, url_for, make_response, session
from werkzeug.security import generate_password_hash, check_password_hash


class AppCard:
    def __init__(self, id, title, description, img_url, img_alt):
        self.id = id
        self.title = title
        self.description = description
        self.img_url = img_url
        self.img_alt = img_alt


class AppUser:
    def __init__(self, id, firstname, lastname, email, photo_url):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.photo_url = photo_url
        self.password_hash = None

    def get_fullname(self):
        return f"{self.firstname.capitalize()} {self.lastname.capitalize()}"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


web = Blueprint("web", __name__)


users_list = [
    AppUser(1, "clement", "dupont", "clement@gmail.com", "https://images.pexels.com/photos/2379004/pexels-photo-2379004.jpeg"),
    AppUser(2, "linda", "dupuis", "linda@gmail.com", "https://images.pexels.com/photos/1036623/pexels-photo-1036623.jpeg"),
    AppUser(3, "monica", "livi", "monica@gmail.com", "https://images.pexels.com/photos/774095/pexels-photo-774095.jpeg"),
    AppUser(4, "boris", "rose", "boris@gmail.com", "https://images.pexels.com/photos/1680172/pexels-photo-1680172.jpeg"),
]

users_list[0].set_password("caroline1")
users_list[1].set_password("caroline2")
users_list[2].set_password("caroline3")
users_list[3].set_password("caroline4")


@web.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@web.route("/login", methods=["GET"])
def login():
    return render_template("fragments/login.html")


@web.route("/dashboard", methods=["GET"])
def dashboard():
    email = session["username"]
    for user in users_list:
        if user.email == email:
            return render_template("fragments/dashboard.html", user=user)
    return redirect(url_for("web.error"))


@web.route("/auth/login", methods=["POST"])
def auth_login():
    email = request.form.get("email")
    password = request.form.get("password")
    keep_connection = request.form.get("keep-connection")
    print(f"🎾 keep connection: {keep_connection}")

    for user in users_list:
        if user.email == email and user.check_password(password):
            resp = make_response(redirect(url_for("web.dashboard")))
            #resp.set_cookie("user_email", email)
            session["username"] = email
            return resp
    session["error"] = {'title': 'Bad Request', 'message':'You have failed to log in'}
    return redirect(url_for("web.error"))


@web.route("/home", methods=["GET"])
def home():
    hero_cards_list = [
        AppCard(1, "Men", "Description for Men", "https://images.pexels.com/photos/18398385/pexels-photo-18398385.jpeg", "two men"),
        AppCard(2, "Women", "Description for Women", "https://images.pexels.com/photos/1152994/pexels-photo-1152994.jpeg", "a woman touching her hair"),
        AppCard(3, "Children", "Description for Children", "https://images.pexels.com/photos/32627917/pexels-photo-32627917.jpeg", "a child in a bedroom"),
    ]
    return render_template("fragments/home.html", cards=hero_cards_list)


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
