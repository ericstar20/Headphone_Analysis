# Reference
# sentiment: https://textblob.readthedocs.io/en/dev/
# visualize: https://stackabuse.com/python-for-nlp-sentiment-analysis-with-scikit-learn/

from textblob import TextBlob
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import review dataset
df = pd.read_csv("/Applications/SW_PRO/Personal Projects/Headphone coparison/bose_n700/n700.csv")
df.head()

review = df['review_text']
rscore_list = []

# analyze each review's sentiment
for sentence in review:
    blob = TextBlob(sentence)
    score  = float()
    sum_sc = float()
    for sen in blob.sentences:
        score = sen.sentiment.polarity
        sum_sc += score                 # calculate each review total sentiment score
    rscore_list.append(sum_sc)

# add the sentiment point list to original dataframe
df['sentiment_point'] = rscore_list

# assign a positive, negative or neutral
def f(row):
    if row['sentiment_point'] > 0:
        val = 'Positive'
    elif row['sentiment_point'] < 0:
        val = 'Negative'
    else:
        val = 'Neutral'
    return val
df['sentiment_status'] = df.apply (lambda row: f(row), axis=1)

print(df.head())

# data visualize
# 1. set up plot_size
plot_size = plt.rcParams["figure.figsize"]
plot_size[0] = 8
plot_size[1] = 6
plt.rcParams["figure.figsize"] = plot_size

#2. visualizing
# a). pie chart
df.sentiment_status.value_counts().plot(kind='pie', autopct='%1.0f%%', colors=["green", "red", "gray"])
plt.title('Matplot pie plot')
plt.legend(loc='top right')
plt.show()

# b). scatter char
# # Create data
#  select a column based on other column : df.loc[df['B'] == 3, 'A'].iloc[0]
g1 = tuple(df.loc[df['sentiment_status'] == 'Positive']['sentiment_point'])
g2 = tuple(df.loc[df['sentiment_status'] == 'Neutral']['sentiment_point'])
g3 = tuple(df.loc[df['sentiment_status'] == 'Negative']['sentiment_point'])
data = (g1, g2, g3)
print(type(g1))
colors = ("green", "gray", "red")
groups = ("Positive", "Neutral", "Negative")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, facecolor="1.0")
for data, color, group in zip(data, colors, groups):
    y = range(0,len(data))
    x = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=50, label=group)

plt.title('Matplot scatter plot')
plt.legend(loc='center right', bbox_to_anchor=(1.0, 0.5))
plt.show()

# c). line graph
df_c = df.sort_values(by=['sentiment_point'])
y = df_c['sentiment_point']
x = range(0,len(df))
plt.plot(x,y)
plt.title('Matplot Line plot')
plt.legend(loc='top left')
plt.show()
