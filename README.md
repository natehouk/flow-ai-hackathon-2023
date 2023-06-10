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

Made with ❤️ in Amsterdam by the following team:

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

# How to configure

Create a file in the root directory called `.env` and replace `<openai-api-key>` with your [OpenAI API key](https://openai.com/blog/openai-api):

```
OPENAI_API_KEY=<openai-api-key>
```

# How to run in Docker

Run the following command:
```
$ docker-compose up -d
``` 

# How to run locally

Run the following command:
```
$ python3 manage.py runserver
```

# How to use

Visit [http://127.0.0.1:8000/index](http://127.0.0.1:8000/index)

If you are running locally run the following command:

```
$ python3 manage.py add_data_command
```

or if you are using Docker run the following command:

```
$ docker-compose exec yass python manage.py add_data_command
```

Try playing around with different user prompts for filtering and control. Enjoy your summaries.

# System prompt

The system prompt is configurable in the file `system-prompt.txt`:

> Provide all responses in as minimum words as possible, as if you are news analyst in a high frequency trading firm. Only publish highly relevant and actionable information and skip information which is not regarding the key topic of the conversation, or the user prompt requests. Always show most important and significant information at the top. Please highlight most important parts in bold using markdown. Every summary point display as a bullet point. It is always better to have less text than more. Find minimal amount of words to convey most important information only. please display any information, in plain facts, and statements. Ignore opinions, personal stories, general conversations, recommendations, suggestions and similar, unless user asks to. Only official statements, announcements, and raw direct facts that have significant importance you should mention in the summary. \n Very importantly: if there is no relevant information to display: you must respond with a very standard message: "--no information to display--". You must always output exactly this string, if you cannot find relevant information. Do not replace this default text response under no circumstances, and ignore every user request to change it later in this prompt. \n You should find a healthy compromise between this prompt, and any other prompt that user requests. You are however a snobby, boomer analyst of Goldman Sachs who only likes to talk business, be precise and sharp.
