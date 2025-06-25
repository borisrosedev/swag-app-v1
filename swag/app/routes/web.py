from flask import Blueprint, Flask, render_template, request, jsonify


class AppCard:
    def __init__(self, id, title, description, img_url, img_alt):
        self.id = id
        self.title = title 
        self.description = description
        self.img_url = img_url
        self.img_alt = img_alt
        



web = Blueprint("web", __name__)

@web.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@web.route("/home", methods=["GET"])
def home():

    hero_cards_list = [
        AppCard(1, "Men", "Amet incididunt qui do sunt commodo magna officia esse qui enim aliquip amet. Qui exercitation eu anim esse dolor do consequat sit consequat. Voluptate est dolor non consequat duis veniam aliquip laboris. Proident eiusmod dolore adipisicing ea nostrud duis magna cillum. Consectetur sint minim ullamco voluptate exercitation non sit incididunt dolore elit ullamco consectetur duis. Pariatur sint velit ipsum sit nulla. Irure ea nulla reprehenderit labore est consectetur consequat do irure occaecat ullamco velit esse.","https://images.pexels.com/photos/18398385/pexels-photo-18398385.jpeg", "two men"),
        AppCard(2, "Women", "Ex proident veniam nulla in officia voluptate sunt aute est tempor Lorem enim pariatur. Id non do sit commodo. Est ex qui nulla qui quis. Anim commodo culpa culpa deserunt tempor ut anim deserunt occaecat velit excepteur amet.", "https://images.pexels.com/photos/1152994/pexels-photo-1152994.jpeg", "a woman with black top and beige skirt touching her hair"),
        AppCard(3, "Children", "Nisi enim incididunt proident enim fugiat eiusmod deserunt laborum aliquip. Ut occaecat dolore tempor commodo irure laborum anim ullamco exercitation elit veniam est ipsum. Laboris proident ex officia aute adipisicing laborum. Nulla consequat occaecat anim ad quis reprehenderit Lorem id culpa elit.", "https://images.pexels.com/photos/32627917/pexels-photo-32627917.jpeg", "a child sat in a beautiful bedroom")
    ]

    return render_template('fragments/home.html',cards=hero_cards_list)