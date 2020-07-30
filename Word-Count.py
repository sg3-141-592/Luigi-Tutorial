import pickle
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
        return luigi.LocalTarget(
            "data/count_{}.pickle".format(self.fileId), format=luigi.format.Nop
        )

    def run(self):
        with open("data/{}.txt".format(self.fileId)) as file:
            word_count = Counter(file.read().split())
            with self.output().open("w") as outfile:
                pickle.dump(word_count, outfile)


class ConCat(luigi.Task):
    def requires(self):
        return [CountWords(fileId=1), CountWords(fileId=2), CountWords(fileId=3)]

    def output(self):
        return luigi.LocalTarget("data/summary.txt")

    def run(self):
        counters = Counter()
        for input in self.input():
            with input.open("rb") as infile:
                nextCounter = pickle.load(infile)
                counters += nextCounter
        #
        with self.output().open("w") as f:
            for item in counters.items():
                f.write("{}\t{}\n".format(*item))
