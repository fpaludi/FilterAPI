import pandas as pd
import numpy as np

# Load Static Data
STATIC_DB_NAME = "BLI_28032019144925238.csv"
_COUNTRIES_DF = pd.read_csv(f"api/data/{STATIC_DB_NAME}")


class Countries:
    def __init__(self):
        self._data = _COUNTRIES_DF.copy()
        # self._data = pd.read_csv(f"api/data/{STATIC_DB_NAME}")

    def _eq_filter_handlers(self, **kwargs):
        mask = np.array([True] * self._data.shape[0])
        for filter_k, filter_v in kwargs.items():
            if filter_k in self._data.columns:
                mask = mask & (self._data[filter_k] == filter_v).values
        return mask

    def get_all_data(self):
        return self._data

    def get_countries_value_gt(self, value, **kwargs):
        # Extra Filters
        mask = self._eq_filter_handlers(**kwargs)
        # Filter by value
        mask = mask & (self._data["Value"] > value)
        return self._data.loc[mask]
