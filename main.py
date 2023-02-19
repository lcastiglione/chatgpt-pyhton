import openai
from dotenv import load_dotenv
import os

from setup.chat.chat import chat_loop


load_dotenv()
openai.api_key = os.getenv('API_KEY')



#getImg("tanks",n=10)
#getVariationImg('assets/2.png',n=10)
#get_edit_image("Family on a beach smiles with a background of turtles", 'assets/1.png', 'assets/mask.png')
chat_loop()
