from newsapi import NewsApiClient
import json


def get_top_headlines_from_newsapi(params=""):
    newsapi = NewsApiClient(api_key=os.environ.get("NEWSAPI_KEY"))
    top_headlines = newsapi.get_top_headlines(q=params,
                                            category='business',
                                            language='en',
                                            country='us')
    articles = top_headlines["articles"] 
    new_headlines = set()
    for news in articles:
        title = news["title"]
        source = news["source"]["name"]
        description = news["description"]
        content = news["content"]
        # print(title,source,description,content)
        new_headlines.add(str({'title':title,"description":description,"source":source}))
    

    return new_headlines

def request_headlines(previous_headline):
    current_headline = set()
    new_headline = set()
    current_headline = get_top_headlines_from_newsapi(params="")
    new_headline = current_headline - previous_headline
    print(new_headline)
    return new_headline


