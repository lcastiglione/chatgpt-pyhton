# Import
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary
import webbrowser
from dotenv import load_dotenv
import os

load_dotenv()

# Config
cloudinary.config(
  cloud_name = "dmiwlqoki",
  api_key = os.getenv('API_KEY_CLOUD'),
  api_secret = os.getenv('API_SECRET_CLOUD'),
  secure = True
)

def transform_image():
    # Upload
    upload("assets/image.jpg", public_id="image")

    # Transform
    url, options = cloudinary_url("image", width=1000, height=1000, crop="thumb", gravity="auto", radius=20)
    webbrowser.open(url, new=2)