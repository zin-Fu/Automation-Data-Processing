import requests
from bs4 import BeautifulSoup
import os
import json
import chardet

# 确保输出文件夹存在
output_dir = 'articles'
os.makedirs(output_dir, exist_ok=True)

def save_article(url):
    try:
        # 发送 GET 请求
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功

        # 自动检测编码
        detected_encoding = chardet.detect(response.content)['encoding']
        if detected_encoding:
            response.encoding = detected_encoding
        else:
            response.encoding = 'utf-8'  # 如果检测不到编码，默认使用 utf-8

        # 解析 HTML 内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 自动抓取文章标题（根据网页的不同，你可能需要修改这里）
        title = soup.title.string.strip().replace(" ", "_").replace("/", "_")

        # 提取文章内容，根据页面的实际结构修改选择器
        article_content = soup.find('div', class_='article-content')

        if not article_content:
            # 如果找不到这个 div，可以尝试抓取所有段落 <p> 标签作为内容
            article_content = soup.find_all('p')
            article_text = '\n'.join([p.get_text() for p in article_content if p.get_text()])
        else:
            article_text = article_content.get_text(strip=True)

        # 保存到 TXT 文件
        file_name = os.path.join(output_dir, f"{title}.txt")
        with open(file_name, 'w', encoding='utf-8') as article_file:
            article_file.write(article_text)

        print(f"Saved article: {file_name}")
    
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")

def read_urls_from_json(file_path):
    """从 JSON 文件中读取所有 URL 并爬取它们的内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for item in data:
            url = item.get('url')
            if url:
                save_article(url)
    except Exception as e:
        print(f"Failed to read JSON file: {e}")

def main():
    while True:
        # 用户输入网页链接或者 JSON 文件路径
        input_str = input("请输入要爬取的网页链接或JSON文件路径 (或输入 'exit' 退出): ").strip()
        
        # 如果输入 'exit' 则退出程序
        if input_str.lower() == 'exit':
            print("程序结束")
            break
        
        # 检查输入的是 JSON 文件还是单个 URL
        if input_str.endswith('.json'):
            read_urls_from_json(input_str)
        else:
            save_article(input_str)

if __name__ == "__main__":
    main()
