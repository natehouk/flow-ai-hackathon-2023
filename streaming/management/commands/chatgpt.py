from datetime import datetime
import openai
from streaming.models import Prompts

# print the chat completion
def get_prompt(prompt):
	last_object = Prompts.objects.last()

	openai.api_key = "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"
	chat_completion = openai.ChatCompletion.create(
	    model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{prompt} \n {last_object.value}"}], max_tokens = 100,
	)
	
	return chat_completion.choices[0].message.content
	# return prompt
