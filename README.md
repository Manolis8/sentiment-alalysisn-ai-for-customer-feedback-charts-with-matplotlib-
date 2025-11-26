Customer Feedback Sentiment Analysis

This project is a small Python tool for collecting customer feedback and analyzing its sentiment using TextBlob. It classifies each response as positive, negative, or neutral, and generates a simple bar chart to show the distribution. It's a straightforward way to explore basic NLP and data visualization.

Features

Collects feedback interactively from the user

Cleans and processes the text

Uses TextBlob for sentiment scoring

Classifies feedback into three categories: Positive, Negative, Neutral

Displays a bar chart of sentiment distribution

Prints the results in a clean table format

Project Structure
customer-feedback-sentiment-analysis/
│
├──sentiment_analysis.py
├── requirements.txt
└── README.md

Installation

Clone the repository:

https://github.com/Manolis8/sentiment-alalysisn-ai-for-customer-feedback-charts-with-matplotlib-.git
cd sentiment-alalysisn-ai-for-customer-feedback-charts-with-matplotlib-


Install the dependencies:

pip install -r requirements.txt

Usage

Run the script:

python src/sentiment_analysis.py


Enter feedback line by line, then type:

done


to finish and see the analysis.

Example Output
feedback                sentiment_score    sentiment_category
------------------------------------------------------------
love this product!           0.50              Positive
terrible experience          -1.00             Negative
it was okay                   0.00             Neutral

Visualization

Once the analysis finishes, the script generates a bar chart showing how many responses were positive, negative, or neutral.
