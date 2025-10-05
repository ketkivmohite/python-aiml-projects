
# Sentiment Analyzer with Python and TextBlob

A simple Python program that analyzes the sentiment of user-entered sentences using the TextBlob library. It classifies text as positive, negative, or neutral based on a polarity score.

## Features

- Uses TextBlob's built-in sentiment analysis capabilities
- Classifies sentences into three sentiment categories: Positive, Negative, Neutral
- Interactive command-line interface for user input
- Easy to use and beginner-friendly NLP project


## How It Works

- The program accepts English sentences from the user
- TextBlob processes the sentence and returns a polarity score (-1 to 1)
- Positive polarity indicates positive sentiment, negative indicates negative sentiment, and zero indicates neutral sentiment
- Results are displayed with corresponding emoji feedback


## Setup and Installation

1. Make sure you have Python 3 installed on your system.
2. Install TextBlob using pip:

```bash
pip install textblob
```

3. Download required TextBlob data:

```bash
python -m textblob.download_corpora
```

4. Run the Python script:

```bash
python sentiment_analyzer.py
```


## Usage

- Run the script `sentiment_analyzer.py`
- Enter any sentence and press Enter
- View the sentiment result (Positive, Negative, Neutral)
- Type `exit` to quit the program


## Example

```
Enter a sentence: I love learning Python!
Sentiment: Positive 

Enter a sentence: The weather is terrible today.
Sentiment: Negative 

Enter a sentence: The book is on the table.
Sentiment: Neutral 
```


## Learnings

- Basic natural language processing with TextBlob
- Handling user input in Python
- Sentiment analysis concepts and polarity scoring
- Building interactive command-line tools



This project is for educational purposes. Feel free to use, share, and modify with credit.

***

Feel free to ask for a custom version or help with formatting for GitHub!
