import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

def get_sentiment(text: str):
    """Return the polarity score of a text using TextBlob."""
    blob = TextBlob(text)
    return blob.sentiment.polarity

def classify_sentiment(score: float) -> str:
    """Classify sentiment based on polarity score."""
    if score > 0:
        return 'Positive'
    elif score < 0:
        return 'Negative'
    return 'Neutral'

def main():
    print("=== Customer Feedback Sentiment Analyzer ===")
    print("Type customer feedback below. Type 'done' when finished.\n")

    feedback_list = []

    while True:
        feedback = input("Feedback: ")
        if feedback.lower() == "done":
            break
        feedback_list.append(feedback)

    if not feedback_list:
        print("No feedback entered. Exiting.")
        return

    # Create dataframe
    data = pd.DataFrame(feedback_list, columns=['feedback'])
    data['feedback'] = data['feedback'].str.lower()

    # Analyze sentiment
    data['sentiment_score'] = data['feedback'].apply(get_sentiment)
    data['sentiment_category'] = data['sentiment_score'].apply(classify_sentiment)

    # Count categories
    counts = data['sentiment_category'].value_counts()

    # Plot results
    plt.figure(figsize=(8, 6))
    counts.plot(kind='bar')
    plt.title("Customer Feedback Sentiment Analysis")
    plt.xlabel("Sentiment Category")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

    print("\n=== Analysis Results ===")
    print(data)

if __name__ == "__main__":
    main()
