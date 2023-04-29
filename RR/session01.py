#!/usr/bin/env python

# Author: Vyvienne Bautista
# Session date: 29/04/23

def concatenate(strings):
    # eg. [ 'apple', 'banana', 'mango' ]
    # assume strings is a list
    together = ""

    for s in strings:
        together = together + s

    return together

def cube(tocube):
    cubednum = tocube**3
    return cubednum

def cubes(data):
    # eg. [ 1, 2, 3 ]
    # make them into cubed numbers
    data = list(map(cube, data))
    return data
