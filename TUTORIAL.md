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

For this tutorial we will need three libraries, ```luigi```, ```beautifulsoup4``` and ```requests```. Run the following command to install these libraries with pip:

``` bash
pip install luigi beautifulsoup4 requests
```

## Step 2 - Getting List of Books
In this step we will create a Python script to download a list of books, and run it as a Luigi task. 