# import pandas as pd
# from textblob import TextBlob

# # Load the CSV file into a DataFrame
# csv_file_path = "C:/Users/rishi/OneDrive/Desktop/Personal/Internship/Twitter_Data_Sample.csv"  # Replace with the path to your CSV file
# df = pd.read_csv(csv_file_path)

# # Define a function to perform sentiment analysis and segregate words using TextBlob
# def analyze_sentiment_and_segregate_words(text):
#     analysis = TextBlob(str(text))
    
#     # Separate words into positive, negative, and neutral lists
#     positive_words = [word for word, pol in zip(analysis.words, analysis.sentences[0].polarity) if pol > 0]
#     negative_words = [word for word, pol in zip(analysis.words, analysis.sentences[0].polarity) if pol < 0]
#     neutral_words = [word for word, pol in zip(analysis.words, analysis.sentences[0].polarity) if pol == 0]

#     return ' '.join(positive_words), ' '.join(negative_words), ' '.join(neutral_words)

# # Apply sentiment analysis and word segregation to the 'text' column
# df[['positive_words', 'negative_words', 'neutral_words']] = df['clean_text'].apply(analyze_sentiment_and_segregate_words)

# # Save the updated DataFrame to a new CSV file
# output_csv_path = 'C:/Users/rishi/OneDrive/Desktop/Personal/Internship/sentiment_results.csv'  # Replace with your desired output file path
# df.to_csv(output_csv_path, index=False)

# print(f"Sentiment and words segregation results saved to {output_csv_path}")

import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
csv_file_path = "C:/Users/rishi/OneDrive/Desktop/Personal/Internship/Twitter_Data_Sample.csv"  # Replace with the path to your CSV file
df = pd.read_csv(csv_file_path)

# Define a function to perform sentiment analysis using TextBlob
def analyze_sentiment(text):
    analysis = TextBlob(str(text))
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    return polarity, subjectivity


# Apply sentiment analysis to the 'text' column and create a new 'sentiment' column
df['polarity'], df['subjectivity'] = zip(*df['clean_text'].apply(analyze_sentiment))  # Replace 'text_column_name' with your column name

def categorize_sentiment(polarity):
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'
df['sentiment'] = df['polarity'].apply(categorize_sentiment)
sentiment_counts = df['sentiment'].value_counts(normalize=True) * 100

# Plot the percentage of positive, negative, and neutral sentiments
plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'])
plt.title('Sentiment Analysis Results')
plt.xlabel('Sentiment')
plt.ylabel('Percentage')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# Save the updated DataFrame to a new CSV file
output_csv_path = 'C:/Users/rishi/OneDrive/Desktop/Personal/Internship/sentiment_analysis_results.csv'  # Replace with your desired output file path
df.to_csv(output_csv_path, index=False)

print(f"Sentiment analysis results saved to {output_csv_path}")
