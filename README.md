# Introduction

This code will parse   UNIX /etc/passwd and /etc/groups files and combine the data into a single json output.

## Tech Stack
This code is written in Python and it has been tested with both python 2.x and python 3.x versions.
Pytest is used for unit testing


## How it works
Every  time we run the code, a under  LOGS/OUTPUT folder, a the requored json file is created with timestamp. At the same time a logging file logging.log is created
for tracking.


## How to run this code

Make file is created and the code can be run by below commands
```bash
make build  ( to run the code)
make test ( to run the tests)


./run.sh ( to run the shell script)


## Cron setting
Cron job is set up to run this code every night at 12 AM
Refer: https://www.adminschoice.com/crontab-quick-reference






