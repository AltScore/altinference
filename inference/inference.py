import pandas as pd
import dill


class Inferer:
    def __init__(self, model_path: str, pipeline_path: str, selected_features: list):
        self.model = dill.load(open(model_path, "rb"))
        self.pipeline = dill.load(open(pipeline_path, "rb"))
        self.selected_features = selected_features

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

    def predict_probability(self, data: pd.DataFrame):
        model_selected_features = self.selected_features
        selected_features = self._get_original_variables(
            model_selected_features, data.columns, "_"
        )
        data = data[selected_features]
        data_processed = self.pipeline.transform(data)
        pd = self.model.predict_proba(data_processed[model_selected_features])[:, 1]
        return pd
