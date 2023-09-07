import requests
from bs4 import BeautifulSoup
from mail import send_email


def get_last_person():
    response=requests.get(url="https://en.wikipedia.org/wiki/Deaths_in_2023")
    bs = BeautifulSoup(response.text, 'html.parser')
    last_person = bs.find(id="bodyContent").find_all('ul')[1].li
    
    return last_person
    
def get_link(url):
    response = requests.get(url=url)
    bs = BeautifulSoup(response.text, 'html.parser')
    try:link=bs.find(string="Русский").parent.parent.attrs['href']
    except:link=url
    
    finally:return link

def get_paragraph(url):
    response = requests.get(url=url)
    bs = BeautifulSoup(response.text, 'html.parser')
    paragraph = bs.findAll(
                lambda tag:tag.name == "p" and
                len(tag.attrs) == 0
    )[0]
    
    for i in paragraph.select('sup'):#Удаление спец символов
        i.decompose()
    
    s_clear = u"".join([c for c in paragraph.get_text() if ord(c) != 769])#Удаление ударений
    
    return s_clear


def parsing(last_person):
    link=get_link(f"https://en.wikipedia.org{last_person.a.attrs['href']}")
    paragraph=get_paragraph(link)
    send_email(text=link+"\n"+paragraph)
    # print(link,paragraph)


if __name__ == "__main__":
    response=requests.get(url="https://en.wikipedia.org/wiki/Deaths_in_2023")
    bs = BeautifulSoup(response.text, 'html.parser')
    last_person = bs.find(id="bodyContent").find_all('ul')[1].li
    parsing(last_person)
    