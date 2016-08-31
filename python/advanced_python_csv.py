# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 22:05:16 2016

@author: ramohse

Reads the emails from the faculty.csv file and writes them in a column
to the emails.csv file

fac_file - faculty.csv file
fac_reader - faculty.csv reader object
email_list - a list of emails from faculty.csv
email_file - email.csv file
email_writer - email.csv writer object

"""

import csv

with open('faculty.csv') as fac_file:
    fac_reader = csv.reader(fac_file)
    email_list = []
    next(fac_reader, None)
    for row in fac_reader:
        email_list.append(row[3])

fac_file.close()


with open('emails.csv', 'w') as email_file:
    email_writer = csv.writer(email_file, delimiter='\n')
    email_writer.writerow(email_list)

email_file.close()
