from bs4 import BeautifulSoup
from playsound import playsound
from gtts import gTTS
import requests


def read_it(text):
    """
    Use Google's free text to speech to read text.
    - Note that it appears to max out at 5000 characters at a time.
    """

    tts = gTTS(text=text, lang="en-ie")  # gtts-cli --all
    tts.save("readit.mp3")
    playsound("readit.mp3")


def get_article(url):
    """Super simple search for <p> tags and then sends content to read_it()."""
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    para = soup.findAll("p")
    for p in para:
        read_it(p.text)


if __name__ == "__main__":
    url = r"https://www.nytimes.com/2019/05/18/arts/television/game-of-thrones-season-8.html"
    get_article(url)
