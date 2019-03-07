import math
import os
import random
import re
import sys

def reverso(a):
	b=[]
	for i in range(len(a),0,-1):
		b.append(a[i-1])

	return b

def hourglassSum(arr):
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            if (arr[i][j] and arr[i+1][j] and arr[i+2][j] and arr[i+1][j+1] and arr[i][j+2] and arr[i+1][j+2] and arr[i+2][j+2]):
                print(arr[i][j],arr[i+1][j],arr[i+2][j], '\n', 'etc')

def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost*(float(tip_percent)/100)
    tax = meal_cost*(float(tax_percent)/100)

    print(int(meal_cost + tip + tax))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)


#print(reverso(a))
#hourglassSum(a)
