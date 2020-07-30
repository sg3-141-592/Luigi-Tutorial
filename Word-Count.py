import pickle
import requests
import luigi
from bs4 import BeautifulSoup
from collections import Counter

NUM_BOOKS = 10
REPLACE_LIST = """.,"';_[]:*"""

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
            resultCounter = 0
            for result in listTop.select("li>a"):
                if "/ebooks/" in result["href"]:
                    resultCounter += 1
                    f.write(
                        "http://www.gutenberg.org/{link}.txt.utf-8\n".format(
                            link=result["href"]
                        )
                    )
                    if resultCounter >= NUM_BOOKS:
                        break


class DownloadBooks(luigi.Task):
    def requires(self):
        return GetTopBooks()

    def output(self):
        outputTargets = []
        for i in range(NUM_BOOKS):
            outputTargets.append( luigi.LocalTarget("data/downloads/{}.txt".format(i)) )
        return outputTargets

    def run(self):
        with self.input().open("r") as i:
            for i, line in enumerate(i.read().splitlines()):
                with self.output()[i].open("w") as outfile:
                    resp = requests.get(line)
                    filtered_text = resp.text
                    for char in REPLACE_LIST:
                        filtered_text = filtered_text.replace(char, " ")
                    outfile.write(filtered_text)


class CountWords(luigi.Task):
    fileId = luigi.Parameter()

    def requires(self):
        return DownloadBooks()

    def output(self):
        return luigi.LocalTarget(
            "data/counts/count_{}.pickle".format(self.fileId), format=luigi.format.Nop
        )

    def run(self):
        with open("data/downloads/{}.txt".format(self.fileId)) as file:
            word_count = Counter(file.read().split())
            with self.output().open("w") as outfile:
                pickle.dump(word_count, outfile)


class ConCat(luigi.Task):
    def requires(self):
        requiredInputs = []
        for i in range(NUM_BOOKS):
            requiredInputs.append( CountWords(fileId=i) )
        return requiredInputs

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
