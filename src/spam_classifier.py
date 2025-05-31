import joblib
import os

""""This module provides functionality to load a pre-trained spam classification model and vectorizer,"""


def load_model():
    try:
        # Define the paths to the model and vectorizer files
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(
            base_dir, "..", "models", "spam_model.pkl"
        )  # You can change the path/names as needed, but the name should match the one used in train_model.py
        vectorizer_path = os.path.join(
            base_dir, "..", "models", "vectorizer.pkl"
        )  # You can change the path/names as needed, but the name should match the one used in train_model.py

        # Check if the model and vectorizer files exist
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        if not os.path.exists(vectorizer_path):
            raise FileNotFoundError(f"Vectorizer file not found: {vectorizer_path}")

        # Load the model and vectorizer using joblib
        model = joblib.load(model_path)
        vectorizer = joblib.load(vectorizer_path)
        print(f"Model loaded successfully from {model_path}.")
        print(f"Vectorizer loaded successfully from {vectorizer_path}.")
        return model, vectorizer
    except Exception as e:
        print(f"Error loading model or vectorizer: {e}")
        raise


"""Predicts the label of an email based on its subject and content using the pre-trained model and vectorizer."""


def predict_label(model_bundle, subject, content):
    model, vectorizer = model_bundle  # unpacking, contains both model and vectorizer
    full_text = f"{subject} {content}"  # concatenate subject and content for prediction
    X = vectorizer.transform(
        [full_text]
    )  # Transforming the text using the vectorizer transform method
    prediction = model.predict(X)[
        0
    ]  # Get the prediction result, [0] to get the first element since predict returns an array
    return prediction  # Retunrs the predicted label (spam or job)
