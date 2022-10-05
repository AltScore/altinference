import pandas as pd
import dill
import numpy as np


class Inferer:
    def __init__(self, model_path: str, pipeline_path: str):
        self.model = dill.load(open(model_path, "rb"))
        self.pipeline = dill.load(open(pipeline_path, "rb"))
        self.selected_features = self.model.feature_names_in_.tolist()

    def _get_original_variables(
        self, model_selected_features: list, columns: list, separator: str
    ):
        selected_features = []
        for feature in model_selected_features:
            if feature in columns:
                selected_features.append(feature)
            else:
                selected_features.append(feature.rsplit(separator, 1)[0])
        return selected_features

    def _fill_missing_features(self, data: pd.DataFrame, needed_features: list):
        for feature in needed_features:
            if feature not in data.columns:
                data[feature] = np.nan
        return data

    def predict_probability(self, data: pd.DataFrame):
        model_selected_features = self.selected_features
        selected_features = self._get_original_variables(
            model_selected_features, data.columns, "_"
        )
        data = self._fill_missing_features(data, selected_features)
        data = data[selected_features]
        data_processed = self.pipeline.transform(data)
        pd = self.model.predict_proba(data_processed[model_selected_features])[:, 1]
        return pd
