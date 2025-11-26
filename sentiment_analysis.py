import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Create an empty list to store feedback
feedback_list = []

# Ask for user input until they decide to stop
while True:
    feedback = input("Enter customer feedback (or type 'done' to finish): ")
    if feedback.lower() == 'done':
        break
    feedback_list.append(feedback)

# Create a DataFrame from the feedback list
data = pd.DataFrame(feedback_list, columns=['feedback'])

# Clean the feedback data
data['feedback'] = data['feedback'].str.lower()

# Define sentiment analysis and classification functions
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def classify_sentiment(score):
    if score > 0:
        return 'Positive'
    elif score < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Perform sentiment analysis and classification
data['sentiment'] = data['feedback'].apply(get_sentiment)
data['sentiment_category'] = data['sentiment'].apply(classify_sentiment)

# Count the sentiment categories
sentiment_counts = data['sentiment_category'].value_counts()

# Plot the results
plt.figure(figsize=(8,6))
sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'])
plt.title('Customer Feedback Sentiment Analysis')
plt.xlabel('Sentiment Category')
plt.ylabel('Count')
plt.show()

print(data)
