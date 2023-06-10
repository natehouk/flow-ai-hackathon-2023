from datetime import datetime
import openai
import os
from streaming.models import Prompts
from streaming.config import SYSTEM_PROMPT

# print the chat completion
def get_prompt(prompt):
	last_object = Prompts.objects.last()

	# openai.api_key = "sk-"
	openai.api_key = os.environ.get("OPENAI_API_KEY", "sk-")
	print(os.environ.get("OPENAI_API_KEY", "sk-"))
	chat_completion = openai.ChatCompletion.create(
	    model="gpt-3.5-turbo", messages=[
	    	{"role": "system", "content": SYSTEM_PROMPT},
	    	{"role": "user", "content": f"{prompt} \n {last_object.value}"}
	    ], 
	    max_tokens = 100,
	)
	
	return chat_completion.choices[0].message.content
	# return prompt
