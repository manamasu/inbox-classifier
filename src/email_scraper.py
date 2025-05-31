import win32com.client
import pandas as pd
from helper import clean_text, extract_links


# This script scrapes emails from the Outlook inbox and saves them to a CSV file.
# It extracts the subject, sender, received time, and content of each email.
def scrape_emails(max_emails=10):
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    # reference to InboxFolder (6), see for more https://learn.microsoft.com/en-us/office/vba/api/outlook.oldefaultfolders
    inbox = outlook.GetDefaultFolder(6)
    messages = (
        inbox.Items
    )  # inbox.Items return the Items of a Folder object, see https://learn.microsoft.com/en-us/office/vba/api/outlook.items
    messages.Sort("[ReceivedTime]", True)
    # messages = messages.Restrict("[UnRead] = True")  # (Optional)

    data = []
    count = 0

    for msg in messages:
        try:
            # Extract subject, sender, received time, and content of the email
            subject = msg.Subject or ""
            body = msg.Body or ""
            sender = msg.SenderName or ""
            received = msg.ReceivedTime or ""
            full_text = subject + "\n" + body
            content = clean_text(full_text)

            links, domains = extract_links(full_text)

            data.append(
                {
                    "Subject": subject,
                    "From": sender,
                    "Received": received,
                    "Domains": "; ".join(domains),
                    "Content": content,
                    "RawLinks": "; ".join(links),
                    "Label": "",  # <- Placeholder for labels
                }
            )

            count += 1
            if count >= max_emails:
                break

        except Exception as e:
            print("Error reading message:", e)
            continue

    # Check if any emails were found, if not then just return
    if not data:
        print("No emails found.")
        return

    # Save the scraped emails to a CSV file
    df = pd.DataFrame(data)
    df.to_csv("emails_scraped.csv", index=False)
    print(f"Saved {len(df)} emails to 'emails_scraped.csv'")


if __name__ == "__main__":
    scrape_emails()
