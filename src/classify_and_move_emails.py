import pandas as pd
from email_utils import fetch_emails
from helper import get_or_create_subfolder
import win32com.client
import datetime

from spam_classifier import load_model, predict_label


def classify_and_move_emails(max_emails, output_csv):
    model = load_model()  # Load the pre-trained model and vectorizer

    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # Inbox
    spam_folder = get_or_create_subfolder(inbox, "Spam_pred")
    job_folder = get_or_create_subfolder(inbox, "Job_pred")

    classified_data = []
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for email in fetch_emails(max_emails=max_emails, include_msg_obj=True):
        # Extracting necessary fields from the email
        content = email["Content"]
        subject = email["Subject"]
        msg = email["msg_obj"]

        # Predicting the label using the pre-trained model
        prediction = predict_label(model, subject, content)

        email["Timestamp"] = timestamp  # Add TimeStamp, time when email was classified
        email["Label"] = prediction  # Add prediction label to the email data

        try:
            if prediction == "spam":
                msg.Move(spam_folder)
            else:
                msg.Move(job_folder)
        except Exception as move_error:
            print(f"Failed to move email: {move_error}")

        # Now removing msg_obj so we can safely save to CSV without issues
        del email["msg_obj"]
        classified_data.append(email)

    # Save classification results to a CSV file
    df = pd.DataFrame(classified_data)
    df.to_csv(output_csv, index=False)
    print(f"Classified and moved {len(df)} emails. Saved to '{output_csv}'.")


if __name__ == "__main__":
    classify_and_move_emails(max_emails=30, output_csv="emails_classified.csv")
