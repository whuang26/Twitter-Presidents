# Twitter-Presidents

A visualization of Twitter data from four prominent world leaders: U.S. President Joe Biden, Indian Prime Minister Narendra Modi, Turkish President Recep Tayyip Erdoğan, and Mexican President Andrés Manuel López Obrador.

## Data Gathering (Scraping Twitter Data into a CSV File)
Our project team wrote a Python script that scraped Twitter data from the four world leaders into a newly created CSV file with six headers: Text (contents of the Tweet), User (the Twitter user handle), Date (date of the Tweet), Favs (number of Favorites for the Tweet), Retweets (number of Retweets for the Tweet), and Replies (number of Replies for the Tweet).

If you would like to scrape Twitter data for any user over a specified period of time, follow the instructions below.

### Setup

Before you can get started, you need to get your Terminal to be using a bash shell. Follow the first two steps in this README to do so: https://github.com/code4policy/modules/tree/main/setup

You will also be using Python, a programming language, to execute the script and generate a CSV file. Once your Terminal is using a bash shell, type the following command and hit "Enter" to install Python: `brew install python`

### Step-by-Step Instructions

Once your Terminal is using a bash shell, you'll need to install **snscrape** and **pandas**. 

snscrape is a scraper for social networking services like Twitter, and allows you to scrape different kinds of Twitter data. To learn more about snsscrape, visit: https://github.com/JustAnotherArchivist/snscrape

pandas is open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. To learn more about pandas, visit: https://pandas.pydata.org/docs/index.html

1. To install snscrape and pandas, enter the following commands in your Terminal and hit "Enter":
	```
	pip3 install snscrape
	pip3 install pandas
	```
2. Download the Python script and save it somewhere. The script can be found on this page: https://github.com/whuang26/Twitter-Presidents/tree/main/scripts. We recommend saving it to your desktop in a folder. Hypothetically, let's name this folder "TwitterProject". You can rename the script - for example, if you want to scrape Tweets from Barack Obama, you might rename it to "Obama.py".

3. Edit the "Obama.py" Python script by right-clicking it and opening it with Sublime Text or another text editor. You can now customize the Python script for the specific Twitter user you want to scrape from and the specific timeframe. To change the user, change the green "from:@JoeBiden" field in line 23 to another user. For example, if you want to scrape Tweets from Barack Obama instead, edit the field to "from:@BarackObama".

	If you want to edit the timeframe of the scrapped Tweets, change the green data parameters "since:2021-01-01 until:2022-01-01" in line 23. For example, if you want to scrape all of Barack Obama's Tweets from 2020 to 2021, edit the field to "since:2020-01-01 until:2022-01-01".

4. In line 41, change the green filepath to where you want the .csv file output to be created. You can also name your file.csv from this filepath. For example, if you are using a Mac and want to output the .csv file with the name "tweets_Obama" to the TwitterProject folder on your desktop from step 2, your filepath would be "/Users/whuang/Desktop/TwitterProject/tweets_Obama.csv" - be sure to replace "whuang" with your Mac username.

5. Save your Python script, open your Terminal, and run the following command:
	```
	python3 /Users/whuang/Desktop/TwitterProject/Obama.py
	```
	Again, be sure to replace "whuang" with your Mac username.

6. You will receive this error in your Terminal:
	```
	FutureWarning: username is deprecated, use user.username instead
  	tweet_list = [tweet.content, tweet.username, tweet.date,tweet.likeCount,tweet.retweetCount,tweet.replyCount]
  	```
	Do not worry! Your .csv file should still have been generated - this error message has more to do with an internal change Twitter made to their API.



## Optional: Data Cleaning 

Since the visualization techniques we will use do not take the URLs, mentions, hashtags in the tweets into account while analyzing the data, we will not clean the scraped tweets. However, if you'd like to for your own data, we recommend using Tweet Preprocessor, which is a preprocessing library for tweet data written in Python.

