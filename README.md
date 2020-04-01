# Crawling Yelp Reviews
The Jazz Standard is a restaurant and jazz club in New York City. This readme demo shows how I scraped comments about the club from yelp.com.

1. Import the BeautifulSoup class from bs4 and urlopen from urllib:
```
from bs4 import BeautifulSoup
from urllib.request import urlopen
```

2. Use the urlopen function to open the url:
```
url = https://www.yelp.com/biz/jazz-standard-new-york
page = urlopen(url)
```
Note:
Although nothing is displayed to the screen, this code causes Python to navigate to the site and retrieve its html code.

3. Pass the page object to the BeautifulSoup class. This requires a second parameter: ‘html.parser’. The second parameter indicates the type of code our first parameter is using:
```
soup = BeautifulSoup(page, 'html.parser')
```

4. We can use BeautifulSoup’s find() function to search for the first tag where the itemprop attribute equals ‘description’. We only want the text, not the tag. For this, we can add the get_text() function, and save it to a variable named comment:
```
comment = soup.find(itemprop='description').get_text()
```

5. By adding the name of that attribute, we can get the date and save it to a variable named date:
```
date = soup.find(itemprop='datePublished')['content'] 
```

6.	We can repeat the code above to get the author and number of stars:
```
author = soup.find(itemprop='author')['content']
stars = soup.find(itemprop='ratingValue')['content']
```

7.	Let’s use BeautifulSoup’s find() function to the find the review tag again and save it to a review variable:
```
review = soup.find(itemprop='review')
```
Note:
	This line of code should precede the code to find the comment, date, author, and stars.

8.	to find the comment, we will attach it to the review variable:
```
comment = review.find(itemprop='description').get_text()
```

Note:
	This must also be done for the date, author, and stars.

9.	Our code works for the first comment. To find all reviews, we will change the find() function to find_all():
```
reviews = soup.find_all(itemprop='review')
```

Note:
	The variable name ‘review’ has also been changed to ‘reviews’

10.	However, the find() and find¬¬_all() functions do not return the same datatypes. Find() returns a tag object, but find_all() returns a list of tags. To iterate over all tags returned by the find_all() function, we can add a for loop:
```
for review in reviews:
    comment = review.find(itemprop='description').get_text()
```

Note:
The lines of code to find the date, author, and stars should also be added to this for loop.

11.	We can create a list of the results. To do so:
    a.	We can create an empty list object before the loop:
```
allReviews = []
```
b.	As the last line of code inside the loop, we can append to this list:
```
allReviews.append([comment, date, author, stars])
```

12.	passed to Pandas’ DataFrame() class to create a dataframe. To do this:
a.	Import Pandas:
```
import pandas as pd
```
Note:
This should appear near the top of the script. It is not wise to import packages inside of loops.
'https://www.yelp.com/biz/jazz-standard-new-york'

b.	After the for loop, pass the allReviews variable to theDataFrame() class and print the results:
```
reviewFrame = pd.DataFrame(allReviews)
print(reviewFrame.head())
```
Note:
To increase performance, we only want to print the first few rows to verify that the code is working. The head() function will reduce the dataframe to only the first few rows.


