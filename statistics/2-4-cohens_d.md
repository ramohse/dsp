[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

# -*- coding: utf-8 -*-
"""
@author: ramohse

Data, classes, and functions imported from Think Stats 2 git repository:
https://github.com/AllenDowney/ThinkStats2

Calculates descriptive statistics for the first baby and other baby datasets

"""

import first
import thinkstats2
import thinkplot
from math import sqrt


firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

### Calculation of descriptive statistics of each group

tot_mean = live.totalwgt_lb.mean()
#tot_var = live.totalwgt_lb.var()
#tot_std = live.totalwgt_lb.std()
#tot_ct = len(live.totalwgt_lb)

firsts_mean = firsts.totalwgt_lb.mean()
firsts_var = firsts.totalwgt_lb.var()
firsts_std = firsts.totalwgt_lb.std()
firsts_ct = len(firsts)

others_mean = others.totalwgt_lb.mean()
others_var = others.totalwgt_lb.var()
others_std = others.totalwgt_lb.std()
others_ct = len(others)


### Calculation of Cohen's d

diff = firsts_mean - others_mean
percent_diff = diff / tot_mean
totalvar = ((firsts_ct * firsts_var) + (others_ct * others_var)) / (firsts_ct + others_ct)

cohens_d = diff / sqrt(totalvar)


### Prints the outcome

print("The difference in mean weight between first babies and subsequent babies is:")
print('{0:.2f} lbs'.format(diff))
print('or ', '{0:.2}%'.format(percent_diff * 100), ' of the mean weight of all births.')
print('\n')
print('The Cohen\'s d effect-size measure of first birth size vs. others is:')
print('{0:.2f} std devs'.format(cohens_d), ',')
print('larger in magnitude than the effect first births have on length of pregnancy (0.029 std devs), but still small.')
