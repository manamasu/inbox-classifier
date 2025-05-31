import os
import pandas as pd
from email_utils import fetch_emails


def scrape_emails_to_csv(max_emails):
    # We use list() to collect all yielded items into a list
    # otherwise it will be a generator which cannot be directly converted to a DataFrame.
    data = list(fetch_emails(max_emails))
    if not data:
        print("No emails found.")
        return
    df = pd.DataFrame(data)
    if "msg_obj" in df.columns:
        del df[
            "msg_obj"
        ]  # safety measure if msg_obj exists. Avoids potential issues with CSV

    # Ensure the data directory exists and save the DataFrame to a CSV file
    baseDir = os.path.dirname(os.path.abspath(__file__))
    dataDir = os.path.join(baseDir, "..", "data")
    if not os.path.exists(dataDir):
        os.makedirs(dataDir)  # Create data directory if it doesn't exist
    df.to_csv(os.path.join(dataDir, "emails_scraped.csv"), index=False)
    print(f"Saved {len(df)} emails to 'emails_scraped.csv'.")


if __name__ == "__main__":
    scrape_emails_to_csv(max_emails=100)  # Adjust max_emails as needed
