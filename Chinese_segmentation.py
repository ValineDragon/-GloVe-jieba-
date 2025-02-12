import numpy as np
import pandas as pd
import jieba
import re
import os
from tqdm import tqdm
# import mxnet
import requests

if not os.path.exists('stopWord.json'):
    stopWord = requests.get("https://raw.githubusercontent.com/goto456/stopwords/master/cn_stopwords.txt")
    with open("stopWord.json","w") as f:
        f.write(stopWord.content)

with open("stopWord.json","r",encoding='utf-8') as f:
    stopWords = f.read().split("\n")  

def do_segment(text):
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9\s]', '', text)
    words = jieba.cut(text)
    filtered_words = [word for word in words if word not in stopWords]
    return ' '.join(filtered_words)

with open('text8_BefSeg', 'r', encoding='utf-8') as f:
    content = f.read()

segmented_content = do_segment(content)

with open('text8', 'w', encoding='utf-8') as f:
    f.write(segmented_content)