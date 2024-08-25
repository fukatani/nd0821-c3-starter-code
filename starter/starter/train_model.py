import pickle

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
    test,
    categorical_features=cat_features,
    label="salary",
    training=False,
    encoder=encoder,
    lb=lb,
)

# Train and save a model.

trained_model = train_model(X_train, y_train)
y_pred = trained_model.predict(X_test)
precision, recall, fbeta = compute_model_metrics(y_test, y_pred)
print(f"precision: {precision}")
print(f"recall: {recall}")
print(f"fbeta: {fbeta}")
pickle.dump(trained_model, open("model/trained_model.pkl", "wb"))
pickle.dump(encoder, open("model/encoder.pkl", "wb"))

# add data slicing
