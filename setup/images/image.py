import openai
import os
import webbrowser
import requests


def save_img(url, option='browser'):
    if option == 'browser':
        webbrowser.open(url, new=2)
    elif option == 'file':
        _, query_string = url.split('?')
        params = dict(param.split('=') for param in query_string.split('&'))
        print(params)
        file_name = os.path.join(
            'assets/res', f"{params['sig'].replace('/','')}.png")
        res = requests.get(url)
        with open(file_name, 'wb') as f:
            f.write(res.content)
        # edited_image = Image.open(requests.get(url, stream = True).raw)
       # edited_image.save(file_name, "PNG")


def getImg(prompt, n=1):
    response = openai.Image.create(
        prompt=prompt,
        n=n,
        size="512x512"
    )
    return [save_img(r['url'], option='file') for r in response['data']]


def getVariationImg(img, n=1):
    response = openai.Image.create_variation(
        model="image-alpha-001",
        image=open(img, "rb"),
        n=n,
        size="256x256"
    )
    print(response['data'])
    return [save_img(r['url'], option='file') for r in response['data']]


def get_edit_image(prompt, img, mask):
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
