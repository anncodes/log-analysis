# Logs Analysis Project
Udacity Full Stack Nanodegree

A reporting tool that prints out reports in plain text based on the data in the database.

The reporting tool answers the following examples:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Getting Started

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
2. Clone this repository to your local machine.
3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip. Move 'newsdata.sql' into the **vagrant** directory.
4. Start the virtual machine.
From the terminal in the folder where vagrant is installed:
'vagrant up' to start the virtual machine.
'vagrant ssh' to log into the virtual machine.
'cd /vagrant' to change to the vagrant directory.
'psql -d news and -f newsdata.sql' to load the data and create tables.


### Create views  

View to get the total requests.

```
CREATE VIEW requests 
AS SELECT date(time) 
AS date, count(*) AS total 
FROM log 
GROUP BY date;
```

View to get the total requests that returned errors.

```
CREATE VIEW err_requests 
AS SELECT date(time) as date, count(*) AS total 
FROM log 
WHERE status = '404 NOT FOUND' 
GROUP BY date 
ORDER BY total;
```


### Run the reporting tool

Make sure that you are in the directory where your files and vagrant are.

```
python3 newslog.py 
```
