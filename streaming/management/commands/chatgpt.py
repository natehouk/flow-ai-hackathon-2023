from datetime import datetime
import openai
import os
from streaming.models import Prompts
import markdown

# print the chat completion
def get_prompt(transcript):
	last_object = Prompts.objects.last()

	openai.api_key = os.environ.get("OPENAI_API_KEY")
	gpt_model = os.environ.get("GPT_MODEL", "gpt-3.5-turbo")
	system_prompt =  os.environ.get("SYSTEM_PROMPT", "Follow these rules: 1) Your job is to summarize data inputs into bullet points. 2) Be concise. 3) Always show most important information as the top bullet point. 4) Emphasize important parts in bold using Markdown. 5) Companies, names and proper nouns should be in italic using Markdown. 6) Never write more than five bullet points. 7) The bullet points, bold and italic should be formatted using Markdown.")
	user_prompt = last_object.value
	print(f"{system_prompt} 8) {user_prompt}")
	chat_completion = openai.ChatCompletion.create(
	    model=gpt_model, messages=[
	    	{"role": "system", "content": f"{system_prompt} 8) {user_prompt}"},
	    	{"role": "user", "content": f"{transcript}"},
	    ], 
	)
	result = chat_completion.choices[0].message.content
	print(result)

	# # convert markdown to html
	html = markdown.markdown(result)

	return html