Tweet Preprocessor currently supports cleaning, tokenizing, and parsing URLs, hashtags, mentions, reserved words (RT, FAV), emojis, smileys. The library only supports JSON and .txt file formats. Therefore, you may need to convert your CSV file into a JSON file first to use this library.

Detailed information on Tweet Preprocessor: https://pypi.org/project/tweet-preprocessor/



## Creating Word Clouds 

There are many online tools that allow you to upload a text file and it will generate a word cloud. Our choice for this project is MonkeyLearn's WordCloud Generator. If you want to learn why we chose MonkeyLearn, you can read our explanation on this page: https://whotweetswhat.works/about-project/index.html 

If you would like to create a MonkeyLearn word cloud using your scraped Twitter data, follow the instructions below.

### Step-by-Step Instructions

1. Generate your .csv file of scraped Twitter data by following the instructions above for **Data Gathering**. 

2. Go to https://monkeylearn.com/word-cloud/ and click the "Upload text file" button on the top right corner.

3. Locate and upload your .csv file of scraped Twitter data, and click "Generate cloud".

4. You now have your word cloud! On the top bar, you can adjust the color, font, and the number of terms in your cloud (up to 100 terms). You can also sort the terms by **Relevance** or **Frequency** on the right bar. To better understand the differences between the two results, read our explanation here: https://whotweetswhat.works/about-project/index.html 

5. Once you are satisfied with the appearance of your word cloud, you can click the blue "Download" button on the top right corner. You can then download either a .svg or .png image file of your word cloud. You also have the option to download a .csv of the word cloud terms with three headers: **Word** (the generated term), **Count** (the total count of the term in the document uploaded), and **Relevance** (the relevance score for the term). 

## Data Visualization D3 Bar Chart of Most Tweeted Terms 

Our project team used Observablehq to create this visualization 

### Setup

To use Observablehq, create an account on the site. You can complete this visualization by forking code from an existing bar chart or following the step-by-step instructions below.  

### Step-by-Step Instructions

1. Create a blank notebook on ObeservableHQ. Insert a new cell and import your data to the file. Remember we are only changing this code to suit our bar chart requirements, so change the lyric column in your data set and add the the leaders tweets in its place. Do add attachment, presh command+shift+u and select the file:

	```
	FileAttachment("your_file_name.csv")
	```
Running this command will allow you to view the data you have uploaded. 

2. Add the following D3.js javascript code and create a CSV loop calling csvParse to parse the input string. This returns an array of objects in each row. 

	```
	d3 = {
  		const d3 = require("d3-dsv@1", 	"d3@5","d3-scale@3","d3-scale-chromatic@1", "d3-shape@1", "d3-array@2")
  	return d3
	}
	```


	```
	data = {
  	const text = await FileAttachment("tswiftlyrics.csv").text();
  		return d3.csvParse(text, ({lyric}) => ({
    	lyric: lyric
  		}));
 	}
	```

