"""
Isomorphic Strings (Leet Code)

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurences of a character must be replacd with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: True

Example 2:
Input: s = "foo", t = "bar"
Output: False

Example 3:
Input: s = "paper", t = "title"
Output: True

Note:
You may assume both s and t have the same length.

"""

def isomorphicStrings(s, t):
    
    arr_1 = []
    arr_2 = []
    dict_1 = {}
    dict_2 = {}

    counter = 1
    
    for i in range(len(s)):
        if (s[i] == t[i]):
            arr_1.append(0)
            continue
        if (s[i] in dict_1):
            arr_1.append(dict_1[s[i]])
        else:
            arr_1.append(counter)
            dict_1[s[i]] = counter
            counter += 1

    counter = 1

    for i in range(len(t)):
        if (s[i] == t[i]):
            arr_2.append(0)
            continue
        if (t[i] in dict_2):
            arr_2.append(dict_2[t[i]])
        else:
            arr_2.append(counter)
            dict_2[t[i]] = counter
            counter += 1
    
    for i in range(len(arr_1)):
        if (arr_1[i] != arr_2[i]):
            return False
    return True


