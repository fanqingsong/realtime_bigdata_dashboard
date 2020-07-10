# coding: utf-8
import time
from kafka import KafkaProducer
import requests
from bs4 import BeautifulSoup

web_url = "https://en.wikipedia.org/wiki/COVID-19_pandemic"

class Scrawler:
    def __init__(self, web_url):
        self._web_url = web_url

        self._producer = KafkaProducer(bootstrap_servers='localhost:9092')

    def _get_html_doc(self):
        res = requests.get(self._web_url)
        print(res.text)

        html_doc = res.text

        return html_doc

    def _get_all_paragraphs(self, html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')

        paragraphs = []
        for para in soup.find_all("p"):
            para_content = para.get_text()
            print(para_content)
            paragraphs.append(para_content)

        return paragraphs

    def _send_paragraphs(self, paragraphs):
        for para in paragraphs:
            self._producer.send('rawContent', para.encode('utf8'))
            time.sleep(1)

    def execute(self):
        html_doc = self._get_html_doc()
        paragraphs = self._get_all_paragraphs(html_doc)
        self._send_paragraphs(paragraphs)

if __name__ == "__main__":
    scrawler = Scrawler(web_url)
    scrawler.execute()

