import openai
import re


def chat_loop():
    prompt = ""
    context = ""

    while True:
        prompt = input(">>")
        if prompt == 'exit':
            break
        print(context + "Nueva pregunta: "+ prompt)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt+ "\n",
            temperature=0.7,
            max_tokens=4000, #Toma en cuenta el prompt y la respuesta
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print(response["choices"][0]["text"] + "\n")
        context += f"Pregunta anterior: {prompt}\n"