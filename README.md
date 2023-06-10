# flow-ai-hackathon-2023

## YASS (Yet Another Streaming Summarizer)

Yet Another Streaming Summarizer, or YASS, is a tool to make live streaming summaries of inputs with the help of a Large Language Model (LLM).

Possible inputs include:
* Streaming or prerecorded meeting from WebEx
* Streaming chats from WebEx
* Streaming video news from YouTube
* Prerecorded video from YouTube
* NewsAPI news stories

The results are then added to a data frame which is appended to the system prompt. Finally, a user prompt is appended which allows for interactive filtering and control.

Output is concise, actionable bytes of information formatted in Markdown which streams to the browser.

# Team Orange

Built with ❤️ in Amsterdam by the following team:

* Marius Kluonis
* Ayush Shivani
* Sarvesh Mehta
* Nate Houk

# How to build

Run the following commands:
```
$ mkdir -p /opt/src
$ cd /opt/src
$ git clone git@github.com:natehouk/flow-ai-hackathon-2023.git
$ cd flow-ai-hackathon-2023
$ pyenv install 3.8.16
$ pyenv shell 3.8.16
$ pip install -r requirements.txt
```

# How to run in Docker

Run the following command:
```
$ docker-compose up -d
```

Visit 

# How to run locally

Run the following command:
```
$ python3 manage.py runserver
```

# How to use

Visit [http://127.0.0.1:8000/index](http://127.0.0.1:8000/index)

Run the following command:

```
$ python3 manage.py add_data_command
```

Try playing around with different user prompts for filtering and control. Enjoy your summaries.
