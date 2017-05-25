# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 10:44:06 2016

@author: confocal
"""

def BalanceAfterMonths(bal, interest, pmt, months):
    '''
    bal: float, balance at the beginning of the period
    interest: float, annual interest rate in decimal form
    pmt: float, minimum monthly payment as a decimal fraction of the balance
    months: integer, number of months elapsed
    
    Returns the unpaid balance after the specified number of months if only the minimum payment is made.
    '''
    if months == 1:
        return (1 + interest/12)*(bal * (1-pmt))
    else:
        return (1 + interest/12)*(BalanceAfterMonths(bal, interest, pmt, months - 1)*(1-pmt))
        
# test
#bal = 484
#interest = 0.2
#pmt = 0.04

#for i in range (1,13):
#    ans = BalanceAfterMonths(bal, interest, pmt, i)
#    roundAns = round(ans*100)/100
#    print("Month "+str(i)+" Remaining balance: "+str(roundAns))

ans = BalanceAfterMonths(balance, annualInterestRate, monthlyPaymentRate, 12)
roundAns = round(ans*100)/100

print("Remaining balance: "+str(roundAns))