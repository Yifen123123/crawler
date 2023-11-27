# 抓取PTT電影版的網頁原始碼（HTML)
import requests
from bs4 import BeautifulSoup
url = "https://www.ptt.cc/bbs/movie/index.html"
# 建立一個 Request 物件， 附加 Request Headers 的資訊
#request = req.Request(url, headers={
    #"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)
# 檢查狀態碼
if response.status_code == 200:
    # 使用 BeautifulSoup 解析 HTML 内容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 獲取文章列表
    articles = soup.find_all('div', class_='r-ent')
    
    # 遍历文章列表并打印标题和链接
    for article in articles:
        title = article.find('div', class_='title').text.strip()
        if title.find("暮光之城") != -1:
            link = article.find('div', class_='title').a.get('href')
            print(f'Title: {title}\nLink: https://www.ptt.cc{link}\n')
else:
    print(f'Failed to retrieve page. Status code: {response.status_code}')

#with req.urlopen(url) as response:
#data = response.read().decode("utf-8")
#print(data)
# 解析原始碼，取得每篇文章的標題
#import bs4
#root = bs4.BeautifulSoup(data, "html.parser")
#print(root.title.string)
#titles = root.find("div",class_="title")#尋找 class = "title"的div 標籤
#print(titles)
#for title in titles:
    #if title.a !=None: #如果標題包含a 標籤（沒有被刪除）印出來
       # print(title.a.string)