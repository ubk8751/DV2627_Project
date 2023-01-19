import os

import feedparser
import cv2
import requests
import json
from PIL import Image

img = cv2.imread("img/monke.jpg", 1)

feed = feedparser.parse("https://www.reddit.com/r/me_irl/hot/.rss")

def get_keys(image_url):
    try:
        
        url = 'https://dv1615-apimanagement-lab.azure-api.net/vision/v2.0/analyze?visualFeatures=Tags'
        body = {'url':image_url}
        headers = {'Ocp-Apim-Subscription-Key': '6af7226881af4bf4a83ccd810023a5a0'}
        response = requests.post(url, headers = headers, json = body).json()
        items = []
        print(response)
        if 'code' in response or 'statusCode' in response:
            return None, response['message']

        for item in response["tags"]:
            if item['confidence'] >= 0.99:
                items.append(item["name"])

        if len(items) < 1:
           return None, "There is no 99% answer."

        return items, ""

    except:
        return None, "API Management layer URL is invalid"

def translate(items):
    try:
        url = "https://dv1615-apimanagement-lab.azure-api.net/translate?api-version=3.0&from=en&to=sv"
        
        headers = {'Ocp-Apim-Subscription-Key': '6af7226881af4bf4a83ccd810023a5a0'}

        body = body = [{"text": item} for item in items]
        
        response = requests.post(url, headers=headers, json=body).json()
        
        translations = []

        for item in response:
            for translation in item['translations']:
                translations.append(translation['text'])
        
        return translations
        
    except:
        return None
path = os.getcwd() + "\\img" #monke.jpg"
for f in os.listdir(path):
    #print(f)
    ext = os.path.splitext(f)[1]
    image = Image.open(os.path.join(path,f))
keys = get_keys(image)
#t = translate(keys)
print(keys)