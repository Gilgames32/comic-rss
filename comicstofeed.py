import json
import os
import sys
from feedgen import FeedGenerator

# FIXME prolly a bad idea for github actions
os.chdir(sys.path[0])


class ComicSeries:
    contentpath = "./content"

    def __init__(self, title = None, link = None, desc = None) -> None:
        self.title = title
        self.link = link
        self.desc = desc
        self.chapters = []
        pass

    def load_meta(self, name = "meta.json"):
        with open(os.path.join(self.contentpath, name), "r") as f:
            meta = json.load(f)
            self.title = meta["title"]
            self.link = meta["link"]
            self.desc = meta["description"]

    def load_entries(self):
        for i in os.listdir(self.contentpath):
            ipath = os.path.join(self.contentpath, i)
            if os.path.isdir(ipath):
                for j in os.listdir(ipath):
                    if j.endswith(".json"):
                        print(i, j)
                        with open(os.path.join(ipath, j)) as f:
                            # TODO
                            pass


c = ComicSeries()
c.load_meta()
print(c.title)