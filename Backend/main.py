from crawler import Crawler

crawler = Crawler(url='https://www.foxnews.com/', max_depth=4)

while not crawler.is_done():
    articles = [link for link in crawler.links()]
    print(f'First link: {articles[0]}')

    for link in articles:
        print(f'Navigating to {link.url}')
        try:
            crawler.navigate(url=link)
            break
        except Exception as e:
            print(f'Error: {e}')
