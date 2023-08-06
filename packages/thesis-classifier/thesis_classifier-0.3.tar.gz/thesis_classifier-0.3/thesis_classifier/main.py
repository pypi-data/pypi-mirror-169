import joblib
from typing import List
from .helper.preprocess import Preprocess


class Classifier:
    def __init__(self):
        self.model = joblib.load('model/sklearn_MNB_2.model')
        self.preprocess = Preprocess()

    def predicts(self, inputs: List[str]):
        predicted_list = self.preprocess.list(inputs)
        predicted_list = self.tf.transform(predicted_list)
        predicted_list = self.model.predict(predicted_list)
        return predicted_list
