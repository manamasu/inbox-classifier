# 📥 inbox-classifier

**inbox-classifier** is an email sorting tool that uses **machine learning** to classify Outlook Emails and move them into custom folders. It works via Outlook’s COM interface, leveraging *Logistic Regression* to detect categories like spam, job applications and more if needed.

---

## Checklist/Goals

- [x] Scrape emails from Outlook via COM  
  - [ ] Remove/transform unnecessary infos/links
- [x] Save scraped emails to CSV for labeling  
- [ ] Checking Data and potentially cleaning data
- [ ] Train Logistic Regression model on labeled email content  
- [ ] Predict email categories with trained model  
- [ ] Automatically move predicted emails to corresponding subfolders (e.g. `Spam_pred`, `Job_pred` in Outlook)  
- [ ] Support multiple machine learning models  
- [ ] Integrate Microsoft Graph API fallback for Outlook Web/Modern clients (Additional Feature: Optional)  
- [ ] Add automatic model retraining on updated labels
- [ ] Build user-friendly interface for labeling and sorting

## Setup

More info coming soon
