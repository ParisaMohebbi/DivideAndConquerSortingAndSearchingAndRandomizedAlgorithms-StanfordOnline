#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 11:44:10 2023

@author: parisa
"""

import math

def karatsubaMultiply(x,y):
	# Defining base case for recursive calls
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x * y
	else:
		n = max(len(str(x)),len(str(y)))
		n_by_2 = n // 2

		# Step1: Rewriting x and y in terms of a,b,c,d
		a = x // 10**(n_by_2)
		b = x % 10**(n_by_2)
		c = y // 10**(n_by_2)
		d = y % 10**(n_by_2)

		# Step2: Computing ac
		ac = karatsubaMultiply(a,c)

		# Step3: Computing bd
		bd = karatsubaMultiply(b,d)

		# Step4: Computing ad+bc
		ad_bc = karatsubaMultiply(a+b,c+d) - ac - bd

		# Step5: Calculating finalValue
		finalAns = ac * 10**(2*n_by_2) + ad_bc * 10**(n_by_2) + bd

		return finalAns

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
print(karatsubaMultiply(x,y))
# 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
