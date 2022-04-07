from datetime import datetime
from urllib.request import Request
from urllib.request import urlopen
import requests

from bs4 import BeautifulSoup

start_time = datetime.now()


def saveImage(name):
    stars = 0
    response = requests.get('https://genshin.honeyhunterworld.com/img/char/' + name + '_gacha_splash.png')
    req = Request('https://genshin.honeyhunterworld.com/db/char/'+ name + '/?lang=EN',
                  headers={'User-Agent': 'Mozilla/5.0'})

    html = urlopen(req).read()
    soup = BeautifulSoup(html, features="html.parser")

    wrape1 = soup.find("td", string="Rarity")
    wrape = wrape1.findNext("td")
    for star in wrape.find_all("div", class_="sea_char_stars_wrap"):
        stars += 1


    photo = open('C:/PythonProjects/Genshin/IntrestingStuff/GenshinTelegramGameBot/Resurses/Arts/Characters/' + str(stars) + 'star/' +name + '.png', "wb")
    photo.write(response.content)
    photo.close()

# url = "http://anekdotnow.ru/collection/50525.html"
# html = urlopen(url).read()
# soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements

# textMes = ''
# for script in soup(["script", "style"]):
# script.extract()    # rip it out

# for text in soup.find_all('br'):
#    textMes += (text.get_text())    # rip it out
# f.write (textMes)
# f.close
# bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


req =  Request('https://genshin.honeyhunterworld.com/db/char/characters/?lang=EN',
               headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
soup = BeautifulSoup(html, features="html.parser")

textMes = ''
for script in soup(["script", "style"]):
    script.extract()

for charect in soup.find_all("div", class_="char_sea_cont"):
    text = charect.find('a', href=True)
    Name = text['href']
    Name = Name.replace('/db/char/', '')
    Name = Name.replace('/?lang=EN', '')

    if len(Name.split('_')) == 1:
        textMes += ('\n' + Name)
        saveImage(Name)

f = open('names.txt', 'w')
f.write (textMes)
f.close

print(datetime.now() - start_time)


