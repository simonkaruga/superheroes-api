from flask import Blueprint, jsonify, request
from .models import db, Hero, Power, HeroPower

bp = Blueprint('api', __name__)

@bp.route("/")
def home():
    return {"message": "Superheroes API running"}

@bp.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict(only=("id", "name", "super_name")) for hero in heroes])

@bp.route("/heroes/<int:id>", methods=["GET"])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero.to_dict())

@bp.route("/powers", methods=["GET"])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@bp.route("/powers/<int:id>", methods=["GET"])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict())

@bp.route("/powers/<int:id>", methods=["PATCH"])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    try:
        power.description = request.json["description"]
        db.session.commit()
        return jsonify(power.to_dict())
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

@bp.route("/hero_powers", methods=["POST"])
def create_hero_power():
    try:
        hp = HeroPower(**request.json)
        db.session.add(hp)
        db.session.commit()
        return jsonify(hp.to_dict()), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
