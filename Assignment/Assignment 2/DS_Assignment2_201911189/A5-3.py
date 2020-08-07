#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A5-3 (2 points)
def root():
    for node in T:
        if f(node) == 0:
            return node
        
def is_root(p):
    return f(p) == 0

def parent(p):
    if f(p) % 2 == 0:
        for node in T:
            return T[(f(p))/2-1]
    elif f(p) % 2 == 1:
        for node in T:
            return T[(f(p)-1)/2]
        
def left(p):
    for node in T:
        if node == parent(T[2*f(p)+1]):
            return node
        else:
            return None

def right(p):
    for node in T:
        if node == parent(T[2*f(p)+2]):
            return node
        else:
            return None

def is_leaf(p):
    if left(p) != None or right(p) != None:
        False
    else:
        True

