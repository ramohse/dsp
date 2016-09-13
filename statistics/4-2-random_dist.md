[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>>*The numbers are random, as they fall within a uniform distribution as indicated by the cumulative density function.Additionally, the probability density function seems to indicate more or less equal probability among values.*  

```python
""" Tests the random.random() function by looking at a probability density function and cumulative density function based on 1,000 random samples generated from the function.

Uses modules from the Think Stats 2 github repository:
https://github.com/AllenDowney/ThinkStats2

"""

import random
import nsfg
import thinkstats2
import thinkplot

vals = [random.random() for _ in range(1000)]

cdf = thinkstats2.Cdf(vals)
thinkplot.Cdf(cdf)
thinkplot.Show(legend=False)
```  

[cdf](https://drive.google.com/open?id=0BxDOrykhLakVZGtCQ01yU2YyQWc "cdf for randomly-generated sample")  

```python
pmf = thinkstats2.Pmf(vals)
thinkplot.Pmf(pmf, linewidth = 0.05)
thinkplot.Show(axis=[0, 1, 0, .0011])
```  
[pmf](https://drive.google.com/open?id=0BxDOrykhLakVVi1jQ2dxWEVnaGc "pmf for randomly-generated sample")  
