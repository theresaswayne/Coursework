# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:56:58 2016

@author: theresa
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''    
    
    tens = '' # str to match the dictionary keys
    ones = ''    
    answer = ''
    
    num = int(us_num)
    if num > 10: # break it into digits
        tens = num // 10
        ones = num % 10

        # special cases = multiples of 10 and 11-19

        if ones == 0:
            answer = trans[str(tens)] + " shi"
        elif num < 20:
            answer = "shi " + trans[str(ones)]
        else:
            answer = trans[str(tens)] + " shi " + trans[str(ones)]

    else:     #  use the single digit word
        ones = trans[str(num)] # note this includes 10 itself
        answer = ones      

    return answer

# testing
#
#print("expected result: san shi liu, actual result: ", convert_to_mandarin('36'))
#print("expected result: er shi, actual result: ", convert_to_mandarin('20'))
#print("expected result: shi liu, actual result: ", convert_to_mandarin('16'))
#    
print("expected result: jiu shi jiu, actual result: ", convert_to_mandarin('99'))