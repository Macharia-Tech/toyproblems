from django.shortcuts import render

# Create your views here.

# The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age, oldest age].

# The order of the numbers passed in could be any order. The array will always include at least 2 items.

# For example:

# two_oldest_ages([1, 3, 10, 0]) # should return [3, 10]

def two_oldest_ages(ages):
    array=[]
    for i in range(2) :
        mass.append(max(ages))
        ages.remove(max(ages))
    return sorted(mass)
    
    #your code here