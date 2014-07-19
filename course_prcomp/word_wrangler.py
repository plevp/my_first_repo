"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    list2 = [];
    ind1 = -1;
    ind2 = 0;
    if list1 == []:
        return []
    while (True):
        if ind2 ==len(list1):
            break;
        ind1 = ind2;
        list2.append(list1[ind1]);
        if ind1 == len(list1)-1:
            break;
        lasti = list1[ind1]
        ind2 = ind1+1
        while ind2 < len(list1) and list1[ind2] == lasti:
            ind2 +=1
    return list2

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    list3 =[]
    ind1 =0;
    ind2 =0;
    while (True):
        if ind1 == len(list1):
            #list3.extend(list2[ind2:])
            break;
        elif ind2 == len(list2):
            #list3.extend(list1[ind1:])
            break;
        elif list1[ind1] == list2[ind2]:
            list3.append(list1[ind1])
            ind1 += 1
            ind2 += 1
        elif list1[ind1] < list2[ind2]:
            ind1 +=1
        else: #list1[ind1] > list2[ind2]:
            ind2 += 1
    return list3


# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in both list1 and list2.

    This function can be iterative.
    """   
    
    list3 =[]
    ind1 =0;
    ind2 =0;
    while (True):
        if ind1 == len(list1):
            list3.extend(list2[ind2:])
            break;
        elif ind2 == len(list2):
            list3.extend(list1[ind1:])
            break;
        elif list1[ind1] == list2[ind2]:
            list3.append(list1[ind1])
            list3.append(list1[ind1])
            ind1 += 1
            ind2 += 1
        elif list1[ind1] < list2[ind2]:
            list3.append(list1[ind1])
            ind1 +=1
        else: #list1[ind1] > list2[ind2]:
            list3.append(list2[ind2])
            ind2 += 1
           
    return list3
    return []
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    #print list1
    if len(list1) <2:
        return list1

    half_len = len(list1)/2
    #print half_len
    
    return merge(merge_sort(list1[0:half_len]), merge_sort(list1[half_len:]))

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return ['']
    list1 =  gen_all_strings(word[1:])
    first = word[0]
    list2 = []
    for item in list1:
        for ind in range(len(item)+1):
            list2.append(item[:ind] + first + item[ind:])
    return list1 + list2

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    list1 = []
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    for line in netfile.readlines():
        list1.append(line[0:-1]);
    
    print list1[:100]
    return list1

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

#Uncomment when you are ready to try the game
run()

#print remove_duplicates([])
#print remove_duplicates([1,1])
#print remove_duplicates([1,2,2,2,3])
#print remove_duplicates([1,2,2,4,5,5])
#print remove_duplicates([1,1,2,2,3,3,4,4,4,5,5,5,7,7,7,7,7])
#print remove_duplicates([1,1])


#print intersect([], [])
#print intersect([1,2], [2])
#print intersect([1], [1,2])
#print intersect([1,3,5, 7], [2,5,6,7])
#print intersect([1,1,2,3,3,4], [1,1,2,2,3,4,4,5])
#print intersect([1,1,2,3,3,4], [1,1,2,2,3,4,4,5,5,7,8,9,9])
#print intersect([1,1,2,3,3,4,6,7,8,9], [1,1,2,2,3,4,4,5])

#print merge([], [])
#print merge([1,2], [2])
#print merge([1], [1,2])
#print merge([1,3,5, 7], [2,5,6,7])
#print merge([1,1,2,3,3,4], [1,1,2,2,3,4,4,5])
#print merge([1,1,2,3,3,4], [1,1,2,2,3,4,4,5,5,7,8,9,9])
#print merge([1,1,2,3,3,4,6,7,8,9], [1,1,2,2,3,4,4,5])

#print merge_sort([])
#print merge_sort([1])
#print merge_sort([2,1])
#print merge_sort([1,2,3])
#print merge_sort([2,1,3])
#
#                                  
#print merge_sort([1,1,2,3,3,4,6,7,8,9])
#print "xxxx"
#
#print gen_all_strings("b")
#
#print gen_all_strings("ab")
#
#
#print gen_all_strings("aab")
#
#print len(gen_all_strings("aab"))


#http://www.codeskulptor.org/#user36_bS17ZJvqtJ_20.py

