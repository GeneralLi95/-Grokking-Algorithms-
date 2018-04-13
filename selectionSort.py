#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:yaoli 
@file: selectionSort.py 
@time: 2018/04/13 
"""

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))    #非常巧妙的一步，两个list,一个pop掉，一个append进去
    return newArr


array = [5, 3, 6, 2, 10]
print (selectionSort(array))

