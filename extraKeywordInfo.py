import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random
import os
import re

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

rootdir = './'
regex = re.compile('(.*key.json$)')
for root, dirs, files in os.walk(rootdir):
  for file in files:
    if regex.match(file):
       # print (file)
        name=file
        saveAs=name.replace('key.json','image.png')

        
        with open(name) as f:
          data = json.load(f)
        words=""
        for i in range(len(data)):
            next=(data[i]['extractions'])
            for x in range(len(next)):
                if (float(next[x]['relevance'])>0.6):
                    words+=" "+(next[x]['parsed_value'])
        text=words
        wordcloud = WordCloud(width=1200, height=800, margin=0).generate(text)
        plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3),interpolation="bilinear")
        plt.axis("off")
        plt.margins(x=0, y=0)
        plt.savefig(saveAs,bbox_inches='tight')


        
