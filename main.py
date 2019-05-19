
import itertools

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

    # Girlfriendguidetohealth
    msos = soup.findAll("div", {"class": "MsoNormal"})

    # Average page
    para = soup.findAll("p")

    for p in itertools.chain(msos, para):
        text = p.text.strip().replace("\n", " ")
        print(text)
        if len(text) > 0:
            read_it(text)


if __name__ == "__main__":
    # url = r"https://www.nytimes.com/2019/05/18/arts/television/game-of-thrones-season-8.html"
    # url = r"https://medium.com/tenable-techblog/stealing-downloads-from-slack-users-be6829a55f63"
    url = r"https://www.derrickreimer.com/essays/2019/05/17/im-walking-away-from-the-product-i-spent-a-year-building.html"
    # url = r"https://www.reuters.com/article/us-health-heart-aspirin/without-heart-disease-daily-aspirin-may-be-too-risky-idUSKCN1SJ275"
    # url = r"http://www.girlfriendguidetohealth.com/2013/12/oh-holy-shit.html"
    get_article(url)
