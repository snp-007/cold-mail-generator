import re


def clean_text(text):
    """
    Clean scraped webpage text while preserving
    technical terms and job-related information.
    """

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)

    # Remove excessive whitespace/newlines
    text = re.sub(r"\s+", " ", text)

    # Remove strange unicode characters
    text = re.sub(r"[\u200b-\u200f\u202a-\u202e]", "", text)

    return text.strip()