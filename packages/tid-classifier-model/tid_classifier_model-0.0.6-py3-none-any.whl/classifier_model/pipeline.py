import re
from typing import List
import numpy as np
# to handle datasets
import pandas as pd
from classifier_model.processing.features import ExtractLetterTransformer
from feature_engine.encoding import OneHotEncoder, RareLabelEncoder
from feature_engine.imputation import (AddMissingIndicator, CategoricalImputer,
                                       MeanMedianImputer)
from sklearn.linear_model import LogisticRegression
# to divide train and test set
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from classifier_model.config.core import config

titanic_pipe = Pipeline(
    [
        # ===== IMPUTATION =====
        # impute categorical variables with string 'missing'
        (
            "categorical_imputation",
            CategoricalImputer(
                imputation_method="missing", variables=config.model_config.cat_vars,
            ),
        ),
        # add missing indicator to numerical variables
        (
            "missing_indicator",
            AddMissingIndicator(variables=config.model_config.num_vars),
        ),
        # impute numerical variables with the median
        (
            "median_imputation",
            MeanMedianImputer(
                imputation_method="median", variables=config.model_config.num_vars
            ),
        ),
        # # Extract first letter from cabin
        (
            "extract_letter",
            ExtractLetterTransformer(variables=config.model_config.cabin),
        ),
        # == CATEGORICAL ENCODING ======
        # remove categories present in less than 5% of the observations (0.05)
        # group them in one category called 'Rare'
        (
            "rare_label_encoder",
            RareLabelEncoder(
                tol=0.05, n_categories=1, variables=config.model_config.cat_vars
            ),
        ),
        # encode categorical variables using one hot encoding into k-1 variables
        (
            "categorical_encoder",
            OneHotEncoder(variables=config.model_config.cat_vars, drop_last=True),
        ),
        # scale using standardization
        ("scaler", StandardScaler()),
        # logistic regression (use C=0.0005 and random_state=0)
        ("Logit", LogisticRegression(C=0.0005, random_state=0)),
    ]
)
