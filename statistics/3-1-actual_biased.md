[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>>*Exercise from Think Stats, 2nd Edition (thinkstats2.com)*  
>>*Allen Downey*  
>>*Read the female respondent file.*  

```python
%matplotlib inline
import chap01soln
resp = chap01soln.ReadFemResp()
```
>>*Make a PMF of numkdhh, the number of children under 18 in the respondent's household.*

```python
import thinkstats2
pmf_kids = thinkstats2.Pmf(resp.numkdhh)
```
>>*Display the PMF.*  

```python
import thinkplot
thinkplot.Pmf(pmf_kids, label='num_kids')
thinkplot.Show()

<matplotlib.figure.Figure at 0x115706e48>
```
![pmf](https://drive.google.com/open?id=0BxDOrykhLakVODdmWDhjSl9RYzQ "Ex 03-01")

>>*Define BiasPmf.*  

```python
def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.
​
    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.
​
    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.
​
     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)
​
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
```
>>*Make a the biased Pmf of children in the household, as observed if you surveyed the children instead of the respondents.*  

```python
biased_kids = BiasPmf(pmf_kids, label = 'biased')
```
>>*Display the actual Pmf and the biased Pmf on the same axes.*  

```python
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf_kids, biased_kids])
thinkplot.Show(xlabel='num kids',
                   axis=[0, 6, 0, 0.6])

<matplotlib.figure.Figure at 0x115710a90>
```
![biased_pmf](https://drive.google.com/open?id=0BxDOrykhLakVNDF1M2hYNDI5c3M "Ex 03-02")

>>*Compute the means of the two Pmfs.*  

```python
print('mean of pmf', pmf_kids.Mean())
print('mean of biased pmf', biased_kids.Mean())
```
>>*mean of pmf 1.02420515504*  
>>*mean of biased pmf 2.40367910066*  
