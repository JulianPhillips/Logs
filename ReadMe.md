#Logs Analysis Udacity
###Full Stack Development ND

## About
This project looks through a sql file and gives back the answers to these three questions
* 1. What are the most popular three articles of all time?
* 2. Who are the most popular article authors of all time? 
* 3. On which days did more than 1% of requests lead to errors?

## Prerequisites
* Python 3 (https://docs.python.org/3/download.html)
* Vagrant (https://www.vagrantup.com/downloads.html)
* VirtualBox  (https://www.virtualbox.org/wiki/Downloads)


## Steps 
* Run psql -d news -f newsdata.sql on the virtual machine /vagrant folder to create the database

### Write/Run these lines to create the necessary views:

'''create view access as
select to_char(time, 'Month, DD, YYYY') as date, count(status) as access
from log
group by date
order by date
'''

''' create view error as
select to_char(time, 'Month, DD, YYYY') as date, count(status) as error
from log
where status like '4%'
group by date
order by date
'''

''' create view rate_of_error as
select access.date, round(100.00 * error / access, 2) as rate
from access, error
where access.date = error.date
''' 

### After creating these views you can run python3 Logs.py to generate the logs analysis


## Built with
* Python3
* SQL
## Author
Julian Parker