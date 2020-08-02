### Introduction
In this tutorial we will build a data processing pipeline to analyse the most common words from the most popular books on [Project Gutenburg](https://www.gutenberg.org/). To do this we will be building our pipeline using the [**Luigi**](https://luigi.readthedocs.io/en/stable/index.html) package.

Luigi is a Python package that manages long running batch processes. It allows us to define a data processing job as a graph of tasks. For example Task B depends on the output of Task A. And Task D depends on the output of Task B and Task C.  Luigi automatically works out what Tasks to it needs to run to complete a requested job.

Luigi gives us a powerful framework to develop and manage data processing pipelines. It provides visualisation of our pipeline, parallelisation of tasks, handling of failures and selective re-execution of the pipeline.

In this guide, we will implement a Luigi batch job in Python 3. 

### Pre-requisites
- Python 3.6 or higher and ```virtualenv``` installed. Follow [How To Install Python 3 on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server) to configure Python and ```virtualenv```.


## Installating Luigi

For this tutorial I've used a VirtualEnvironment. There's a 
``` bash
sudo apt update
sudo apt -y upgrade
apt-get install python3-venv
```

``` bash
sudo apt install -y python3-pip
```

``` bash
python3 -m venv venv
. venv/bin/activate
```

``` bash
pip install wheel
pip install luigi
```

``` bash
sudo ufw allow 8082
```

### Running the Luigi Scheduler
Simple tasks can be run using the ```--local-scheduler``` argument.

Tasks are run as a one off using the ```--local-scheduler``` argument.

In production we use the Luigi daemon. This gives a central point for running our pipelines and provides visualisation of them. 

## Step 1 — Installing Luigi
In this step, we'll create a virtual environment to provide a clean sandbox environment to install Luigi into.

First, create a project directory. For this tutorial we'll call it ```luigi-demo```:

``` bash
mkdir luigi-demo
```

Navigate into the newly created ```luigi-demo``` directory:

``` bash
cd luigi-demo
```

Create a new virtual environment ```luigi-venv```:

``` bash
python3 -m venv luigi-venv
```

And activate the newly created virtual environment.

``` bash
. luigi-venv/bin/activate
```

You see ```(luigi-venv)``` appended to the front of your terminal to indicate which virtual environment is active.

``` bash
(luigi-venv)username@hostname:~/luigi-demo$
```

For this tutorial we will need three libraries, ```luigi```, ```beautifulsoup4``` and ```requests```. Run the following command to install these libraries using pip:

``` bash
pip install luigi beautifulsoup4 requests
```

You will get a response that the latest verisons of the libraries and all of their dependencies have been installed.

``` bash
Successfully installed beautifulsoup4-4.9.1 certifi-2020.6.20 chardet-3.0.4 docutils-0.16 idna-2.10 lockfile-0.12.2 luigi-3.0.1 python-daemon-2.2.4 python-dateutil-2.8.1 requests-2.24.0 six-1.15.0 soupsieve-2.0.1 tornado-5.1.1 urllib3-1.25.10
```

## Step 2 - Creating a Luigi Task
In this step we will create a "Hello World" Luigi Task to demonstrate their concepts. A Luigi Task is where the execution of our pipeline and the definition of dependencies takes place.

Create a new file ```hello-world.py```, and insert the following code.

``` python
import luigi

class HelloLuigi(luigi.Task):

    def output(self):
        return luigi.LocalTarget('hello-luigi.txt')

    def run(self):
        with self.output().open("w") as outfile:
            outfile.write("Hello Luigi!")

```

We can create classes that follow the 

The ```output()``` method defines one or more ```Target``` objects that our task produces. A target is a data source we are connecting to. In the case of this demo, we define a ```luigi.LocalTarget```, which is a local file. 

Luigi allows you to connect to a variety of common data sources including [AWS S3 buckets](https://luigi.readthedocs.io/en/stable/api/luigi.contrib.s3.html), [MongoDB databases](https://luigi.readthedocs.io/en/stable/api/luigi.contrib.mongodb.html) and [SQL databases](https://luigi.readthedocs.io/en/stable/api/luigi.contrib.sqla.html).

You can find a complete list of supported data sources [here](https://luigi.readthedocs.io/en/stable/api/luigi.contrib.html).

The ```run()``` method contains the code we want to execute for our pipeline stage. For this example we are taking the output target we defined, and writing "Hello Luigi!" to.

To execute the new function run the following command

``` bash
python -m luigi --module hello-world HelloLuigi --local-scheduler
```

For the ```--module hello-world HelloLuigi``` flag we tell Luigi which Python module and Luigi Task to execute.

The ```--local-scheduler``` flag tells Luigi to not connect to a Luigi scheduler daemon, and instead execute this task locally. Running tasks using the ```local-scheduler``` flag is only recommended for testing.

We run using ```python -m``` instead of executing luigi directly as Luigi can only execute code that is with the current PYTHONPATH. 



## Step 2 - Getting List of Books
In this step we will create a Python script to download a list of books, and run it as a Luigi task.

Create a new file ```word-frequency.py```, and insert the following code. The following code uses the requests library to download the contents of the top most read books on [Project Gutenberg](http://www.gutenberg.org).

``` python
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
            print(GlobalParams.NUMBER_BOOKS)
            if resultCounter >= GlobalParams().NUMBER_BOOKS:
                break
```