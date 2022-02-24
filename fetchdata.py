import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re


class Crawler:
  def __init__(self, company_name, url_pool, limit, keyword_dict):
    self.company_name = company_name
    self.url_pool = url_pool
    self.limit = limit
    self.visited_url = set()
    self.keyword_dict = keyword_dict

  def crawl(self):

    if not self.url_pool:
      return

    counter = 0

    while self.url_pool and counter < self.limit:
      source_url = self.url_pool.pop(0)
      self.visited_url.add(source_url)
      try:
        self.parse_web_page(source_url)
        counter += 1
        print(counter)
        print('Processed [%s]' % source_url)
        #print(keyword_dict)
      except Exception as ex:
        print('Failed to parse the site [%s]: %s' % (source_url, ex))


  #filter url and resolve relative url to absolute url
  def normalize_url(self, new_url,source_url):

    #filtering
    filters=['support','terms']
    if self.company_name not in new_url:
      return ''
    if 'http' in new_url and 'jobs' not in new_url:
      return ''
    for filter in filters:
      if filter in new_url:
        return ''

    #convert relative path
    if 'http' not in new_url and  'https' not in new_url:
      new_url=urljoin(source_url,new_url)
    return new_url


  def indexing(self, word_list):
    for word in word_list:
      # TODO: match synonyms
      word=word.lower()
      if word in self.keyword_dict:
        self.keyword_dict[word] += 1


  def parse_web_page(self, source_url):
    webUrl  = urllib.request.urlopen(source_url)
    bsObj = BeautifulSoup(webUrl, features="html.parser")

    for link in bsObj.find_all('a'):
      #to filter and handle relative path
      url_string = self.normalize_url(link.get('href'),source_url)
      if url_string and url_string not in self.visited_url:
        self.url_pool.append(url_string)

    self.indexing(bsObj.get_text().split())

