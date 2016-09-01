import csv, re, collections, itertools

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


# 5b_03.06 - Dictionary with last name as key

name_list = ';_'.join(name_list)
name_list = re.findall('\w*?;_', name_list)
name_list = ' '.join(name_list)
name_list = re.split(';_\s?', name_list)
del name_list[len(name_list)-1]    #removes erroneous blank space list item


deg_list = ' '.join(deg_list)
deg_list = re.sub('\s+',' ', deg_list)
deg_list = re.sub('\.','', deg_list)
deg_list = re.split('\s', deg_list)
del deg_list[0]    #removes erroneous blank space list item


title_list = ' '.join(title_list)
title_list = re.split('\s..\sBiostatistics\s?', title_list)
del title_list[len(title_list)-1]    #removes erroneous blank space list item


dict_vals = list(zip(deg_list, title_list, email_list))
dict_vals = list(zip(name_list, dict_vals))   

faculty_dict = collections.defaultdict(list)

for k, v in dict_vals:
    faculty_dict[k].append(v)
    
faculty_dict = collections.OrderedDict(faculty_dict)
first_three = itertools.islice(faculty_dict.items(), 0, 3)

for key, value in first_three:
    print(key, value)
