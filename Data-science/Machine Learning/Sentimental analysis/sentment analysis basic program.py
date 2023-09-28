import numpy as np
import pandas as pd

sentiment_dict = {
    'positive': ['love', 'amazing', 'great', 'awesome'],
    'negative': ['hate', 'terrible', 'awful', 'horrible']
}

text = input("comment")

words = text.lower().split()

positive_count = 0
negative_count = 0

for word in words:
    if word in sentiment_dict['positive']:
        positive_count += 1
    elif word in sentiment_dict['negative']:
        negative_count += 1

if positive_count > negative_count:
    sentiment = "positive"
elif negative_count > positive_count:
    sentiment = "negative"
else:
    sentiment = "neutral"

print(f"Text: {text}")
print(f"Sentiment: {sentiment}")