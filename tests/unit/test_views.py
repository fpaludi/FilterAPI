import pytest
import json
import pandas as pd
from flask import jsonify
from top_app import create_app
from api.models import STATIC_DB_NAME


@pytest.fixture
def client(request):
    # SetUp
    app = create_app()
    app.config.update(TESTING=True, DEBUG=True)
    test_client = app.test_client()

    # "Running"
    yield test_client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_get_all_countries(client):
    # Load reference dataframe
    df = pd.read_csv(f"api/data/{STATIC_DB_NAME}")
    df.index = df.index.astype(str)
    item1 = df.fillna(-3).to_dict()  # dealing with nans in json

    # Get value from endpoint
    response = client.get("api/v1.0/countries/all")
    item2 = json.loads(response.get_data(as_text=True).replace("NaN", "-3")) # dealing with nans in json

    assert response.status_code == 200
    assert item1 == item2


def test_life_satisfaction_gt(client):
    for i_value in [5, 5.5]: # to check int and float endpoints
        # Load reference dataframe
        df = pd.read_csv(f"api/data/{STATIC_DB_NAME}")
        mask = ((df["Indicator"] == "Life satisfaction") &
                (df["Inequality"] == "Total") & 
                (df["Value"] > i_value)
        )
        df = df.loc[mask, ["Country", "Value"]]
        item1 = df.rename(columns={"Value": "LifeSatisfactionValue"}).set_index("Country").to_dict()

        # Get value from endpoint
        response = client.get(f"api/v1.0/countries/life_satisfaction_gt/{i_value}")
        item2 = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert item1 == item2


def test_fail_life_satisfaction_gt(client):
    # Load reference dataframe
    VALUE1 = 5 
    VALUE2 = 7
    df = pd.read_csv(f"api/data/{STATIC_DB_NAME}")
    mask = ((df["Indicator"] == "Life satisfaction") &
            (df["Inequality"] == "Total") & 
            (df["Value"] > VALUE1)
    )
    df = df.loc[mask, ["Country", "Value"]]
    item1 = df.rename(columns={"Value": "LifeSatisfactionValue"}).set_index("Country").to_dict()

    # Get value from endpoint
    response = client.get(f"api/v1.0/countries/life_satisfaction_gt/{VALUE2}")
    item2 = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert item1 != item2
    assert VALUE1 != VALUE2

def test_bad_value_life_satisfaction_gt(client):
    # Get value from endpoint
    response = client.get(f"api/v1.0/countries/life_satisfaction_gt/-2")
    assert response.status_code == 400
    response = client.get(f"api/v1.0/countries/life_satisfaction_gt/-3.9")
    assert response.status_code == 400
    response = client.get(f"api/v1.0/countries/life_satisfaction_gt/stringvalue")
    assert response.status_code == 400

def test_error_handler(client):
    # Get value from endpoint
    response = client.get(f"/bad_endpoint")
    assert response.status_code == 404
    response = client.get(f"api/v1.0/countries/bad_endpoint")
    assert response.status_code == 404
