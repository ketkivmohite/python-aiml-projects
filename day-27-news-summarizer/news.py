import requests
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# List of available categories
categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]

# Ask user for desired news category
print("Available categories:", ", ".join(categories))
category = input("Enter the category you want news for: ").strip().lower()
if category not in categories:
    print("Invalid category, using 'general' by default.")
    category = "general"

url = f"https://saurav.tech/NewsAPI/top-headlines/category/{category}/in.json"
response = requests.get(url)
data = response.json()

articles = data['articles']
print(f"Number of articles fetched: {len(articles)}")

for article in articles:
    title = article['title']
    content = article.get('content') or article.get('description') or ""
    print(f"\nTitle: {title}")
    print("Summary:")
    if content.strip():
        parser = PlaintextParser.from_string(content, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, 2)
        for sentence in summary:
            print(sentence)
    else:
        print("No summary available for this article.")
