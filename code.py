from colored import fore, style
from PIL import Image
import requests
from io import BytesIO
import numpy as np

print(fore.GREEN)
print('If I have vulnerable code you ask?', style.RESET)
input('<press enter>')

print(fore.RED)
print(f'Well, it {style.BOLD} depends', style.RESET)
input('<press enter>')

print(fore.BLUE)
print('Here is an image...', style.RESET)
response = requests.get('https://i.kym-cdn.com/entries/icons/mobile/000/025/817/Screen_Shot_2018-03-30_at_11.34.27_AM.jpg')
img = Image.open(BytesIO(response.content))
img.show()
input('<press enter>')

img = np.array(img)
print(img)
print(fore.YELLOW)
print('I turned it into an array for no reason', style.RESET)
input('<press enter>')

print('Good bye!')