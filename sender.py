import requests
from bs4 import BeautifulSoup

from config import *
from utils import *

URL_API = "https://cubox.pro/c/api/v2"

def cubox_concat_header():
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    return headers


def gen_post_cubox_data(url_save):
    r_save = requests.get(url_save)
    soup = BeautifulSoup(r_save.content, "lxml")

    # get title
    title = soup.title.text
    if title == "":
        title_meta = soup.find("meta", dict(property="og:title"))
        if title_meta is not None:
            title = title_meta['content']

    # get description
    description = soup.find("meta", dict(name="description")) or ""
    if description != "":
        description = description['content']

    data = dict(
        type=0,  # url type
        title=title,
        description=description,
        targetURL=url_save,
    )
    return data

def _check_dulplicate(url: str) -> bool:
    r_cubox = cubox_inbox()
    exist_urls = [x['targetURL'] for x in r_cubox.json()['data']]
    return url in exist_urls

def cubox_new(url_save):
    if _check_dulplicate(url_save):
        print("[Warn] dulplicate url")
        return None
    _url_cubox_new = f"{URL_API}/search_engine/new"

    data_cubox = gen_post_cubox_data(url_save)
    headers_cubox = cubox_concat_header()

    r_cubox = requests.post(_url_cubox_new, data=data_cubox, headers=headers_cubox)
    return r_cubox

def cubox_inbox(filters='', page=1, asc=False, archiving=False):
    _url_cubox_inbox = f"{URL_API}/search_engine/inbox?asc={bool_str(asc)}&page={page}&filters={filters}&archiving={bool_str(archiving)}"
    print(_url_cubox_inbox)
    r_cubox = requests.get(_url_cubox_inbox, headers=cubox_concat_header())
    return r_cubox
    