
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

### A
We want to download the top books from Project Gutenburg and analyse the most common words in them.

Luigi allows us to build pipelines of data processing.

### Running the Luigi Scheduler
Simple tasks can be run using the ```--local-scheduler``` argument.

Tasks are run as a one off using the ```--local-scheduler``` argument.

In production we use the Luigi daemon. This gives a central point for running our pipelines and provides visualisation of them. 

### 1. Getting Number of Books

