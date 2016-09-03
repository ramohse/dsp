# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 22:36:55 2016

@author: ramohse

Reads the faculty.csv file. parses the faculty data, and creates dictionaries
per the Advanced Python exercise request 
(https://github.com/ramohse/dsp/blob/master/05b-python_advanced.md)

deg_list - parsed list of degrees
title_list - parsed list of titles (Professor, Assistant Professor, etc)
email_list - parsed list of email addresses
name_list - list of faculty names
first_name_list - list of faculty first names
last_name_list - list of faculty last names
dict_vals - an intermediate list of lists containing faculty email, title, degrees
faculty_dict - dictionary of faculty members, last name key
professor_dict - dictionary of faculty members, first, last name key

Each exercise is beneath a heading denoted by '###', with the last exercise
live and the preceeding two hashed out.

"""

import csv, re, itertools

with open('faculty.csv') as fac_file:
    fac_reader = csv.reader(fac_file)
    name_list = []    
    deg_list = []
    title_list = []
    email_list = []
    next(fac_reader, None)
    for row in fac_reader:
        name_list.append(row[0])
        deg_list.append(row[1])
        title_list.append(row[2])
        email_list.append(row[3])

fac_file.close()


### The below formats the lists for use
name_list = ';_'.join(name_list)
last_name_list = name_list + ';_'
last_name_list = re.findall('\w*?;_', last_name_list)
last_name_list = ' '.join(last_name_list)
last_name_list = re.split(';_\s?', last_name_list)


first_name_list = ';_' + name_list
first_name_list = re.findall(';_\w\.?\s?\w*?(?:(?!\s).)*', first_name_list)
first_name_list = ''.join(first_name_list)
first_name_list = re.split(';_', first_name_list)
del first_name_list[0]    #removes erroneous blank space item


for i in range(len(deg_list)-1):
    deg_list[i] = re.sub('Ph\.?D\.?','Ph.D.', deg_list[i])
    deg_list[i] = re.sub('Sc\.?D\.?','Sc.D.', deg_list[i])
    deg_list[i] = re.sub('^\s', '', deg_list[i])
    

title_list = ' '.join(title_list)
title_list = re.split('\s..\sBiostatistics\s?', title_list)
del title_list[len(title_list)-1]    #removes erroneous blank space list item



### 5b_03.06 - Dictionary with last name as key

#dict_vals = [list(a) for a in zip(deg_list, title_list, email_list)] 
#faculty_dict = dict(zip(last_name_list, dict_vals))

#print(faculty_dict)
#first_three = itertools.islice(faculty_dict.items(), 0, 3)
#for key, value in first_three:
#    print(key, ':', value)



### 5b_03.07 - Dictionary with first, last name as key

#dict_vals = [list(a) for a in zip(deg_list, title_list, email_list)] 
#name_list = list(zip(first_name_list,last_name_list))
#professor_dict = dict(zip(name_list, dict_vals))   

##print(professor_dict)
#first_three = itertools.islice(professor_dict.items(), 0, 3)
#for key, value in first_three:
#    print(key,':', value)



### 5b_03.08 - Dictionary printed by last name

dict_vals = [list(a) for a in zip(deg_list, title_list, email_list)] 
name_list = list(zip(first_name_list,last_name_list))
professor_dict = dict(zip(name_list, dict_vals))   

##print(professor_dict)
for key in sorted(professor_dict, key=lambda x: x[1]):
    print(key, ':', professor_dict[key])
