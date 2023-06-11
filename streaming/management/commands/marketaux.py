import requests
import json

def get_top_headlines_from_newsapi(params=""):
    endpoint = "https://api.marketaux.com/v1/news/all"
    query_input = ""
    api_token = "x4ZhlBIav8w8VhTLB3cDEo4CnyVRDQJiNwwVVIwq"
    query_params = "?entity_types=index,equity" + "&api_token="+ api_token 
    articles = json.loads(requests.get(endpoint+query_params).text)
    new_headlines = set()
    for headline in articles["data"]:
        title = headline["title"]
        description = headline["description"].replace("\n"," ").replace("  "," ")
        if description is None:
            description = ""
        source = headline["source"]
        new_headlines.add(str({'title':title,"description":description,"source":source}))
    return new_headlines

def request_headlines(previous_headline):
    current_headline = set()
    new_headline = set()
    current_headline = get_top_headlines_from_newsapi(params="")
    new_headline = current_headline - previous_headline
    return new_headline