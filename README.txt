--Original Date: 2018-06-01
--Updated Date: 2018-06-04
--Project: Udacity FSND Logs Analysis Project
--Python Version 3.6
--Vagrant 2.1.1

tldr; Run Python app: While in vagrant dir, i run command [ python NewsReportingTool.py > output.txt] to kick off my python file which will output to a flat file

--Several files in folder but for this project this is the description
Files:
1. README.txt = instructions file explaining project
2. FileOutput.png - screenshot of vagrant output of answers to questions
3. NewsReportingTool.py = python file to run sql queries and output answers to questions
4. SQL Reporting queries:
    a. topViewArticles.sql = query that returns the top 3 viewed articles 
    b. topAuthors.sql = query that returns top authors by views for all time
    c. errorsDaily.sql = query that returns total views, total success, total errors then calculates error rate

Program run:
1. I 'cd' into my working directory using GIT Bash
2. Run command vagrant up
3. Run command vagrant ssh
4. Now that I am in vagrant I cd into vagrant/newsdata/FSND_LogsProject folder
5. If I want to explore my News database I run psql News
    a. I can \d or \dt to explore tables in database and see columns
    b. \q to exit
6. Run Python app: While in vagrant dir, i run python NewsReportingTool.py to kick off my python file which will output in the terminal display the results of the query
    or run [ python NewsReportingTool.py > output.txt] to output to a file.
