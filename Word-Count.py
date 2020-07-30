import requests
import luigi
from bs4 import BeautifulSoup
from collections import Counter

class GetTopBooks(luigi.Task):
    def output(self):
        return luigi.LocalTarget("data/topBooks.txt")

    def run(self):
        resp = requests.get("http://www.gutenberg.org/browse/scores/top")
        soup = BeautifulSoup(resp.content, "html.parser")
        # Get the header from the page
        pageHeader = soup.find_all("h2", string="Top 100 EBooks yesterday")[0]
        listTop = pageHeader.find_next_sibling("ol")
        with self.output().open("w") as f:
            for result in listTop.select("li>a"):
                if "/ebooks/" in result["href"]:
                    f.write(
                        "http://www.gutenberg.org/browse/scores{link}\n".format(
                            link=result["href"]
                        )
                    )


class DownloadBooks(luigi.Task):
    def requires(self):
        return GetTopBooks()

    def output(self):
        return luigi.LocalTarget("data/results.txt")

    def run(self):
        with self.input().open("r") as i:
            for i, line in enumerate(i.read().splitlines()):
                resp = requests.get(line)
        with self.output().open("w") as f:
            f.write("Hi")

class CountWords(luigi.Task):
    fileId = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget("data/count_{}.txt".format(self.fileId))
    
    def run(self):
        with open("data/{}.txt".format(self.fileId)) as file:
            word_count = Counter(file.read().split())
            with self.output().open("w") as f:
                for item in word_count.items():
                    f.write("{}\t{}\n".format(*item))

