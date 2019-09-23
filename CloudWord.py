import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("/Applications/詩典修煉手冊/Personal Projects/Headphone coparison/bose_n700/n700.csv")
df.head()
print("There are {} observations and {} features in this dataset. \n".format(df.shape[0],df.shape[1]))

# You can try to play with this dataframe
df[["review_header", "review_text", "review_rating", "review_posted_date"]].head()

# Create the wordcloud
#?WordCloud

# Start with one review:
text = df.review_text[0]

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# lower max_font_size, change the maximum number of word and lighten the background:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
wordcloud.to_file("/Applications/詩典修煉手冊/Personal Projects/Headphone coparison/bose_n700/first_review.png")

# To create whole review's cloudword
text = " ".join(review for review in df.review_text)
print ("There are {} words in the combination of all review.".format(len(text)))

# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(["BOSE", "bose", "n700", "700", "headphone", "headphones", "qc35", "sony"])

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
wordcloud.to_file("/Applications/詩典修煉手冊/Personal Projects/Headphone coparison/bose_n700/All_review.png")
