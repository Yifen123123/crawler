import requests
from bs4 import BeautifulSoup

def get_page_content(url):
    # 設定 User-Agent 以模擬瀏覽器的請求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # 透過 requests 模組發送 GET 請求，獲取頁面內容
    response = requests.get(url, headers=headers)
    
    # 檢查響應狀態碼
    if response.status_code == 200:
        # 使用 BeautifulSoup 解析 HTML 內容
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        # 如果請求失敗，印出錯誤信息並返回 None
        print(f'Failed to retrieve page. Status code: {response.status_code}')
        return None

def scrape_ptt_movie_pages(start_page, end_page):
    # PTT 電影版的基礎 URL
    base_url = "https://www.ptt.cc/bbs/movie/index.html"
    
    # 進行指定頁數範圍的爬取
    for _ in range(end_page - start_page + 1):
        # 取得當前頁面的內容
        soup = get_page_content(base_url)
        
        if soup:
            # 找到所有文章條目
            articles = soup.find_all('div', class_='r-ent')
            
            for article in articles:
                # 取得文章標題
                title = article.find('div', class_='title').text.strip()
                # 如果標題中包含"驚奇隊長2"，則印出相關信息
                if title.find("驚奇隊長2") != -1:
                    link = article.find('div', class_='title').a.get('href')#href:title的連結
                    print(f'Title: {title}\nLink: https://www.ptt.cc{link}\n')


            # 找到上一頁的鏈接
            # 找上一頁的連結是因為在網址中的內容沒有下一頁 
            prev_link = soup.find('div', class_='btn-group btn-group-paging').find_all('a')[1].get('href')
            base_url = 'https://www.ptt.cc' + prev_link

# 爬取第1頁到第5頁的內容
scrape_ptt_movie_pages(1, 5)
