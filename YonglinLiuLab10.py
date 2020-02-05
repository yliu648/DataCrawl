#Yonglin Liu Lab 10
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

#use the prettify function and save the result to a file, which we can open in a text editor
#with open('C:/Users/michael.deamer/Desktop/jazz.html', 'w', encoding='utf8') as jazzHTML:
#jazzHTML.write(soup.prettify())
outputFileName = 'C:/Users/yongl/Fordham/Fall 2019/Python/Lab/jazz.html'
urlList = ['https://www.yelp.com/biz/jazz-standard-new-york']

pagination = 'Page 1 of 12'
ofIndex = pagination.index('of')
totalPage = pagination[ofIndex+3:]

nextPage = 20
i = 1
while i < int(totalPage):
    nextUrl = 'https://www.yelp.com/biz/jazz-standard-new-york?start=' + str(nextPage)
    urlList.append(nextUrl) 
    nextPage += 20
    i += 1

for url in urlList:
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    #with open (outputFileName, 'w', encoding = 'utf8') as jazzHTML:
     #   jazzHTML.write(soup.prettify())
     
    reviewList = soup.find_all('div', itemprop = 'review')
    #review is the parent tag
    parentList = []
    for review in reviewList:
        comment = review.find('p', itemprop = 'description').get_text()
        author = review.find('meta', itemprop = 'author')['content']
        #look for a mata tag where there is an itemprop of author
        #author infor is within the text so cant use get_text function
        stars = review.find('meta', itemprop = 'ratingValue')['content']
        date = review.find('meta', itemprop = 'datePublished')['content']
        childList = [author, stars, date, comment]
        parentList.append(childList)

    commentFrame = pd.DataFrame(parentList)
    print(commentFrame.head())
    #to save to a csv file: df.to_csv(path)
