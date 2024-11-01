# utils/text_cleaner.py
import re

def clean_text(text):
    # Remove excessive newlines, spaces, and HTML artifacts
    text = re.sub(r'\n+', '\n', text)  
    text = re.sub(r'\s{2,}', ' ', text)  
    return text.strip()