3. Make an empty array and convert to lover case, clean up text

	```
	lyrics = [ ]

	```

	```
	data.forEach(lyric => lyrics.push(lyric.lyric));

	```

	```
	newLyrics = lyrics.join(' ').replace(/[.,\/#!""'$%\?^&\*;:{}=\-_`~()0-9]/g,"").toLowerCase()

	```

4. Add stopwords as per your language requirements. You can search the internet, specifically for github for opensource, forkable stopwords. 

	```
	newLyrics = lyrics.join(' ').replace(/[.,\/#!""'$%\?^&\*;:{}=\-_`~()0-9]/g,"").toLowerCase()

	```
	
	```
	stopword = [Add stop words here]

	```
5. The next step is to remove all the stopwords from the text. 

	```
	remove_stopwords = function(str) {
    	var res = []
    	var words = str.split(' ')
  		for(let i=0;i<words.length;i++) {
       		var word_clean = words[i].split(".").join("")
       		if(!stopwords.includes(word_clean)) {
           res.push(word_clean)
       }
    }
    return(res.join(' '))
	}

	```
	
	```
	lyrics_no_stopwords = remove_stopwords(newLyrics)

	```

6. Get string frequency for each lyric 

	```
	strFrequency = function (stringArr) { //es6 way of getting 	frequencies of words
  		return stringArr.reduce((count, word) => {
        count[word] = (count[word] || 0) + 1;
        return count;
  		}, {})
	}
	```
	
	```
	obj = strFrequency(lyrics_no_stopwords.split(' '))

	```

7. Create a function to return the first n items in the object and sort the frequencies to be max to min

	```
	sortedObj = Object.fromEntries(
	// switch a[1] and b[1] in the arrow function
	Object.entries(obj).sort( (a,b) => b[1] - a[1] )
	)

	```
8. Set attributes of the chart/graph as per your requirement:

	```
	margin = ({top: 20, right: 0, bottom: 30, left: 40})

	height = 500

	x = d3.scaleBand()
    	.domain(final.map(d => d.lyric))
    	.rangeRound([margin.left, width - margin.right])
    	.padding(0.1)

    y = d3.scaleLinear()
    	.domain([0, d3.max(final, d => d.freq)])
    	.range([height - margin.bottom, margin.top])

    yTitle = g => g.append("text")
    	.attr("font-family", "sans-serif")
    	.attr("font-size", 10)
    	.attr("y", 10)
    	.text("Frequency")

    xAxis = g => g
    	.attr("transform", `translate(0,${height - margin.bottom})`)
    	.call(d3.axisBottom(x).tickSizeOuter(0))

    yAxis = g => g
    	.attr("transform", `translate(${margin.left},0)`)
    	.call(d3.axisLeft(y).ticks(15))
    	.call(g => g.select(".domain").remove())

    	tooltip = d3.select("body")
      .append("div")
      .style("position", "absolute")
      .style("font-family", "'Open Sans', sans-serif")
      .style("font-size", "15px")
      .style("z-index", "10")
      .style("background-color", "#A7CDFA")
      .style("color", "#B380BA")
      .style("border", "solid")
      .style("border-color", "#A89ED6")
      .style("padding", "5px")
      .style("border-radius", "2px")
      .style("visibility", "hidden");

	```

9. Create an svg and run the program 

	```
	{
  	const svg = d3.create("svg")
      .attr("viewBox", [0, 0, width, height]);

  	// Call tooltip
  	tooltip;

  	svg.append("g")
  	.selectAll("rect")
  	.data(final)
  	.enter().append("rect")
   	 .attr('x', d => x(d.lyric))
    	.attr('y', d => y(d.freq))
    	.attr('width', x.bandwidth())
    	.attr('height', d => y(0) - y(d.freq))
    	.style("padding", "3px")
    	.style("margin", "1px")
    	.style("width", d => `${d * 10}px`)
    	.text(d => d)
    	.attr("fill", "#CEBEDE")
    	.attr("stroke", "#FFB9EC")
    	.attr("stroke-width", 1)
  	.on("mouseover", function(d) {
      		tooltip.style("visibility", "visible").text(d.lyric + ": " + d.freq);
     	 d3.select(this).attr("fill", "#FDE5BD");
   	 })
    	.on("mousemove", d => tooltip.style("top", (d3.event.pageY-10)+"px").style("left",(d3.event.pageX+10)+"px").text(d.lyric + ": " + d.freq))
   	.on("mouseout", function(d) {
      	tooltip.style("visibility", "hidden");
      	d3.select(this)
    	.attr("fill", "#CEBEDE")
    	});

  
  	svg.append("g")
      	.call(xAxis);
  	svg.append("g")
      	.call(yAxis);
  
  	svg.call(yTitle);

  	return svg.node();
	}
	```

This process has been adapted from an existing interactive chart already published on oberservablehq. You can use other similar charts on obeservable to create bar chart of your requirement. 
