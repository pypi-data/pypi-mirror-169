import joblib
from typing import List
from thesis_classifier.helper.preprocess import Preprocess
from pathlib import Path

path = Path(__file__).parent/'models/sklearn_MNB_2.model'


class Classifier:
    def __init__(self):
        self.model = joblib.load(path)
        self.preprocess = Preprocess()

    def predicts(self, inputs: List[str]):
        predicted_list = self.preprocess.list(text_list=inputs)
        return predicted_list
