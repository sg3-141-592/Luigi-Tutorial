I found it from a Hacker News article about writing for LWN. In the comments someone linked to a Github repo of businesses who pay for technical writing https://github.com/sixhobbits/technical-writing/blob/master/write-for-us.md . I found Digital Ocean in this repo.

--------------

How To Build a Data Processing Pipeline using Luigi on Python 3

--------------

The framework in this tutorial is a powerful and optimised way of producing and managing a data processing pipeline. It was developed by Spotify to solve its own internal data processing needs

The package is a popular solution (see Github https://github.com/spotify/luigi stars and activity) and is being used by major companies to solve real problems (see https://luigi.readthedocs.io/en/stable/index.html "Who uses Luigi?").

The need to connect to many data sources and aggregate data is a common one. And a developer who can utilise frameworks to help them complete this task, will be able to do it quicker in a more reliable and manageable way.

There are currently no tutorials of the major batch pipeline platforms (Luigi and Airflow) for Python on Digital Ocean currently. 

------------------

## Step 1 — Installing Luigi

In this step we will build a virtual environment for this tutorial, and download the latest version of the Luigi package.

## Step 2 — Creating a Luigi Task

In this step we will create a "Hello World" Luigi Task to demonstrate how they work.

## Step 3 — Creating a Task to get a List of Books

In this step we will create a Task to download a list of books of popular books. This will be a data-source for our pipeline.

## Step 4 — Running the Luigi Scheduler

In this step we will launch the Luigi scheduler, and learn the concepts behind the Luigi execution model. You will take your task developed in Step 3, and run it using the Luigi scheduler.

### Step 5 — Downloading the Books

In this step you will create a Luigi task to download a specified book. You will define a dependency between this newly created task, and the task created in step 3. You will visualise the execution of the task within the Luigi interface.

### Step 6 — Counting words and Summarising Results

In this step you will create a Luigi task to count the frequency of words in each of the books downloaded in Step 4. You will create a Luigi task to aggregate and summarise the most frequent words across all books analysed.

### Step 7 — Defining Configuration Parameters

In this step you will add configuration parameters to your tasks to allow you customise how many books to analyse, and the number of words to include in the results.

------------------

I'm a specialist for a major engineering company who specialises in software development ways of working. Especially Python, Cloud and DevOps. I've got just over a decade of professional development experience.

For this tutorial, this is a framework I've introduced into my own company for our internal data processing tooling. I think its a powerful and useful framework for what is a common problem people are trying to solve.

----------------------------

I work as a Specialist for a major engineering company https://www.linkedin.com/in/sean-gilligan-34923429 where I specialise in cloud and DevOps.

I've recently started contributing to open source and have some minor fixes to popular Django Libraries and some cloud security tooling https://github.com/sg3-141-592?tab=repositories

I've got my own site. I've not written many articles yet https://www.dishy.dev/ but you can play Yatzy on there.

My motivation for applying to write is a personal challenge for me To see whether I can get my writing to a level where I can get it published on a major site. 