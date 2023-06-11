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

# How to Configure
Create a file in the root directory called `.env` and replace `<openai-api-key>` with your [OpenAI API key](https://openai.com/blog/openai-api), [NewsAPI key](https://newsapi.org), [Whisper API Key](https://whisperapi.com), choose an OpenAI GPT model ("gpt-4", "gpt-3.5-turbo", etc) and set the system prompt:
```
NEWS_API_KEY="<news-api-key>"
OPENAI_API_KEY="<openai-api-key>"
WHISPER_API_KEY="<whisper-api-key>"
GPT_MODEL="gpt-4"
SYSTEM_PROMPT="Follow these rules:\n* Your job is to summarize data inputs into bullet points.\n* Be concise.\n* Always show most important information as the top bullet point.\n* Emphasize important parts in bold using Markdown.\n* Companies, names and proper nouns should be in italic using Markdown.\n* Never write more than five bullet points.\n* The bullet points, bold and italic should be formatted using Markdown."
```

Remember that your costs will be affected by the GPT model chosen.

Configuring the system prompt is important for giving your LLM flair and setting up the constraints of the inference. The default system prompt is:

> Follow these rules:
> * Your job is to summarize data inputs into bullet points.
> * Be concise.\n* Always show most important information as the top bullet point.
> * Emphasize important parts in bold using Markdown.
> * Companies, names and proper nouns should be in italic using Markdown.
> * Never write more than five bullet points.
> * The bullet points, bold and italic should be formatted using Markdown.

You can copy the file `.env-template` to `.env` and use it as a template for your configuration.

# How to Run in Docker

Run the following command:
```
$ docker-compose up -d
``` 

# How to Build Manually

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

# How to Run Locally

Run the following command:
```
$ python3 manage.py runserver
```

# How to Use

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

If you are running locally run the following command:

```
$ python3 manage.py add_data_command
```

or if you are using Docker run the following command:

```
$ docker-compose exec yass python manage.py add_data_command
```

Try playing around with different user prompts for filtering and control. Enjoy your summaries.
