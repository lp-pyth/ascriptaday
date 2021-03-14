# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 15:36:07 2021
google news headline scanner
@author: lux
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import re
from collections import Counter
c = Counter()  

findword = ''    #What word are you looking for

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()
soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")

def word_search(findword):
#   search0 = rf'\b{findword}\b'          #r'\bbob\b'      # matches bob
    search1 = rf'(?i)\b{findword}\b'      #r'(?i)\bbob\b'  # matches bob, Bob
#   search2 = rf'{findword}'              #r'bob'          # matches bob, Bob, bobcat  
    contents = news.title.text
    count = sum(1 for match in re.finditer(search1, contents))
    return count

# Print publish date, news title, link and how often word was found
article_count = 0
for news in news_list:
  if (word_search(findword)) > 0:     
      article_count = article_count + 1
      print(news.pubDate.text)
      print(news.title.text)
      print(news.link.text)
      print("Word found in article:", word_search(findword))
      print("-"*60)
      print("")
      
print('Total number of articles:', len(news_list))
print('Number of articles with search term:', article_count)
  
  
  
  
  
  