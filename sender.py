import requests
from bs4 import BeautifulSoup

from config import *


def cubox_concat_header():
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    return headers


def gen_post_cubox_data(url_save):
    r_save = requests.get(url_save)
    soup = BeautifulSoup(r_save.content, "lxml")

    # wechat url
    author = soup.find("meta", dict(name="author"))['content']
    title = soup.find("meta", dict(property="og:title"))['content']
    description = soup.find("meta", dict(name="description"))['content']

    data = dict(
        type=0,  # url type
        title=title,
        description=description,
        targetURL=url_save,
    )
    return data


def cubox_new(url_save):
    _url_cubox = "https://cubox.pro/c/api/v2/search_engine/new"

    data_cubox = gen_post_cubox_data(url_save)
    headers_cubox = cubox_concat_header()

    r_cubox = requests.post(_url_cubox, data=data_cubox, headers=headers_cubox)
    return r_cubox
