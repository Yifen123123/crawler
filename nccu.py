import requests
from bs4 import BeautifulSoup
url = "https://www.facebook.com/groups/628916884757960"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)
print(1)
if response.status_code == 200:
    print(2)
    soup = BeautifulSoup(response.text, 'html.parser')#'html.parser'是一個解析器，指定BeautifulSoup使用哪種方式解析HTML。
    articles = soup.find_all('div', class_='mbox')
    for article in articles:
        print(3)
        title = article.find('div', class_='mtitle').text.strip()
        print(title)
else:
    print(f'Failed to retrieve page. Status code: {response.status_code}')
