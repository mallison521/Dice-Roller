#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:56:16 2019

@author: mallison
"""


import random
print(random.randint(1,6))
ans = input(f"Would you like to reroll the dice?").lower();
while True:
    if ans == 'yes':
        for i in range(1):
            print(random.randint(1,6))
            ans = input(f"Would you like to reroll the dice?").lower();
    elif ans == 'no':
        break
print('Have a nice day!')