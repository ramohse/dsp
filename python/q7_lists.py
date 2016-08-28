# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.
    """        
    count = 0
    
    for w in words:
        if len(w) > 1 and w[0] == w[(len(w) -1)]:
            count += 1
        else:
            count = count
            
    return count



def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
    """
    x_list = []
    non_x_list =[]

    for w in words:
        if w[0] == 'x':
            x_list.append(w)
        else:
            non_x_list.append(w)
    
    x_list.sort()
    non_x_list.sort()
    
    return x_list + non_x_list



def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].
    """
    new_tup = sorted(tuples, key = lambda tup: tup[(len(tup) - 1)])
    
    return new_tup



def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.
    """
    i = 1
    
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
            i -= 1
        i += 1
    return nums    



def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.
    """
    new_list = []
    i = j = 0
    total_ct = len(list1) + len(list2)
   
    while len(new_list) != total_ct:
        if len(list1) == i:
            new_list += list2[j:]
            break
        elif len(list2) == j:
            new_list += list1[i:]
            break
        elif list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
    
    return new_list
