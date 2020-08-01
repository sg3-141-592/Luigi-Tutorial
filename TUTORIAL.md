### Introduction
In this tutorial we will build a data processing pipeline to analyse the most common words from the most popular books on [Project Gutenburg](https://www.gutenberg.org/). To do this we will be building our pipeline using the [**Luigi**](https://luigi.readthedocs.io/en/stable/index.html) framework.

Luigi is a Python package that manages long running batch processes. It allows us to define a data processing job as a graph of tasks. For example Task B depends on the output of Task A. And Task D depends on the output of Task B and Task C.  Luigi automatically works out what Tasks to it needs to run to complete a requested job.

Luigi gives us a powerful framework to develop and manage data processing pipelines. It provides visualisation of our pipeline, parallelisation of tasks, handling of failures and selective re-execution of the pipeline.

In this guide, we will install and implement a Luigi batch job on Ubuntu 20.04.

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

### Getting Number of Books
A. We show the user they can interrogate the 

### Setting Parameters
A

### Downloading the Books
A

### Analysing the Most Frequent Words

### Conclusion
