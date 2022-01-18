
#Import libraries required 

#For Twitter scraping, we used a scraper called snscrape - for more information, visit https://github.com/JustAnotherArchivist/snscrape)

#We wrote each president's tweets and related features into separate files. 

import snscrape.modules.twitter as sntwitter

import pandas as pd

import codecs, io


# BIDEN'S TWEETS #

#Create an empty list for the scraping loop

tweets_list = []

#Scrape Twitter for Biden's tweets and their engagement features (the number of likes, retweets, replies) and add them to the empty list created above 

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:@JoeBiden + since:2021-01-01 until:2022-01-01').get_items()):

    tweet_list = [tweet.content, tweet.username, tweet.date, tweet.likeCount,tweet.retweetCount,tweet.replyCount]

    tweets_list.append(tweet_list)

#Turn the list created into a dataframe and concatenated it

tweets_df_Biden = pd.DataFrame(tweets_list)

ToB = pd.concat([tweets_df_Biden])

#Name the columns of the file that will be created, i.e. creating a header

ToB = ToB.rename(columns={0: 'Text', 1: 'User', 2: "Date", 3: "Favs", 4: "Retweets",5: "Replies"})

#Write the Pandas object (dataframe) to a comma-separated values (csv) file in utf-8 encoding - Do not forget to change the path of your file. Make sure that you use an absolute path.

ToB.to_csv('/Users/serimtarcan/Desktop/TwitterProject/GitHubRepo/Output/tweets_Biden.csv', encoding ='utf-8')


# OBRADOR'S TWEETS #

#Create an empty list for the scraping loop

tweets_list = []

#Scrape Twitter for Obrador's tweets and their engagement features (the number of likes, retweets, replies) and add them to the empty list created above 

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:@lopezobrador_ + since:2021-01-01 until:2022-01-01').get_items()):

    tweet_list = [tweet.content, tweet.username, tweet.date, tweet.likeCount,tweet.retweetCount,tweet.replyCount]

    tweets_list.append(tweet_list)

#Turn the list created into a dataframe and concatenated it

tweets_df_AMLO = pd.DataFrame(tweets_list)

ToA = pd.concat([tweets_df_AMLO])

#Name the columns of the file that will be created, i.e. creating a header

ToA = ToA.rename(columns={0: 'Text', 1: 'User', 2: "Date", 3: "Favs", 4: "Retweets",5: "Replies"})

#Write the Pandas object (dataframe) to a comma-separated values (csv) file in utf-8 encoding - Do not forget to change the path of your file. Make sure that you use an absolute path.

ToA.to_csv('/Users/serimtarcan/Desktop/TwitterProject/GitHubRepo/Output/tweets_AMLO.csv', encoding ='utf-8')


# MODI'S TWEETS #

#Create an empty list for the scraping loop

tweets_list = []

#Scrape Twitter for Modi's tweets and their engagement features (the number of likes, retweets, replies) and add them to the empty list created above 

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:@narendramodi + since:2021-01-01 until:2022-01-01').get_items()):

    tweet_list = [tweet.content, tweet.username, tweet.date, tweet.likeCount,tweet.retweetCount,tweet.replyCount]

    tweets_list.append(tweet_list)

#Turn the list created into a dataframe and concatenated it

tweets_df_Modi = pd.DataFrame(tweets_list)

ToM = pd.concat([tweets_df_Modi])

#Name the columns of the file that will be created, i.e. creating a header

ToM = ToM.rename(columns={0: 'Text', 1: 'User', 2: "Date", 3: "Favs", 4: "Retweets",5: "Replies"})

#Write the Pandas object (dataframe) to a comma-separated values (csv) file in utf-8 encoding - Do not forget to change the path of your file. Make sure that you use an absolute path.

ToM.to_csv('/Users/serimtarcan/Desktop/TwitterProject/GitHubRepo/Output/tweets_Modi.csv', encoding ='utf-8')


# ERDOGAN'S TWEETS #

#Create an empty list for the scraping loop

tweets_list = []

#Scrape Twitter for Erdogan's tweets and their engagement features (the number of likes, retweets, replies) and add them to the empty list created above 

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:@RTErdogan + since:2021-01-01 until:2022-01-01').get_items()):

    tweet_list = [tweet.content, tweet.username, tweet.date, tweet.likeCount,tweet.retweetCount,tweet.replyCount]

    tweets_list.append(tweet_list)

#Turn the list created into a dataframe and concatenated it

tweets_df_Erdogan = pd.DataFrame(tweets_list)

ToE = pd.concat([tweets_df_Erdogan])

#Name the columns of the file that will be created, i.e. creating a header

ToE = ToE.rename(columns={0: 'Text', 1: 'User', 2: "Date", 3: "Favs", 4: "Retweets",5: "Replies"})

#Write the Pandas object (dataframe) to a comma-separated values (csv) file in utf-8 encoding - Do not forget to change the path of your file. Make sure that you use an absolute path.

ToE.to_csv('/Users/serimtarcan/Desktop/TwitterProject/GitHubRepo/Output/tweets_Erdogan.csv', encoding ='utf-8')
