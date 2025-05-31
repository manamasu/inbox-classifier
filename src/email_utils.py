import win32com.client
from helper import clean_text, extract_links


# This script scrapes emails from the Outlook inbox and saves them to a CSV file.
# It extracts the subject, sender, received time, and content of each email.
def fetch_emails(max_emails, include_msg_obj=False):
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    # reference to InboxFolder (6), see for more https://learn.microsoft.com/en-us/office/vba/api/outlook.oldefaultfolders
    inbox = outlook.GetDefaultFolder(6)
    messages = (
        inbox.Items
    )  # inbox.Items return the Items of a Folder object, see https://learn.microsoft.com/en-us/office/vba/api/outlook.items
    messages.Sort("[ReceivedTime]", True)
    # messages = messages.Restrict("[UnRead] = True")  # (Optional)

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

            email_data = {
                "msg_obj": msg,
                "Subject": subject,
                "From": sender,
                "Received": received,
                "Domains": "; ".join(domains),
                "Content": content,
                "RawLinks": "; ".join(links),
                "Label": "",  # <- Placeholder for manual labeling
            }

            if include_msg_obj:
                email_data["msg_obj"] = msg

            yield email_data

            count += 1
            if count >= max_emails:
                break

        except Exception as e:
            print("Error reading message:", e)
            continue
