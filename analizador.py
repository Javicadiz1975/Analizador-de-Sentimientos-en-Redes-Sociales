from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt

# Configuración de API de Twitter (agrega tus claves)
api_key = "API_KEY"
api_key_secret = "API_KEY_SECRET"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = api.search("Python", count=50)
sentimientos = {"Positivo": 0, "Negativo": 0, "Neutral": 0}

for tweet in tweets:
    blob = TextBlob(tweet.text)
    if blob.sentiment.polarity > 0:
        sentimientos["Positivo"] += 1
    elif blob.sentiment.polarity < 0:
        sentimientos["Negativo"] += 1
    else:
        sentimientos["Neutral"] += 1

plt.bar(sentimientos.keys(), sentimientos.values(), color=["green", "red", "gray"])
plt.title("Análisis de Sentimientos")
plt.show()
