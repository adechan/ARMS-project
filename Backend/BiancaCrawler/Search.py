import urllib.request
from bs4 import BeautifulSoup
import json
# import pandas as pd
articleUrls=[]
# import Crawler
import re

def searchArticleUrls(path):
    links=open(path,"r")
    for link in links:
        articleUrls.append(link)


def searchAWord(string):
    searchArticleUrls("Urls.txt")
    records=[]
    i = 0
    for url in articleUrls:
        i += 1
        print(f'{i}/{len(articleUrls)}')
        try:
            request = urllib.request.Request(url)
            html = urllib.request.urlopen(request).read()
            soup = BeautifulSoup(html,'html.parser')
            article_body=soup.find_all('div',attrs={'id':'app'})
            for a in article_body:
                if string in str(a):
                    date=a.find('time').text
                    regex = re.findall(r"[A-Z][a-z]+,?\s+(?:[A-Z][a-z]*\.?\s*)?[A-Z][a-z]+", str(a))
                    print(regex)
                    if 'Published ' in date:
                        date = date.sub(len('Published '))
                    category=a.find("a",attrs={'class':'css-nuvmzp'}).text[0:]
                    article_title=a.find("h1").text[0:]
                    print(category)
                    records.append((string,category,article_title,date))
                # except:
                #     pass
        except:
            pass
    # df = pd.DataFrame(records, columns=['string', 'category', 'article_title', 'date'])
    # df.to_csv('category.csv', index=False, encoding='utf-8')
    return records


def categories(records):
    d = dict()
    for record in records:
        if record[1] not in d:
            d[record[1]] = 1
        else:
            d[record[1]] += 1
    return d


if __name__ == "__main__":
    searchAWord("Trump")


