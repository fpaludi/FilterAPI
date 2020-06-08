import pytest
import pandas as pd
from api.models import Countries, STATIC_DB_NAME

def test_get_all_countries():
    df = pd.read_csv(f"api/data/{STATIC_DB_NAME}")
    countries = Countries()
    df_test = pd.concat([countries.get_all_data(), df]).drop_duplicates(keep=False)
    assert df_test.shape[0] == 0

def test_get_countries_value_gt():
    df = pd.read_csv(f"api/data/{STATIC_DB_NAME}")
    countries = Countries()
    df_test = pd.concat([countries.get_countries_value_gt(3), df[df["Value"] > 3]]).drop_duplicates(keep=False)
    assert df_test.shape[0] == 0

    filter_dict = dict(Indicator="Life satisfaction", Inequality="Total")
    mask = ((df["Indicator"] == "Life satisfaction") &
            (df["Inequality"] == "Total") & 
            (df["Value"] > 3)
    )
    df_test = pd.concat([countries.get_countries_value_gt(3, **filter_dict), df.loc[mask, :]]).drop_duplicates(keep=False)
    assert df_test.shape[0] == 0
