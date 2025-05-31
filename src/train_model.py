import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

""""This script trains a spam classification model using labeled email data."""


def train_and_save_model():

    # get the path to the data directory where the labeled CSV file is located
    dataPath = os.path.join(os.getcwd(), "../data")

    # read the CSV file into a DataFrame, use your own csv here which you labeled
    df = pd.read_csv(os.path.join(dataPath, "emails_scraped_labeled.csv"))
    print(f"Data loaded from {dataPath}.")

    # Preprocess the text data
    # Here we use TfidfVectorizer to convert text data into TF-IDF features
    vectorizer = TfidfVectorizer(
        max_features=1000, ngram_range=(1, 2), stop_words=["german"]
    )
    df["Text"] = df["Subject"].fillna("") + " " + df["Content"].fillna("")
    X = vectorizer.fit_transform(df["Text"])
    y = df["Label"]

    # Train/Test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

    # Model Training
    model = LogisticRegression(max_iter=1000, class_weight="balanced")
    model.fit(X_train, y_train)

    # Evaluation (optional)
    # You can uncomment the following lines to evaluate the model on the test set

    # from sklearn.metrics import classification_report
    # predictions = model.predict(X_test)
    # print(predictions)
    # print(classification_report(y_test, model.predict(X_test), zero_division=0))

    # Save the model and vectorizer
    if not os.path.exists("../models"):  # You can change the path/names as needed
        os.makedirs("../models")  # You can change the path/names as needed
    joblib.dump(
        model, "../models/spam_model.pkl"
    )  # You can change the path/names as needed
    joblib.dump(
        vectorizer, "../models/vectorizer.pkl"
    )  # You can change the path/names as needed

    print(f"Model and vectorizer saved successfully.")


if __name__ == "__main__":
    train_and_save_model()
