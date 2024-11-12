# пример использования библиотеки pillow
from PIL import Image, ImageDraw, ImageFont
import glob
import datetime

#  создание миниатюр всех jpg-файлов в текущей директории с проставлением текущей даты и сохранением в png формате
MAX_SIZE = (500, 500)
filenames = glob.glob('*.jpg')

for filename in filenames:
    img = Image.open(filename)
    font = ImageFont.truetype("arial.ttf", size=20)
    draw = ImageDraw.Draw(img)
    bbox = (0, 0, 102, 22)
    draw.rectangle(bbox, fill='black')
    draw.text((0, 0), f'{datetime.datetime.now().date()}', font=font, fill='white')
    img.thumbnail(MAX_SIZE)
    img.save(filename.replace('.jpg', '_mini.png'), 'png')


import matplotlib.pyplot as plt
#  пример использования библиотеки matplotlib
labels = ['Facebook', 'Instagram', 'YouTube', 'Linkedin', 'Twitter', 'Reddit']
part_one = [28, 24, 18, 18, 14, 6]
part_two = [72, 76, 82, 82, 86, 94]

width = 0.35
fig, ax = plt.subplots()

ax.bar(labels, part_one, width)
ax.bar(labels, part_two, width, bottom=part_one)

ax.set_ylabel('Соотношение, в %')
ax.set_title('Количество рекламы в разных приложениях')

plt.show()


#  пример использования библиотеки requests
from requests import get, ConnectionError

params = {"ll": "37.620070,55.753630",
          "spn": "0.01,0.006",
          "l": "map"}

try:
    response = get("https://static-maps.yandex.ru/1.x/", params=params)
except ConnectionError:
    print("Проверьте подключение к сети.")
else:
    with open("map.png", "wb") as file:
        file.write(response.content)
