# import libraries
import feedparser
import json

# import local functions and libraries
from JobPost import JobPost
from Queries import Queries


class UpWorkRSS:

    categories_skills = json.load(open("data/categories-and-skills.json"))
    categories = categories_skills['Categories']
    skills = categories_skills['Skills']
    urls = []

    def __init__(self, profile_path):
        self.profile = json.load(open(profile_path))
        self.digest()

    def digest(self):
        ''' Digest rss.txt and turn it into variable before use it as url parameter'''

        with open("data/rss.txt",encoding='utf-8') as f:
            params = f.read().split("?")[1].split("&")
            params = {v.split("=")[0]:v.split("=")[1] for v in params}

        for key in self.profile:
            if key == "queries":
                for v in self.profile[key]:
                    url = Queries(
                        payload=params,
                        q=v
                    )
                    self.urls.append(url.construct())

            elif key == "title":
                for v in self.profile[key]:
                    url = Queries(
                        payload=params,
                        title=v
                    )
                    self.urls.append(url.construct())

            elif key == "skills":
                for v in self.profile[key]:
                    skill = self.skills[v]
                    url = Queries(
                        payload=params,
                        ontology_skill_uid=skill
                    )
                    self.urls.append(url.construct())

            elif key == "categories":
                categories = []
                for v in self.profile[key]:
                    category = self.categories[v]
                    categories.append(str(category))
                url = Queries(
                    payload=params,
                    subcategory2_uid=",".join(categories)
                )
                self.urls.append(url.construct())

    def get(self):
        '''Make a GET request to UpWork RSS'''

        # continue parse the rss url
        for url in self.urls:
            results = feedparser.parse(url)
            for entry in results['entries']:
                job = JobPost(entry)
                job.insert()


if __name__ == "__main__":

    # collecting job post based on rss custom profile
    rss = UpWorkRSS("profile/scraping.json")
    rss.get()