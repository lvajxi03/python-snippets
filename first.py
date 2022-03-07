#!/usr/bin/env python

def func(*arguments):
    print("Hello!")
    for argument in arguments:
        print("Got argument", argument)
    print(" -- the end --")

func(1, 2, 3)
func('a', 'b', 'c')
func(1, 2, 'a', 'b')
func(1, 2, 'a', 'b', [1, 2, 3, 4, 5])



