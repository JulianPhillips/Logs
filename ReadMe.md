Run psql -d news -f newsdata.sql on the virtual machine /vagrant folder to create the database

Write/Run these lines to create the necessary views:

create view access as
select to_char(time, 'Month, DD, YYYY') as date, count(status) as access
from log
group by date
order by date

create view error as
select to_char(time, 'Month, DD, YYYY') as date, count(status) as error
from log
where status like '4%'
group by date
order by date

create view rate_of_error as
select access.date, round(100.00 * error / access, 2) as rate
from access, error
where access.date = error.date

After creating these views you can run python3 Logs.py to generate the logs analysis