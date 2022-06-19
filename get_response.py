from bs4 import BeautifulSoup
import requests


def get_links(url):
    try:
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.content, 'lxml')
        return [item['href'] if item.get('href') is not None else item['src']
                for item in soup.select('[href^="http"], [src^="http"]')]
    except requests.exceptions.ConnectionError:
        return 'No internet connection!'
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema):
        return 'Bad response!'
