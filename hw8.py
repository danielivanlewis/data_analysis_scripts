"""
Daniel Ivan Lewis
SL: Sebastian
11/01/2018
ISTA 131 Hw7
Summary: This module works with pandas, matplotlib, textblob and JSON. The module reads in json files containing tweets
pre and post Sinema McSally debate and checks the sentiment levels for each tweet which is then displayed in graph form.
"""
import pandas as pd
import numpy as np
import json
from textblob import TextBlob as tb
import matplotlib.pyplot as plt

def get_sentiment(fname):
    """
    Purpose: This function reads in tweets from a json file and returns the mean polarity level of the
    data passed in as well as the standard deviation for the given polarity levels.
    Parameters: fname - name of a json file.
    Returns: List containing 2 positions, polarity means and polarity standard deviation.
    """
    f = open(fname, 'r')
    json_data = f.read()
    all_tweets = json.loads(json_data)
    polarities = []
    for tweet in all_tweets:
        blob = tb(tweet)
        if blob.sentiment[0] != 0.0 or blob.sentiment[1] != 0.0:
            polarities.append(blob.sentiment[0])
    polarities = np.asarray(polarities)
    f.close()
    return [np.mean(polarities),np.std(polarities, ddof= 1)]

def get_ct_sentiment_frame():
    """
    Purpose: This function creates a data frame by using the get_sentiment function and 4 different
    json files, pre and post debate tweets for both Sinema and McSally.
    Parameters: NONE.
    Returns: A dataframe with the data gathered from the four json files mentioned above.
    """
    sinema = get_sentiment('sinema_tweets_run437pm.json') + get_sentiment('sinema_tweets_run949pm.json')
    mcsally = get_sentiment('mcsally_tweets_run437pm.json') + get_sentiment('mcsally_tweets_run949pm.json')
    data = [sinema,mcsally]
    return pd.DataFrame(data=data, columns=['pre_mean', 'pre_std', 'post_mean', 'post_std'], index=['Sinema','McSally'])

def make_fig(df):
    """
    Purpose: This function uses the dataframe created in the get_ct_sentiment function and displays a
    figure showing error bars and polarity levels pre and post debate for both candidates.
    Parameters: df - The data frame created in the get_ct_sentiment function.
    Returns: NONE, displays the figure created.
    """
    plt.figure(facecolor='black', figsize=(10,10))
    plt.ylabel('Sentiment', fontsize=24).set_color('red')
    plt.xticks([1.40,3.60], ['Sinema-McSally 4:37 pm', 'Sinema-McSally 9:49 pm'],fontsize=18)
    [i.set_color("red") for i in plt.gca().get_xticklabels()]
    [i.set_color("red") for i in plt.gca().get_yticklabels()]
    plt.errorbar(1,df.loc['Sinema','pre_mean'],yerr=df.loc['Sinema','pre_std'],ecolor='black',capsize=10)
    plt.bar(1,height=abs(df.loc['Sinema','pre_mean']), bottom=df.loc['Sinema','pre_mean'], color='blue')
    plt.errorbar(1.80, df.loc['McSally', 'pre_mean'], yerr=df.loc['McSally', 'pre_std'],ecolor='black',capsize=10)
    plt.bar(1.80, height=abs(df.loc['McSally', 'pre_mean']), bottom=df.loc['McSally', 'pre_mean'], color='green')
    plt.errorbar(3.20, df.loc['Sinema', 'post_mean'], yerr=df.loc['Sinema', 'post_std'],ecolor='black',capsize=10)
    plt.bar(3.20, height=abs(df.loc['Sinema', 'post_mean']), bottom=0, color='blue')
    plt.errorbar(4, df.loc['McSally', 'post_mean'], yerr=df.loc['McSally', 'post_std'],ecolor='black',capsize=10)
    plt.bar(4, height=abs(df.loc['McSally', 'post_mean']), bottom=0, color='green')
    plt.show()

def main():
    """
    Purpose: This function uses the functions mentioned above to create a data frame and creates the figure created
    in the make_fig function.
    Parameters: NONE.
    Returns: NONE, displays the figure created.
    """
    df = get_ct_sentiment_frame()
    make_fig(df)

main()