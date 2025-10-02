import pandas as pd
import re
import string
from nltk.corpus import stopwords
import nltk

# Download stopwords if not already done
nltk.download('stopwords')

# Initialize stopwords and punctuation sets
stop_words = set(stopwords.words('english'))

# Add custom stopwords to filter out common URL and irrelevant tokens
custom_stopwords = {'https', 'com', 'www', 'id', 'p', 'f', 'mail', 'google'}
stop_words.update(custom_stopwords)

punctuations = set(string.punctuation)

def preprocess_text(text):
    # Convert text to lowercase string
    text = str(text).lower()
    # Extract words consisting of alphabets only
    tokens = re.findall(r'\b[a-z]+\b', text)
    # Remove stopwords and punctuation
    filtered_tokens = [word for word in tokens if word not in stop_words and word not in punctuations]
    return filtered_tokens

# Load browser history from CSV file
history_df = pd.read_csv('browser_history.csv')

# Use page titles only for keyword extraction (more meaningful than URLs)
history_df['text'] = history_df['title'].astype(str)

# Apply preprocessing to extract tokens from each title
history_df['tokens'] = history_df['text'].apply(preprocess_text)

# Flatten list of all tokens from all rows for frequency counting
all_tokens = [token for tokens_list in history_df['tokens'] for token in tokens_list]

# Calculate frequency distribution of tokens
freq_dist = nltk.FreqDist(all_tokens)

# Print top 20 most common keywords with counts
print(freq_dist.most_common(20))

# Basic manual mapping from keywords to career paths
career_map = {
    'flutterflow': 'Mobile App Developer',
    'node': 'Backend Developer',
    'design': 'UX/UI Designer',
    'figma': 'UX/UI Designer',
    'learning': 'Lifelong Learner',
    'bharatnatyam': 'Classical Dancer',
    'youtube': 'Content Creator',
    'basics': 'Entry-level Job Seeker'
}

# Collect top 50 keywords
top_keywords = [word for word, freq in freq_dist.most_common(50)]

# Find matching careers based on extracted keywords
matched_careers = set()
for keyword in top_keywords:
    if keyword in career_map:
        matched_careers.add(career_map[keyword])

# Print suggested career paths
print("\nSuggested career paths based on your interests:")
for career in matched_careers:
    print("- " + career)
