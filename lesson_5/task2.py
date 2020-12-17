import requests
from threading import Thread
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args):
        t = Thread(target=func, args=args, name="Thread", daemon=False)
        t.start()
        return t

    return wrapper

@decorator
def download(urls):
    for i in range(len(urls)):
        print(f"Downloading a file by link number {i + 1}")
        r = requests.get(urls[i])
        with open(f"github{i + 1}.zip", "wb") as code:
            code.write(r.content)
        print("Downloaded")

urls = ['https://github.com/Vitalik39/itea_october/archive/master.zip',
        'https://codeload.github.com/fogleman/Minecraft/zip/master',
        'https://github.com/antonplkv/itea-october/archive/master.zip',
        'https://github.com/Vitalik39/itea_october/archive/master.zip',
        'https://codeload.github.com/fogleman/Minecraft/zip/master',
        'https://github.com/antonplkv/itea-october/archive/master.zip',
        'https://github.com/Vitalik39/itea_october/archive/master.zip',
        'https://codeload.github.com/fogleman/Minecraft/zip/master',
        'https://github.com/antonplkv/itea-october/archive/master.zip',
        'https://github.com/Vitalik39/itea_october/archive/master.zip']

download(urls)
