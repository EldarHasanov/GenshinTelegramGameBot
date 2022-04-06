from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request

from datetime import datetime

start_time = datetime.now()




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

#url = "https://genshin.honeyhunterworld.com/db/char/characters/?lang=EN"
req =  Request('https://genshin.honeyhunterworld.com/db/char/characters/?lang=EN', headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
soup = BeautifulSoup(html, features="html.parser")

textMes = ''
for script in soup(["script", "style"]):
    script.extract()

for text in soup.find_all("span", class_="sea_charname"):
    if text.get_text() != "Traveler":
        Name = text.get_text().split()
        if len(Name) == 2 and len(Name[0]) > 3:
            textMes += ('\n' + Name[1].lower())
        else:
            Temp = ''.join(Name)
            textMes += ('\n' + Temp.lower())

f = open('names.txt', 'w')
f.write (textMes)
f.close

print(datetime.now() - start_time)