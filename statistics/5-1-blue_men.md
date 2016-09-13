[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>>*Roughly 34% of the population would qualify for the Blue Man Group, as calculated by the difference betwee the cumulative distribution of the upper bound height requirement (185 cm) and the lower bound height requirement (178 cm).*  
>>*The z-scores of the range are within one standard deviation (mostly) above the mean, which helps verify the finding--as 68% of a sample with a normal distrubution falls within +/-1 standard deviation of the mean, and we are looking at the +1 standard deviation, or half of that 68% value.*  

```python
"""
Calculates the proportion of the population who would qualify for the Blue Man Group based on height.
Uses modules from the Think Stats 2 github repository:
https://github.com/AllenDowney/ThinkStats2
"""

import thinkstats2
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)

"""
There are 2.54 inches in a cm
Lower bound of 5'10" is 70 inches, or 177.8 cm
Upper bound of 6'1" is 73 inches, or 185.42
"""

lower_b = dist.cdf(177.8)
upper_b = dist.cdf(185.42)
z_lower = ((177.8 - mu) / sigma)
z_upper = ((185.42 - mu) / sigma)
print('Percentage of population tall enough for Blue Main group:', '{0:.2f}'.format((upper_b - lower_b)))
print('z-score, lower bound:', '{0:.2f}'.format(z_lower))
print('z-score, upper bound:', '{0:.2f}'.format(z_upper))
```
