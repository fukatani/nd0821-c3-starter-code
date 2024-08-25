# Script to train machine learning model.

from sklearn.model_selection import train_test_split
import pandas

# Add the necessary imports for the starter code.

from ml.data import process_data
from ml.model import train_model, compute_model_metrics

# Add code to load in the data.

data = pandas.read_csv("./data/cleaned_census.csv")

# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.20)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)

# Proces the test data with the process_data function.

X_test, y_test, _, _ = process_data(
    train, categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb
)

# Train and save a model.

trained_model = train_model(X_train, y_train)
y_pred = trained_model.predict(X_test)
compute_model_metrics(y_test, y_pred)

# add data slicing