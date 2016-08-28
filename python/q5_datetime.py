# Hint:  use Google to find python function
"""Calculates the number of days between two dates as strings bu converting them to dates with datetime's strptime() function
Day, month, and year format codes:
%m - zero-padded numerical month (i.e. 01, 02, 03)
%d - zero-padded day date
%Y - full year number
%b - month as abbreviated name (Jan, Feb, Mar)
"""

import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015' 

date_start = datetime.datetime.strptime(date_start,'%m-%d-%Y') 
date_stop = datetime.datetime.strptime(date_stop,'%m-%d-%Y')
n = date_stop - date_start
n = n.days
print('%d days' % n) 

####b)  
date_start = '12312013' 
date_stop = '05282015'

date_start = datetime.datetime.strptime(date_start,'%m%d%Y') 
date_stop = datetime.datetime.strptime(date_stop,'%m%d%Y')
n = date_stop - date_start
n = n.days
print('%d days' % n) 

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015' 

date_start = datetime.datetime.strptime(date_start,'%d-%b-%Y') 
date_stop = datetime.datetime.strptime(date_stop,'%d-%b-%Y')
n = date_stop - date_start
n = n.days
print('%d days' % n) 
