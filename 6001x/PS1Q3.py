# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:52:28 2016

@author: confocal
"""

#s = "azcbobobegghakl"
#s = 'twdvjnos'
#s = 'wbgugexukgbqpbxdpalddll'
#s = 'abcdefghijklmnopqrstuvwxyz'
#s = 'zyxwvutsrqponmlkjihgfedcba'
#s = 'pmpfxogohvifcvvdwogklsz'
tempString = s[0]
longestString = ""


i=0
j=0

while i <= len(s): # loop through starting points
    if i == len(s)-1:
        if len(tempString) > len(longestString): # see if we got a longer string
            longestString = tempString
#        print("Reached end of string in i loop")
        break
#    print("checking "+s[i]+" and "+s[i+1])
    if s[i] <= s[i+1]: # these 2 chars are in alpha order
        tempString = s[i:i+2] # they become the seed of the alpha string
#        print("i = "+str(i)+", tempString = "+tempString)
        j = i + 1        
        while j <= len(s): # loop through indices 
#            print("j = "+str(j))
            if j == len(s)-1:
                if len(tempString) > len(longestString): # see if we got a longer string
                    longestString = tempString
#                print("Reached end of string in j loop")
                break
#            print("checking "+s[j]+" and "+s[j+1])
            if s[j] <= s[j+1]:
                tempString = s[i:j+2] # don't break, continue through j
#                print("j = "+str(j)+", tempString = "+tempString)
            elif len(tempString) > len(longestString): # see if we got a longer string
                longestString = tempString
#                print("longestString = "+longestString)
                break # out of the j loop
            else:
                break # out of the j loop if we didn't get a longer string
            if j == len(s)-1:
                break
            else:
                j += 1
    i += 1
print("Longest substring in alphabetical order is: " + longestString)