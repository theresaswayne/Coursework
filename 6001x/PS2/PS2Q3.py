# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 10:44:44 2016

@author: confocal
"""

def BalanceAfterMonths(bal, interest, pmt, months):
    '''
    bal: float, balance at the beginning of the period
    interest: float, annual interest rate in decimal form
    pmt: float, fixed monthly payment
    months: integer, number of months elapsed
    
    Returns the unpaid balance after the specified number of months if only the minimum payment is made.
    '''
    if months == 1:
        return (1 + interest/12)*(bal - pmt)
    else:
        return (1 + interest/12)*(BalanceAfterMonths(bal, interest, pmt, months - 1) - pmt)

#test
#balance = 999999
#annualInterestRate =  0.18
epsilon = 0.12
#pmt = 0.04

lowPmt = balance/12
highPmt = BalanceAfterMonths(balance, annualInterestRate, 0, 12)
pmt = lowPmt + (highPmt-lowPmt)/2
#print("lowest payment "+str(lowPmt)+", highest payment "+str(highPmt)+", guess = "+str(pmt))

while pmt < highPmt:
    finalBal = BalanceAfterMonths(balance, annualInterestRate, pmt, 12)
#    print("payment "+str(pmt)+", final balance = "+str(finalBal))
#    print("lowest payment "+str(lowPmt)+", highest payment "+str(highPmt)+", guess = "+str(pmt))
    if finalBal > 0:
        # guess is too low
        lowPmt = pmt # redefine low point
        pmt = lowPmt + (highPmt-lowPmt)/2
    elif finalBal < 0:
        # guess may be too high
        if abs(finalBal) < epsilon: # close enough
            break
        else: 
            highPmt = pmt
            pmt = lowPmt + (highPmt-lowPmt)/2
    else: # finalBal = 0
        break
#for i in range (1,13):
#    ans = BalanceAfterMonths(bal, interest, pmt, i)
#    roundAns = round(ans*100)/100
#    print("Month "+str(i)+" Remaining balance: "+str(roundAns))

#ans = BalanceAfterMonths(balance, annualInterestRate, monthlyPaymentRate, 12)
roundAns = round(pmt*100)/100

print("Lowest Payment: "+str(roundAns))