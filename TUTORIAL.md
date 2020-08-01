### Introduction
In this tutorial we will build a data processing pipeline to analyse the most common words from the popular books on [Project Gutenburg](https://www.gutenberg.org/). To do this we will be building our pipeline using the **Luigi** package.

**Luigi** is a Python package that is used to manage long running batch processes. Luigi allows us to define a data processing job as a graph of tasks. For example Step B depends on the output of Step A. And Step D depends on the output of Step B and Step C. 

Luigi gives us features like visualisation of our data processing pipeline and handling of failures out of the box.

By using a managed batch runner you can easily visualise your data pipeline. Manage errors. Re-run 

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
