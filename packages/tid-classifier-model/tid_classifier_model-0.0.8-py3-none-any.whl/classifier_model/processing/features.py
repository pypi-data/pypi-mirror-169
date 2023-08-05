from sklearn.base import BaseEstimator, TransformerMixin
from typing import List

class ExtractLetterTransformer(BaseEstimator, TransformerMixin):
    # Extract fist letter of variable

    def __init__(self, variables: List[str]):
        
        if not isinstance(variables, list):
            raise ValueError("Variables should be a list")
        
        self.variables = variables
        

    def fit(self, X, y=None):
        return self
        

    def transform(self, X):
        X = X.copy()
        
        for feature in self.variables:
            X[feature] = X[feature].str[0]
        
        return X
