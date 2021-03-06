from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

with open('sample.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['headline', 'summary', 'video_link'])

    for article in soup.find_all('article'):
        headline = article.h2.a.text
        summary = article.find('div', class_="entry-content").p.text

        try:
            vid_src = article.find('iframe', class_="youtube-player")['src']
            vid_id = vid_src.split('/')[4].split('?')[0]
            yt_link = f'https://youtube.com/watch?v={vid_id}'

        except Exception as e:
            yt_link = None

        csv_writer.writerow([headline, summary, yt_link])



