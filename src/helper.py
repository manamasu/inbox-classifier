import re


"""Extract links and domains from text.
This function finds all URLs in the text and extracts their base domains."""


def extract_links(text):

    if not text:
        return [], []

    # Extract all full URLS
    raw_links = re.findall(r"(https?://[^\s]+|www\.[^\s]+)", text, flags=re.IGNORECASE)

    # Extract base domains (like 'google.com')
    domains = re.findall(
        r"\b(?:https?://|www\.)?([\w.-]+\.(?:com|de|net|org|edu))\b",
        " ".join(raw_links),
        flags=re.IGNORECASE,
    )

    # Remove duplicates from domains while preserving original case
    seen_domains = set()
    unique_domains = []
    for domain in domains:
        d_lower = domain.lower()
        if d_lower not in seen_domains:
            seen_domains.add(d_lower)
            unique_domains.append(domain)

    return raw_links, unique_domains


"""Clean and normalize text by removing URLs and junk patterns."""


def clean_text(text):
    if not text:
        return ""

    text = text.lower()

    # Remove all URLs from content
    cleaned_text = re.sub(
        r"(https?://|www\.)[\w./#?&=%-]+", "", text, flags=re.IGNORECASE
    )

    # Clean out junk patterns
    cleaned_text = re.sub(r"<~~.*?~~>", "", cleaned_text)
    cleaned_text = re.sub(r"~~.*?~~", "", cleaned_text)
    cleaned_text = re.sub(r"~{1,}", "", cleaned_text)
    cleaned_text = re.sub(r"<[^>]+>", "", cleaned_text)

    # Normalize whitespace
    cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()

    return cleaned_text


def get_or_create_subfolder(parent_folder, subfolder_name):
    try:
        return parent_folder.Folders[subfolder_name]
    except Exception:
        return parent_folder.Folders.Add(subfolder_name)
