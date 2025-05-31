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
    df.to_csv("emails_scraped.csv", index=False)
    print(f"Saved {len(df)} emails to 'emails_scraped.csv'.")


if __name__ == "__main__":
    scrape_emails_to_csv(max_emails=100)  # Adjust max_emails as needed
