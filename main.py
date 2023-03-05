import openai
from dotenv import load_dotenv
import os
#from setup.functions.audio import get_text_by_audio
from setup.functions.cloudinary import transform_image


load_dotenv()
openai.api_key = os.getenv('API_KEY')



#getImg("tanks",n=10)
#getVariationImg('assets/2.png',n=10)
#get_edit_image("Family on a beach smiles with a background of turtles", 'assets/1.png', 'assets/mask.png')
#chat_loop()

'''
def chat():
    prompt = "Humano: "
    while True:
        v = input('>>: ')
        if v == 'exit':
            break
        prompt+=v
        answer, prompt = gpt3(prompt,
                              temperature=0.9,
                              frequency_penalty=1,
                              presence_penalty=1,
                              start_text='\nAI:',
                              restart_text='\nHumano: ',
                              stop_seq=['\nHumano:', '\n'])
        print('GPT-3:' + answer)


if __name__ == '__main__':
    chat()
'''
#get_text_by_audio("assets/test.mp3")
transform_image()