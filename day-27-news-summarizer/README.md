# News Summarizer

A simple Python application that fetches the latest Indian news headlines and automatically summarizes the articles using Natural Language Processing (NLP).

## Features

- Fetches live news headlines from India across multiple categories.
- Summarizes each news article to provide concise information.
- Allows filtering news by categories such as business, sports, technology, entertainment, and more.
- Handles missing data and errors gracefully.

## Technologies Used

- Python 3
- `requests` library for HTTP requests
- `sumy` library for text summarization
- Public free API endpoint for Indian news (no API key required)

## Installation

1. Clone this repository or download the code.
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
   Alternatively, install manually:
   ```
   pip install requests sumy
   ```

## Usage

1. Run the Python script:
   ```
   python news.py
   ```
2. When prompted, enter a news category:
   - business
   - entertainment
   - general
   - health
   - science
   - sports
   - technology
3. The script will fetch recent news from the specified category and display a short summary of each article.

## Example

```
Available categories: business, entertainment, general, health, science, sports, technology
Enter the category you want news for: sports

Number of articles fetched: 20

Title: Pakistan vs England 3rd Test: How Haris Rauf and Naseem Shah crushed England batting lineup
Summary:
Haris Rauf and Naseem Shah starred in Pakistan’s stunning victory against England, decimating the English batting lineup.
…

Title: Indian Premier League update: Chennai Super Kings secure a crucial win
Summary:
Chennai Super Kings ended their match with a remarkable performance highlighted by strong batting and bowling.
…
```

## Notes

- The project uses a public free API endpoint from [Saurav.tech](https://saurav.tech/NewsAPI/) for Indian news headlines — no API key is needed.
- Summarization is done using the Latent Semantic Analysis (LSA) algorithm via the `sumy` library.
- Error handling has been implemented to ensure graceful failure in case of network or data errors.

## License

This project is open source and free to use for educational purposes.

---
