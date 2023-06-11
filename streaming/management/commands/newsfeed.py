from newsapi import NewsApiClient
from streaming.management.commands.chatgpt import get_prompt

import json
import os


def get_top_headlines_from_newsapi(params=""):
    newsapi = NewsApiClient(api_key=os.environ.get("NEWS_API_KEY"))
    top_headlines = newsapi.get_top_headlines(q=params,
                                            category='business',
                                            language='en',
                                            country='us')
    # print(top_headlines)
    articles = top_headlines["articles"] 
    new_headlines = set()
    for news in articles:
        title = news["title"]
        source = news["source"]["name"]
        description = news["description"]
        if description is None:
            description = ""
        # print(title,source,description,content)
        new_headlines.add(str({'title':title,"description":description,"source":source}))
    

    return new_headlines

def request_headlines(previous_headline):
    current_headline = set()
    new_headline = set()
    current_headline = get_top_headlines_from_newsapi(params="")
    new_headline = current_headline - previous_headline
    # print(list(new_headline))
    return list(new_headline)

