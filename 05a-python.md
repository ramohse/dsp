# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>>*The most basic difference between lists and tuples is mutability--lists are mutable, and can be changed. You can add, remove, and alter items in a list at will. Tuples, however, are* **IM** *mutable, and cannot be altered. It is this immutability that allows tuples to work as dictionary keys, while lists cannot. This is due to how Python stores and looks up items in dictionaries using "hash functions." Hash functions take values and assign to them integers; when a dictionary is created, Python takes the keys and assigns them hash integers to facilitate the lookup algorithm used in quickly finding key-value pairs.*

>>*This is only effective if the keys cannot change. Say, for instance, you were to create a dictionary using a list as keys for values. Python would look at the list, look at the associated values, and assign a hash value to each key-value element of the dictionary. If you were to change an item in the list used as keys, when Python looked at the dictionary again, it would rehash the altered list element. This would create confusion, as what is ostensibly the same key-value pair would have two distinct hash values. As such, when you went to look it up you would either get two entries for the same key or a search error.*  

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>>*Lists and sets are similar in that they both contain only values (whereas a dictionary contains keys and corresponsing values), and can have items added to or removed from them. However, sets are distinct from lists due to a few key qualities:*  

>>*-Sets cannot contain duplicate values*  
>>*-Sets are unordered (thus no slicing or indexing can be done on a set)*  
>>*-Sets are made up of hashable (i.e. immutable) items*  

>>*Because sets contain hashable items, operations that involve finding an item within a set are much, much faster than those done over a list, as an operation over a list iterates over each item, whereas the set operation utilizes the hash and hash table to quickly find it. These qualities also allow mathematical set operations such as "union", "intersection", and "difference" to be executed over a Python set.*  

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>>*Lambda is a anonymous function that can be created and executed during runtime, without a "def" statement. That is, rather than doing this:*
```python
>>> def add_two(n):
>>>    n += 2
>>>    return n
>>> b = add_two(10)
>>> print(b)
     12
```
>>*One could do this:*
```python
>>> c = lambda x: x+2
>>> print c(10)
     12
```
>>*Rather than defining a whole function to add two to a number, I was able to use lambda to quickly and easily create a function that increments a number by two and print it out.*  

>>*A common use of lambda is in the `sorted()` function, which returns a sorted list. There is a `key` parameter within `sorted()` that allows you to alter each item so it will be sorted differently. When sorting lists, Python puts upper-case letters before lower-case letters, regardless of alphabetic order (so "P" would come before "a", as an example). As such, you might want to make each item lower-case so the whole list sorts alphabetically. One way to do this would be by definining a lower-case function separately, and executing it over the `key` values:*
```python
>>> def lower_case(word):
>>>     return word.lower()
>>>
>>> mylist = ['My', 'name', 'is', 'Marcus']
>>> sorted(mylist, key = lower_case)
    ['is', 'marcus', 'my', 'name']
```
>>*Alternatively, one could define a lower-case function on the fly with lambda within the `sorted()` function itself for more concise code:*
```python
>>> mylist = ['My', 'name', 'is', 'Marcus']
>>> sorted(mylist, key = lambda word: word.lower())
    ['is', 'marcus', 'my', 'name']
```  

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> *List comprehension is a way to create lists based on defined conditions, and transform those conditional list items using conditionals, and Boolean and logical operators. The syntax for list comprehension is comprised of four parts:*  
>>*-Input list--this is the source list, from which you want to create a new list based on some conditions. Could be an existing list, or a `range()` output of numbers*  
>>-*Variable--represents the individual items in the source list*  
>>*-Output expression--the transformation being made to the items in the source list*  
>>*-Optional predicate--a conditional filter on the items in the source list to further refine elements of the new list (like all even numbers, only multiples of 3, etc.)*  

>>*Say, for instance, you had a list of the numbers from 1 to 10, and wanted to create a new list of only the even numbers from that list, multiplied by 2. Using list comprehension, you could do this:*  
```python
>>> old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> new_list = [n * 2 for n in old_list if n % 2 == 0]
```
>>*Where there are four parts are:*  
>>*-Input list--*`old_list`  
>>*-Variable--*`for n in`  
>>*-Output expression--*`n * 2`  
>>*-Optional predicate--*`if n % 2 == 0`  

>>*However, Python has two functions, `map()` and `filter()`, that can accomplish something similar. `map()` applies a function to every item in a list and returns the result; `filter()` returns a new list from an input list based on the items for which a given function returns `True`. Basically, you can filter a list for the items you want and then transform (map) only those items and send them to a new list. Using our list comprehension example from above, the `map() filter()` method would look like this:*
```python
>>> old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> new_list = list(map(lambda n: n * 2, filter(lambda n: n % 2 == 0, old_list)))
```
>>*While the two methods yield similar functional results, the pros and cons of each method are the topic of some heated debate on the internet. List comprehensions can be clearer to a person reading code (especially if the `map() filter()` uses user-defined functions defined elsewhere in code), and list comprehension can execute faster than `map() filter()` in many cases, as `map() filter()` calls a function on each element (vs list comprehension, which loops over the items and only executes code on items that return `True`). However, if the functions applied to the list items are too complex to effectively and concisely write in list comprehension and/or are already defined, an argument can be made for `map() filter()`.*

>>*Comprehensions can also be written for dictionaries and sets, thought the syntax is a little bit different. For dictionaries, the comprehension statement is written in curly brackets `{}` instead of the square brackets `[]` used for lists, and requires two expressions for each item separated by a colon (for key and value). Say, for instance, you have a dictionary with frequencies of letters appearing in a sentence, both upper case and lower case, but would just like to see the frequency of letters regardless of case; your list comprehension might look like this:* 
```python
>>> old_dict = {'g': 2, 'r': 4, 'T': 1, 'i': 4, 'e': 3, 'h': 2, 'l': 1, 'a': 4, 'o': 3, 'n': 3, 's': 3, 'W': 1, '.': 2, 't': 3, 'k': 2, 'C': 1, 'w': 2, ' ': 9, ',': 1, 'm': 1, 'u': 1, 'S': 1, 'y': 2}
>>> new_dict  = {k.lower(): old_dict.get(k.lower(), 0) + old_dict.get(k.upper(), 0) for k in old_dict.keys()}
    new_dict = {'s': 4, 'g': 2, 't': 4, 'k': 2, 'r': 4, 'i': 4, 'e': 3, '.': 4, 'w': 3, 'u': 1, 'y': 2, ' ': 18, ',': 2, 'h': 2, 'm': 1, 'c': 1, 'l': 1, 'a': 4, 'o': 3, 'n': 3}
```
>>*Where the four components of comprehenstion are:*  
>>*-Input list--*`old_dict`  
>>*-Variable--*`for k in`  
>>*-Output expression--*`k.lower(): old_dict.get(k.lower(), 0) + old_dict.get(k.upper(), 0)`  

>>*Set comprehensions are a hybrid of lists and dicitonaries--they are structurally similar to list comprehensions, but are written in curly brackets instead of squares. An example of a set comprehension creating a set of all prime numbers between 1 and 100 could be written as such:*  
```python
>>> primes = {n for n in range(2, 101) if all(n % x for n in range(2, min(n, 11)))}
```
>>*Where the four components are:*  
>>*-Input list--*`range(2, 101)`  
>>*-Variable--*`for n in`  
>>*-Output expression--*`n`  
>>*-Optional predicate (determines the primes)--*`if all(n % x for n in range(2, min(n, 11)))`  

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>>*937 days*  

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> *513 days*  

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> *7,850 days*  

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





