from flask import Blueprint

bp = Blueprint("bluetooth", __name__, url_prefix="/bluetooth")


@bp.route("", methods=["GET"])
def get_bluetooth():
    return "Hello World"
