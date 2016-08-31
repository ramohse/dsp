# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 21:04:16 2016

@author: ramohse

Parses the faculty.csv file and calculates frequency of desired data points
Each block of code transforms the list into a string, performs regex parsing
on the data, coverts it back to a list, then calculates the frequency via the
histogram function.

histogram() - function to create a dictionary for which the key is the
              data point, and the value is the frequency in the data set
print_hist() - function to print the key-value pairs of a dictionary

deg_list - parsed list of degrees
title_list - parsed list of titles (Professor, Assistant Professor, etc)
email_list - parsed list of email addresses
domain_list - parsed list of email domains

"""

import csv, re


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d
    
def print_hist(z):
    for i in z:
        print(i, z[i])


with open('faculty.csv') as fac_file:
    fac_reader = csv.reader(fac_file)  
    deg_list = []
    title_list = []
    email_list = []
    next(fac_reader, None)
    for row in fac_reader:
        deg_list.append(row[1])
        title_list.append(row[2])
        email_list.append(row[3])

fac_file.close()


# 5b_01.01 - How many degrees?

deg_list = ' '.join(deg_list)
deg_list = re.sub('\s+',' ', deg_list)
deg_list = re.sub('\.','', deg_list)
deg_list = re.split('\s', deg_list)
del deg_list[0]    #removes erroneous blank space list item

h_deg = histogram(deg_list)
print('\nDegrees:')
print_hist(h_deg)


# 5b_01.02 - How many titles?

title_list = ' '.join(title_list)
title_list = re.split('\s..\sBiostatistics\s?', title_list)
del title_list[len(title_list)-1]    #removes erroneous blank space list item

h_title = histogram(title_list)
print('\nTitles:')
print_hist(h_title)


# 5b_01.02 - How many email domains?

email_list = ' '.join(email_list)
domain_list = re.findall('@.*?.edu',email_list)

h_domain = histogram(domain_list)
print('\nEmail domains:')
print_hist(h_domain)    
