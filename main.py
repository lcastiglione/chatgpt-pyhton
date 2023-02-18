import openai
from dotenv import load_dotenv
import os
import re
import webbrowser
import requests
from PIL import Image
from io import BytesIO
import shutil

load_dotenv()

openai.api_key = os.getenv('API_KEY')

def save_img(url, option='browser'):
    if option=='browser':
        webbrowser.open(url, new=2)
    elif option=='file':
        _, query_string = url.split('?')
        params  = dict(param.split('=') for param in query_string.split('&'))
        print(params)
        file_name=os.path.join('assets/res', f"{params['sig'].replace('/','')}.png")
        res = requests.get(url)
        with open(file_name,'wb') as f:
            f.write(res.content)
        #edited_image = Image.open(requests.get(url, stream = True).raw)
       # edited_image.save(file_name, "PNG")



def chat():
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

def getImg(prompt,n=1):
    response = openai.Image.create(
        prompt=prompt,
        n=n,
        size="512x512"
    )
    return [save_img(r['url'], option='file') for r in response['data']]

def getVariationImg(img,n=1):
    response = openai.Image.create_variation(
        model="image-alpha-001",
        image=open(img, "rb"),
        n=n,
        size="256x256"
    )
    print(response['data'])
    return [save_img(r['url'], option='file') for r in response['data']]

def get_edit_image(prompt, img,mask):
    response = openai.Image.create_edit(
    model='dall-e-2',
    image=open(img, "rb"),
    mask=open(mask, "rb"),
    noise=1,
    prompt=prompt,
    n=10,
    size="1024x1024"
    )
    return [webbrowser.open(r['url'], new=2) for r in response['data']]


getImg("lionel messi hiperrealista",n=10)
#getVariationImg('assets/2.png',n=10)
#get_edit_image("Family on a beach smiles with a background of turtles", 'assets/1.png', 'assets/mask.png')

