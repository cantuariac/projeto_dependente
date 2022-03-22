from colored import fore, style
from PIL import Image
import requests
from io import BytesIO

print(fore.GREEN)
print('If I have vulnerable code you ask?', style.RESET)
input('<press enter>')

print(fore.GREEN)
print(f'Well, it {style.BOLD} depends', style.RESET)
input('<press enter>')

print(fore.GREEN)
print('Here is an image...', style.RESET)
input('<press enter>')

response = requests.get('https://i.kym-cdn.com/entries/icons/mobile/000/025/817/Screen_Shot_2018-03-30_at_11.34.27_AM.jpg')
img = Image.open(BytesIO(response.content))
img.show()
