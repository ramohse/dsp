# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 19:02:52 2016

@author: ramohse
"""

# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
import math

def donuts(count):
    """
    Given an int count of a number of donuts, returns a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    """
    """ Converts donut count to an integer. If it is not a valid entry, an
    error message is raised. Otherwise checks the value of the variable and
    prints the appropriate output.
    """
    parsed = False
    while not parsed:
        try:
            count = int(count)
            parsed = True
        except ValueError:
            print('Sorry, that\'s not a number. Try again')
            
    if count < 0:
        print('Number of donuts: %d (did you eat some?)' % count)
         
    elif count < 10:
        print('Number of donuts: %d' % count)
        
    else:
        print('Number of donuts: many')



def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
    """    
    l = len(s)
    new_s = ''   
    
    if l < 2:
        return new_s
    else:
        new_s = s[0] + s[1] + s[l-2] + s[l-1]
        return new_s



def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.
    """    
    b = s[0]
    temp_s = s.replace(b,'*')
    return b + temp_s[1:]



def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.
    """
    a_start = a[:2]
    b_start = b[:2]
    
    a_new = b_start + a[2:]
    b_new = a_start + b[2:]

    return a_new + ' ' + b_new



def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.
    """
    l = len(s)    
    if l < 3:
        return s
    elif s[(l-3):] == 'ing':
        return s + 'ly'
    else:
        return s + 'ing'



def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'
    """    
    not_index = s.find('not')
    bad_index = s.find('bad')
    
    if not_index < bad_index:
        return s[:not_index] + 'good' + s[(bad_index + 3):]
    else:
        return s



def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back
    """   
    
    a_split = math.ceil(len(a) / 2)
    b_split = math.ceil(len(b) / 2)
    
    return a[:a_split] + b[:b_split] + a[a_split:] + b[b_split:]
