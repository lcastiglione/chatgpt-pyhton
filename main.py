import openai
from dotenv import load_dotenv
import os
import re

load_dotenv()

openai.api_key = os.getenv('API_KEY')

topic = "demo"
prompt = ""
context = ""
history_log = 'history/' + re.sub('[^0-9a-zA-Z]+', '', topic) + '.log'
file = open(history_log, "a")

while True:
    print(">>")
    prompt = input()
    if prompt == 'exit':
        break
    print(len(context + "\n\n"+ prompt))
    file.write(prompt)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=context + "\n\n"+ prompt,
        temperature=0.7,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    file.write(response["choices"][0]["text"] + "\n")
    print(response["choices"][0]["text"] + "\n")
    context += "\n".join([context, prompt, response["choices"][0]["text"]])

file.close()


