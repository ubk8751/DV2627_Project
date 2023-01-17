import os

import feedparser
import cv2

img = cv2.imread("img/monke.jpg", 1)

feed = feedparser.parse("https://www.reddit.com/r/me_irl/hot/.rss")


print(img.shape)