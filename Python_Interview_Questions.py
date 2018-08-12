#1. From an Array find all combinations where the sum of two integers matches the target
import pyodbc
import numpy as np
import pandas as pd

A = [0,-2,1,-1,3,-3,4,7,-5]
target = 3
B=[]
for i in range(len(A)-1):
    for j in range(i+1,len(A)):
        if A[i] + A[j] == 3:
            B.append((A[i],A[j]))
print(B)

#2. Find Missing Numbers
import pyodbc
import numpy as np
import pandas as pd
B = []
A = [1, 2, 5, 7, 8, 11, 15]

def missingValues(arr):
    for i in range(len(A) - 1):
        if A[i] + 1 == A[i + 1]:
            pass
        else:
            x = A[i]

            while x + 1 != A[i + 1]:
                x = x + 1
                B.append(x)

    print(B)

# missingValues(A)

#3. Find Duplicate Nos in an array

import pyodbc
import numpy as np
import pandas as pd

myarr = [0,3,1,2,3]
def duplicateNos(A):
    my_dict={}
    for item in A:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1
    my_dict

    for key, value in my_dict.items():
        if value > 1:
            return key
        else:
            pass

# duplicateNos(myarr)

#4. Check if the two words are Anagrams
import pyodbc
import numpy as np
import pandas as pd

source ='listen'
target = 'silent'

def anagramCheck(source,target):
    if len(source) == len(target):
        words = list(source)
        for word in words:
            if word in target:
                pass
            else:
                return False
        return True
    else:
        return False
# print(anagramCheck(source,target))

# 5. Find first nonRepeating Character from a given string
mystring ='MorningMo'

def firstnonRepeatedChar(mystring):
    words = list(mystring)
    for word in range(len(words)):
        if words.count(words[word]) == 1:
            print(words[word])
            break
        else:
            pass

# firstnonRepeatedChar(mystring)

#6. From a Given string print out no of vowels and no of consonants
mystring ='hello'

def vowelsConsonantsCount(mystring):
    v = ['a','e','i','o','u']
    l = len(mystring)
    s = list(mystring)
    x = 0
    y = 0
    if len(mystring) > len(v):
        for vowels in v:
            if vowels in s:
                x = x + 1
            else:
                y = y + 1
    else:
        for chars in s:
            if chars in v:
                x = x + 1
            else:
                y = y + 1
    return print(str(x) + ' Vowels and ' + str(y) + ' Consonants')

# vowelsConsonantsCount(mystring)

#7. Find all permutations of a given string
word ='xyz'
def permutations(word):
    if len(word) <= 1:
        return [word]

    #get all permutations of length N-1
    perms = permutations(word[1:])
    char = word[0]
    result = []
    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result

# permutations(word)

#8.Remove Duplicate Chars from a String
mystring ='bananas'
#output = bans
def removeDuplicateChars(mystring):
    x =''
    if len(mystring) == 0:
        return print('Empty String')

    if len(mystring) ==  1:
        return mystring

    for chars in range(len(mystring)):
        if mystring[chars] in x:
            pass
        else:
            x = x + mystring[chars]
    return x

# removeDuplicateChars(mystring)

#9. Check if a given string is a valid shuffle of two strings
#eg String1 : 'abc' , string2 : 'def'  string3:'dabef'
string1 = 'abc'
string2 = 'def'
string3 = 'dabef'

def validStringShuffleCheck(string1, string2, string3):
    x = ''
    y = ''
    for i in range(len(string3)):
        if string3[i] in string1:
            x = x +  string3[i]
        else:
            y = y + string3[i]
    if x in string1 and y in string2:
        return True
    else:
        return False
# validstringShuffleCheck(string1, string2, string3)

#10. Number String. Given a number add commas at thousands location
#eg number = 1234 output: 1,234
# number  = 1234567 Output: 1,234,567
def numberString(numbr,a):
    g =''

    if int(numbr/1000) == 0:
        return print('number less than 1000')

    if len(a) == 0:

        x = int(numbr / 1000)
        y = numbr % 1000

        z = str(x) + ',' + str(y)
        a.append(y)

        if len(str(x)) < 4:
            return str(x)+','+str(y)
        else:
            numberString(x,a)
    else:
        x = int(numbr/1000)
        y = numbr%1000
        z = str(x)+','+str(y)

        a.append(y)

        if len(str(x)) >= 4:
            numberString(x,a)
        else:
            for i in a[::-1]:
                g = g +','+ str(i)


        return print(str(x)+g)


