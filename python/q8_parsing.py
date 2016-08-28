# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

""" Imports the 'football.csv' file to parse and calculate the difference
between goals for and against each team. The program will print the team with
the smallest difference. The file assumes the 'football.csv' file is
in the current working directory.

team_list - a dictionary of teams and their difference between goals for and goals against
min_team - the key for the dictionary entry with the smallest value

"""

import csv

team_list = {}

f = open('football.csv')
csv_f = csv.reader(f)

for row in csv_f:
    if csv_f.line_num == 1:
        continue
    else:
        diff = abs(int(row[5]) - int(row[6]))
        team_list[row[0]] = diff

min_team = min(team_list, key = team_list.get)

print(min_team)
