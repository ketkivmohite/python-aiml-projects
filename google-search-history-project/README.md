# Project: Career Guidance AI Agent from Browser History

## Overview
This project is a simple AI-powered tool that extracts your browsing history, analyzes it to identify your interests, and suggests possible career paths based on those interests. It consists of two Python scripts:

- `history_extract.py`: Extracts browsing history from your installed browsers and saves it to a CSV file.
- `keyword_extraction.py`: Reads the saved browsing history, processes page titles to extract meaningful keywords, and maps those keywords to suggested career paths.

## Features
- Automatically extracts browsing history including timestamps, URLs, and page titles.
- Cleans and processes browsing titles to extract relevant keywords.
- Filters out common stopwords and irrelevant tokens.
- Counts keyword frequency to identify main interests.
- Suggests careers based on keyword-to-career mapping.

## Requirements
- Python 3.6 or above
- Packages:
  - `pandas`
  - `nltk`
  - `browser-history`

You can install the required packages using pip:

```bash
pip install pandas nltk browser-history
```

## Usage

### 1. Extract Browsing History

Run the `history_extract.py` script to generate your browsing history CSV file:

```bash
python history_extract.py
```

This creates a `browser_history.csv` file in the project directory containing your browsing history data.

### 2. Extract Keywords and Get Career Suggestions

Run the `keyword_extraction.py` script to analyze the browsing history, extract keywords, and print suggested career paths:

```bash
python keyword_extraction.py
```

You will see output listing the most frequent keywords from your browsing titles and recommended career options based on those keywords.

## Code Structure

### `history_extract.py`:
- Uses the `browser_history` package to fetch browsing history.
- Creates a pandas DataFrame with columns: `timestamp`, `url`, and `title`.
- Saves the data to `browser_history.csv`.

### `keyword_extraction.py`:
- Reads the saved CSV file.
- Preprocesses page titles by:
  - Converting to lowercase.
  - Tokenizing words using regex.
  - Filtering out stopwords and punctuation.
  - Removing common URL tokens like "https", "com", "www".
- Counts the frequency of remaining keywords.
- Maps keywords to a basic career dictionary.
- Outputs the top keywords and suggested career paths.

## Sample Output

```
[('youtube', 30082), ('figma', 20411), ('flutterflow', 4762), ... ]

Suggested career paths based on your interests:
- UX/UI Designer
- Mobile App Developer
- Content Creator
- Lifelong Learner
- Classical Dancer
- Entry-level Job Seeker
```

## Next Steps
To evolve this into a full AI agent:
- Add a user-friendly interactive interface (e.g., using Streamlit).
- Automate browsing history extraction regularly.
- Implement natural language interaction via chatbot.
- Enhance career mappings and incorporate machine learning for better recommendations.

***

Feel free to contribute or reach out for help in extending this project!