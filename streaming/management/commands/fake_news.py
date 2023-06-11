def fake_news(index = 0):
    news_headline = set()
    file = open("sample.txt")
    news_headline = file.readlines()[index:index+4]
    return news_headline
