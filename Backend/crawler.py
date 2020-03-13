import requests
import re

from link import Link

class Crawler:
    def __init__(self, url = None, max_depth = 6):
        self.__current_url = url
        self.__history = []
        self.__depth = -1
        self.__html = None
        self.max_depth = max_depth

        if url:
            self.navigate(url=url)

        # <div class ="article-date"><strong>Published</strong><time>1 day ago</time></div>
        # print(requests.get('https://www.foxnews.com/').text)

    def visited(self, url: str):
        return url in self.__history

    def links(self):
        result = []
        for link in re.findall('<a href="(.*?)"', self.__html):
            if len(link) > 2 and link[0] == '/' and link[1] != '/':
                link = f'{self.__current_url}/{link[1:]}'
            elif link == '/':
                link = self.__current_url

            result.append(Link(url=link))
        return result

    def navigate(self, url):
        if self.is_done():
            return

        self.__html = requests.get(url).text
        self.__depth = self.__depth + 1
        self.__history.append(url)

    def is_done(self):
        return self.__depth >= self.max_depth

