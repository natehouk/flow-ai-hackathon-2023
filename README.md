# flow-ai-hackathon-2023

## YASS (Yet Another Streaming Summarizer) 🤖

Introducing YASS, the ultimate streaming data summarizer marvel! ✨ Powered by ChatGPT, YASS transforms videos, audios, and news streams into concise insights. 🎥🎧📰 This cutting-edge tool goes beyond mere input flexibility, empowering users to customize summaries based on their unique requirements using prompts. 💪 Say goodbye to information overload and hello to streamlined knowledge extraction with YASS.

Whether you're seeking key takeaways from a video, unraveling audio mysteries, or staying up-to-date with news, YASS has you covered. 📺🔍📡 It's coolness lies in the seamless integration of diverse input data sources, ensuring no information escapes your grasp. 🌐 With YASS, you're in control, shaping summaries to suit your needs.

Embrace the power of YASS, the future of streaming data summarization. Stay ahead of the curve, save time, and make informed decisions effortlessly. ⏱️💡 Unlock the coolness factor today with YASS, your all-in-one streaming summarizer! 🚀🔓

Possible inputs include:
* Live Television News
* Live Radio News
* Live WebEx Meeting
* WebEx Meeting
* YouTube Video
* News Articles
* Market Data
* Twitter
* Telegram
* and more with the Custom Plugin SDK!

The results are then added to a data frame which is appended to the system prompt. Finally, a user prompt is appended which allows for interactive filtering and control.

Output is concise, actionable bytes of information formatted in Markdown which streams to the browser.

# Technical Diagram + Data Flow

```
┌─────────────────────┐
│                     │
│ ┌─────────────┐     │  ┌────────────┐      ┌────────────────────────────────┐
│ │Youtube URL  ├─────┼──┤audio strip ├─────►│                                │
│ └─────────────┘     │  └────────────┘      │                                │
│                     │                      │ extract text with Whisperer API│
│ ┌─────────────────┐ │                      │                                │
│ │Audio files .wav ├─┼─────────────────────►│                                │
│ └─────────────────┘ │                      └──────────────┬─────────────────┘
│                     │                                     │
│ ┌─────────┐         │                                     ▼                       Website GUI
│ │Twitter  ├─────────┼─────────────────►┌─────────────────────────┐  ┌──────────────────────────────┐
│ └─────────┘         │                  │                         │  │                              │
│                     │                  │                         │  │ ┌─────────────────────────┐  │
│ ┌────────┐          │                  │ Text handling service   ├──┤►│Raw collected data output│  │
│ │NewsAPI ├──────────┼─────────────────►│                         │  │ └─────────────────────────┘  │
│ └────────┘          │                  │                         │  │                              │
│                     │                  └─────────────┬───────────┘  │                              │
│ ┌──────────┐        │                    ▲           │              │                              │
│ │Others... ├────────┼────────────────────┘           │              │                              │
│ └──────────┘        │                                ▼              │                              │
│                     │                   ┌────────────────────────┐  │                              │
│                     │                   │                        │  │                              │
└─────────────────────┘ ┌───────────────┐ │                        │  │ ┌──────────────────┐         │
 Datasources            │ system prompt │►│  ChatGPT processor     │◄─┼─┤User prompt input │         │
                        └───────────────┘ │                        │  │ └──────────────────┘         │
                                          └────────────┬───────────┘  │                              │
                                                       │              │                              │
                                                       │              │ ┌──────────────────────┐     │
                                                       └──────────────┤►│Processed data output │     │
                                                                      │ └──────────────────────┘     │
                                                                      │                              │
                                                                      └──────────────────────────────┘

```

# Team Orange

Made with ❤️ in Amsterdam by the following team:

* Marius Kluonis
* Ayush Shivani
* Sarvesh Mehta
* Nate Houk

# Live Demo

Visit [http://yass.work/](http://yass.work/)

**Example Videos for YouTube URL Input Source**
* [https://www.youtube.com/watch?v=UYrm0DZGhaQ](https://www.youtube.com/watch?v=UYrm0DZGhaQ)
* [https://www.youtube.com/watch?v=01xYpDhYwGg](https://www.youtube.com/watch?v=01xYpDhYwGg)
* [https://www.youtube.com/watch?v=9eTzV7HvKHU](https://www.youtube.com/watch?v=9eTzV7HvKHU)
* [https://www.youtube.com/watch?v=L4BqP8qM9yA](https://www.youtube.com/watch?v=L4BqP8qM9yA)
* [https://www.youtube.com/watch?v=IyoGdwVIwWw](https://www.youtube.com/watch?v=IyoGdwVIwWw)
* [https://www.youtube.com/watch?v=02ut26-HFGg](https://www.youtube.com/watch?v=02ut26-HFGg)

**Example User Prompts**
* Display all output as HTML with CSS styling.  Do not include any other text, other than HTML/CSS, start directly with first HTML tag. Output should look as a bullet point list. Please pick cryptocurrency trading and cryptocurrency market related words and make sure they are displayed in red color.  Also if it is Tesla related - add a hyperlink to google search regarding the specific topic. Each bullet point should be 7 words long.
* The following prompt is by far most important. Ignore anything that was requested before this. Only listen to the following: Only display information about price predictions. I only care if price should go up or down. Any statement about price is important and nothing else.
* Translate all data from non-English sources into the English language.

# How to Configure
Create a file in the root directory called `.env` and replace `<openai-api-key>` with your [OpenAI API key](https://openai.com/blog/openai-api), [NewsAPI key](https://newsapi.org), [Whisper API Key](https://whisperapi.com), choose an OpenAI GPT model ("gpt-4", "gpt-3.5-turbo", etc) and set the system prompt:
```
NEWS_API_KEY="<news-api-key>"
OPENAI_API_KEY="<openai-api-key>"
WHISPER_API_KEY="<whisper-api-key>"
MARKETAUX_API_KEY="<marketaux-api-key>"
GPT_MODEL="gpt-4"
SYSTEM_PROMPT="Follow these rules: 1) Your job is to summarize data inputs into bullet points. 2) Be concise. 3) Always show most important information as the top bullet point. 4) Emphasize important parts in bold using Markdown. 5) Companies, names and proper nouns should be in italic using Markdown. 6) Never write more than five bullet points. 7) The bullet points, bold and italic should be formatted using Markdown."
```

Remember that your costs will be affected by the GPT model chosen.

Configuring the system prompt is important for giving your LLM flair and setting up the constraints of the inference:

> SYSTEM_PROMPT="Follow these rules: 1) Your job is to summarize data inputs into bullet points. 2) Be concise. 3) Always show most important information as the top bullet point. 4) Emphasize important parts in bold using Markdown. 5) Companies, names and proper nouns should be in italic using Markdown. 6) Never write more than five bullet points. 7) The bullet points, bold and italic should be formatted using Markdown."

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

# License

Apache License 2.0
