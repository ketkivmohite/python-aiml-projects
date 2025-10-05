from textblob import TextBlob 
def analyze_sentiment():
    print("Python Sentiment Analyzer. Type 'exit' to quit")
    while True:
        text = input("Enter a sentence: ")
        if text.lower() == "exit":
            print("Goodbye!")
            break
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            print("Sentiment:Positive")
        elif sentiment < 0 :
            print("Sentiment: Negative")
        else:
            print("Sentiment: Neutral")
if __name__=="__main__":
    analyze_sentiment()
