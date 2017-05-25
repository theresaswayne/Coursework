#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 23:13:32 2017

@author: theresa
"""
from itertools import chain, combinations

def generate_iterables():
    for i in range(10):
        yield range(i)

itertools.chain.from_iterable(generate_iterables())
#TODO: find code to illustrate how this works
