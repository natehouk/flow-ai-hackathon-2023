# flow-ai-hackathon-2023

**YASS (Yet Another Streaming Summarizer)**
Yet Another Stream Summarizer, or YASS, is a tool to make live streaming summaries of inputs with the help of a GPT LLM.

Possible inputs include:
* Streaming or prerecorded meeting from WebEx
* Streaming chats from WebEx
* Streaming video news from YouTube
* Prerecorded video from YouTube
* NewsAPI news stories

**Team Orange**
Marius Kluonis
Ayush Shivani
Sarvesh Mehta
Nate Houk

**How to build**
```
$ mkdir -p /opt/src
$ cdd /opt/src
$ git clone git@github.com:natehouk/flow-ai-hackathon-2023.git
$ pyenv install 3.8.16
$ pyenv shell 3.8.16
$ pip install -r requirements.txt
```

**How to run**
```
$ python3 manage.py runserver
```

Visit [http://127.0.0.1:8000/index](http://127.0.0.1:8000/index)

```
$ python3 manage.py add_data_command
```
