"""
An anagram of a string is an another string that contains same characters, only the order of characters can be
different.
Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.

Strings in Python are immutable which means that once a string variable is
assigned to a string (For example, a ='Hello') the contents of the string
cannot be changed unlike the list object.

The method lower() returns a copy of the string in which all case-based
characters have been lowercase.

The primary difference between the list sort() function and the sorted() function is that the sort() function will
modify the list it is called on. The sorted() function will create a new list containing a sorted version of the
list it is given. The sort() function modifies the list in-place and has no return value.
"""

import string

string1 = input()
string2 = input()

s = string.ascii_lowercase + "0123456789"

string1 = string1.lower()
string2 = string2.lower()

string1 = sorted(string1)
string2 = sorted(string2)

string1 = "".join(string1)
string2 = "".join(string2)

for i in string1:
    if i not in s:
        string1 = string1.replace(i, "")

for i in string2:
    if i not in s:
        string2 = string2.replace(i, "")

if string1 == string2:
    print("Yes", end="")
else:
    print("No", end="")
