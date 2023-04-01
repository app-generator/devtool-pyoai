import os, random, string
import openai
import requests

rnd = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 5 ))
openai.api_key = os.getenv("OPENAI_API_KEY")

img_info = input('Image Info : ')

res = openai.Image.create(prompt=img_info, n=2, size="1024x1024")

URL = res.data[0]['url']

response = requests.get(URL)

img_name = img_info.lower().replace(' ', '-')[:50] + '-' + rnd + '.png'

open(os.path.join('images', img_name), "wb").write(response.content)
