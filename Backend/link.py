
class Link:
    def __init__(self, url = ''):
        self.url = Link.clean_url(url)

    @staticmethod
    def clean_url(url: str):
        if 'http:' in url or 'https:' in url:
            return url

        return f'https:{url}'

    def __str__(self):
        return self.url

    def is_article(self):
        pass