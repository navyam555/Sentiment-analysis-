from transformers import pipeline

model = pipeline("sentiment-analysis")

def get_sentiment(text):
    return model(text)[0]['label']