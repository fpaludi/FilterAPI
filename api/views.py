from flask import Blueprint, request, jsonify, render_template
from api import models

# Blueprints
router = Blueprint("api", __name__, template_folder="templates")
main = Blueprint("main", __name__, template_folder="templates")


@main.route("/", methods=("GET",))
def index():
    return render_template("index.html")


@router.route("/countries/all", methods=("GET",))
def countries_get_all():
    countries = models.Countries()
    filtered_df = countries.get_all_data()
    return jsonify(filtered_df.to_dict())


@router.route("/countries/life_satisfaction_gt/<value>", methods=("GET",))
def countries_life_satisfaction_gt(value):
    try:
        float_value = float(value)
        if float_value > 0:
            countries = models.Countries()
            filter_dict = dict(Indicator="Life satisfaction", Inequality="Total")
            filtered_df = countries.get_countries_value_gt(float_value, **filter_dict)[
                ["Country", "Value"]
            ]
            return jsonify(
                filtered_df.rename(columns={"Value": "LifeSatisfactionValue"})
                .set_index("Country")
                .to_dict()
            )
    except ValueError:
        pass
    message = {
        "status": 400,
        "message": "Bad Request: The index must be a number greater than 0",
    }
    response = jsonify(message)
    response.status_code = 400
    return response


@main.app_errorhandler(404)
def error_404(error):
    message = {
        "status": 404,
        "message": "Not Found: " + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response