# print(numberString(123,[]))

#11. Given an array the output should be the following
arr = [1,2,3,4]
# output = [24,12,8,6]

def productArray(arr):
    a = []
    x = 1
    for i in arr:
        x = x * i

    for j in arr:
        a.append(int(x/j))

    return a

# productArray(arr)

#12. Given a number return it as as array
# eg: 123 output: [1,2,3]
def numberString(a):
    x = a
    arr = []

    while x > 0:
        rem = x % 10
        arr.append(rem)
        quo = int(x / 10)
        x = quo
    arr.sort()
    return arr


# numberString(123)

#13. Find Avg length of string
def avgStringLength(a):

    if len(a) == 0:
        return None
    else:
        arr = a.strip().split(' ')
    l = 0
    for i in arr:
        l =  l + len(i)
    return l/len(arr)


a = ' Hello How Are you today '
# avgStringLength(a)

#14 Valid Ip Check
def validateIP(ip):
    if len(ip) < 7:
        return 'invalid ip'

    arr = list(ip.strip().split('.'))

    if len(arr) < 4 or len(arr) > 4:
        return 'invalid ip'

    else:
        for i in arr:
            if i.isnumeric() is True:

                if int(i) not in range(1,256):
                    return 'invalid ip'
                else:
                    pass
            else:
                return 'Invalid Ip'
        return 'Valid Ip'


# print(validateIP('1.2.3.255'))


#15. Given a list of lists return a dictionary
#eg: [['A,B'],['B,C'],['C,D'],['D,A'],['D,E'],['E']] Output: {'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 0}

a = [['A,B'],['B,C'],['C,D'],['D,A'],['D,E'],['E,F'],['E']]

def neighbours(a):

    d = {}
    for i in range(len(a)):
        if len(list(a[i][0].split(','))) == 1 :
            if a[i][0] in d.keys():
                pass
            else:
                d[a[i][0]] = 0
        else:
            nums = list(a[i][0].split(','))
            for j in nums:
                if j in d.keys():
                    d[j] =  d.get(j) + 1
                else:
                    d[j] = 1
    return d

# neighbours(a)

# 16. Longest Substring Without Repeating Characters
def lengthOfLongestSubstrings(s):
    if len(s) < 2:
        return 1
    elif len(s) == 0:
        return 0
    else:
        string = s[0]
        a = 1
        longestsubstring = 0

        for i in range(1, len(s)):

            if s[i] in string:
                print('++++++++++++++++++++++')
                print('a:' + str(a), 'String:' + string, 'longestSubstring:' + str(longestsubstring))
                if len(s) == 2:
                    return 1
                else:
                    longestsubstring = a

                    string = ''
                    a = 0
                    print('----------------------------')
                    print('a:' + str(a), 'String:' + string, 'longestSubstring:' + str(longestsubstring))

            else:
                print('============================')
                a = a + 1
                if longestsubstring >= a:
                    pass
                else:
                    longestsubstring = a
                # longestsubstring = a
                string = string + s[i]
                # print('a:' + str(a), 'String:' + string, 'longestSubstring:' + str(longestsubstring))
        return longestsubstring

# 17.
def lengthOfLongestSubstring(s):

    if len(s) == 0:
        return 0
    elif len(s) < 2:
        return 1
    else:
        a = 0
        longestsubstring = 0
#dvdf
        for i in range(len(s)):
            string = s[i]
            for j in range(i+1,len(s)):

                if s[j] in string:
                    longestsubstring = a
                    a = 0
                    pass
                else:
                    string = string + s[j]
                    a = a + 1


# 18] Given an n x n 2D array. Rotate the Array by 90 degrees (clockwise)
"""
Eg. 
arr = a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

output:
 [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
"""
def rotateArray(a):
    list_of_tuples = zip(*a[::-1])
    return [list(elem) for elem in list_of_tuples]


if __name__ == '__main__':
    print(lengthOfLongestSubstring('dvdf'))
