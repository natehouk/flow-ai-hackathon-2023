from datetime import datetime
import openai
import os
from streaming.models import Prompts
import markdown

# print the chat completion
def get_prompt(prompt):
	last_object = Prompts.objects.last()

	openai.api_key = os.environ.get("OPENAI_API_KEY")
	gpt_model = os.environ.get("GPT_MODEL", "gpt-3.5-turbo")
	system_prompt =  os.environ.get("SYSTEM_PROMPT")
	chat_completion = openai.ChatCompletion.create(
	    model=gpt_model, messages=[
	    	{"role": "system", "content": system_prompt},
	    	{"role": "user", "content": f"{prompt} \n {last_object.value}"},
	    ], 
	)
	result = chat_completion.choices[0].message.content
	
	# convert markdown to html
	html = markdown.markdown(result)

	return html