#!/usr/bin/env python

def numbers(start: int) -> int:
    a, b = 0, start
    while True:
        yield b
        a, b = b, b+a

print("first:")
gen = numbers(5)
for i in range(0, 9):
    print(next(gen))
print("second:")
gen = numbers(1)
for i in range(0, 9):
    print(next(gen))
