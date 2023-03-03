from flask import Blueprint, jsonify, request

from services.crawler_client import CrawlerClient
from utils.utils import valid_cpf
from config.config import Config

benefits_blue_print = Blueprint('benefits', __name__, url_prefix='/benefits')

config = Config
@benefits_blue_print.route("/detailed", methods=["POST"])
def get_detailed_benefits():
    cpf = request.form["cpf"]
    login_user = request.form["login_user"]
    login_password = request.form["login_password"]

    cpf_is_valid = valid_cpf(cpf)
    if not cpf_is_valid:
        return jsonify(error="The given cpf is not a valid cpf"), 400

    try:
        benefit = CrawlerClient(
            app_config=config,
            login_user=login_user,
            login_password=login_password,
        ).get_benefits(cpf=cpf)
        return jsonify(benefit_number=benefit), 200

    except Exception as error:
        return jsonify(error=error), 400
