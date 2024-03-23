from bs4 import BeautifulSoup
from transformers import pipeline

def get_text_from_html(html_file_path):
    with open(html_file_path, 'r', encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    text = soup.get_text(separator='\n')
    lines = text.split('\n')
    sentences = [line for line in lines if line.strip()]

    cleaned_text = ' '.join(sentences)
    return cleaned_text

html_file_path = "index6.html"
html_text = get_text_from_html(html_file_path)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summary = summarizer(html_text, max_length=130, min_length=30)
print("Generated Summary:")
print(summary)


