# Twitter-Presidents
A visualization of Twitter data from four prominent world leaders: U.S. President Joe Biden, Indian Prime Minister Narendra Modi, Turkish President Recep Tayyip Erdoğan, and Mexican President Andrés Manuel López Obrador.

## Data Gathering (Scraping Twitter Data into a CSV File)
Our project team wrote a Python script that scraped Twitter data from the four world leaders into a newly created CSV file with six headers: Text (contents of the Tweet), User (the Twitter user handle), Date (date of the Tweet), Favs (number of Favorites for the Tweet), Retweets (number of Retweets for the Tweet), and Replies (number of Replies for the Tweet).

If you would like to scrape Twitter data for any user over a specified period of time, follow the instructions below.

### Setup
Before you can get started, you need to get your Terminal to be using a bash shell. Follow the first two steps in this README to do so: https://github.com/code4policy/modules/tree/main/setup

You will also be using Python, a programming language, to execute the script and generate a CSV file. Once your Terminal is using a bash shell, type the following command and hit "Enter" to install Python:
	brew install python

### Step-by-step Instructions
Once your Terminal is using a bash shell, you'll need to install **snscrape** and **pandas**. 

snscrape is a scraper for social networking services like Twitter, and allows you to scrape different kinds of Twitter data. To learn more about snsscrape, visit: https://github.com/JustAnotherArchivist/snscrape

pandas is open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. To learn more about pandas, visit: https://pandas.pydata.org/docs/index.html

1. To install snscrape and pandas, enter the following commands in your Terminal and hit "Enter":
	pip3 install snscrape
	pip3 install pandas

2. Download the Python script and save it somewhere. The script can be found on this page: https://github.com/whuang26/Twitter-Presidents/tree/main/scripts. We recommend saving it to your desktop in a folder. Hypothetically, let's name this folder "TwitterProject". You can rename the script - for example, if you want to scrape Tweets from Barack Obama, you might rename it to "Obama.py".

3. Customize the script for the specific Twitter user you want to scrape from and the specific timeframe. To change the user, change the green "from:@JoeBiden" field in line 23 to another user. For example, if you want to scrape Tweets from Barack Obama instead, edit the field to "from:@BarackObama".

If you want to edit the timeframe of the scrapped Tweets, change the green data parameters "since:2021-01-01 until:2022-01-01" in line 23. For example, if you want to scrape all of Barack Obama's Tweets from 2020 to 2021, edit the field to "since:2020-01-01 until:2022-01-01".

4. In line 41, change the green filepath to where you want the .csv file output to be created. You can also name your file.csv from this filepath. For example, if you are using a Mac and want to output the .csv file with the name "tweets_Obama" to the TwitterProject folder on your desktop from step 2, your filepath would be "/Users/whuang/Desktop/TwitterProject/tweets_Obama.csv" - be sure to replace "whuang" with your Mac username.

5. Save your Python script, open your Terminal, and run the following command:
	python3 /Users/whuang/Desktop/TwitterProject/Obama.py

Again, be sure to repace "whuang" with your Mac username.

6. You will receive this error in your Terminal:
	FutureWarning: username is deprecated, use user.username instead
  	tweet_list = [tweet.content, tweet.username, tweet.date, tweet.likeCount,tweet.retweetCount,tweet.replyCount]

Do not worry! Your .csv file should still have been generated - this error message has more to do with an internal change Twitter made to their API.

