import openai
import re


def chat_loop():
    prompt = ""
    context = ""

    while True:
        prompt = input(">>")
        if prompt == 'exit':
            break
        print(context + "Nueva pregunta: " + prompt)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=4000,  # Toma en cuenta el prompt y la respuesta
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print(response["choices"][0]["text"] + "\n")
        context += f"Pregunta anterior: {prompt}\n"


def gpt3(prompt, model='text-davinci-003', response_length=1000,
         temperature=0.7, top_p=1, frequency_penalty=0, presence_penalty=0,
         start_text='', restart_text='', stop_seq=[]):
    print(prompt)
    response = openai.Completion.create(
        prompt=prompt + start_text,
        model=model,
        max_tokens=response_length,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop_seq,
    )
    answer = response.choices[0]['text']
    new_prompt = prompt + start_text + answer + restart_text
    return answer, new_prompt
