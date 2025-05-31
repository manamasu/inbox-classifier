# 📥 inbox-classifier

**inbox-classifier** is an email sorting tool that uses **machine learning** to classify Outlook Emails and move them into custom folders. It works via Outlook’s COM interface, leveraging *Logistic Regression* to detect categories like spam, job applications and more if needed.

---

## Checklist/Goals

- [x] Scrape emails from Outlook via COM  
  - [x] Extract relevant information/metadata (subject, sender, etc.)
  - [x] Clean text content (remove weird junk)
  - [x] Extract raw links and domains (deduplicated)
- [x] Save scraped emails to CSV for labeling
- [x] Train Logistic Regression model on labeled email content  
- [x] Automatically move predicted emails to corresponding subfolders (e.g. `Spam_pred`, `Job_pred` in Outlook)  
- [ ] Support multiple machine learning models (Optional)
- [ ] Integrate Microsoft Graph API fallback for Outlook Web/Modern clients (Optional)  
- [ ] Add automatic model retraining on updated labels (Optional)
- [ ] Build user-friendly interface for labeling and sorting (Optional)

---

## Setup

1. Clone the Repoistory

   ```bash
    git clone https://github.com/yourusername/inbox-classifier.git
    cd inbox-classifier
   ```

2. Set up your virtual Environment

   ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    pip install -r requirements.txt
   ```

---

## How to Use

### Step 1: Scrape Emails to CSV

First we want to scrape the emails, you can change the max_size in the files.

Start the script, depending on your version:

```py src/scrape_emails.py``` OR ```python src/scrape_emails.py```

### Step 2: Manually label your Data

You can now copy your generated csv file from Step 1. and name the copy e.g, `emails_scraped_labeled.csv`

Now label your data manually with either `spam` or `ham`.

Note: (50-100) should be enough, but you can try it out yourself and explore what works best for you.
  
### Step 3: Train your Model

Note: This creates the model under the models folder, you can change parameters according to your needs.

```py src/train_model.py``` OR ```python src/train_model.py```

### Step 4: Classify and Sort Emails Automatically

Now you can classify and move your emails, after training.

```py src/classify_and_move_emails.py``` OR ```python src/classify_and_move_emails.py```
