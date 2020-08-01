### Introduction
In this tutorial we will build a data processing pipeline to download the most popular books from Project Gutenburg and analyse the most common words in them.

We will build this using the Python library Luigi. Luigi allows us to define a data processing job as a graph of tasks. Luigi gives us features like visualisation of our process, handling of failures

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
