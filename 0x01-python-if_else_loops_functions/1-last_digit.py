#!/usr/bin/python3
import random
number = random.randint(-100000, 100000)
digit = abs(number) % 10
if figures < 0:
	digit = -digit
print(f"Last digit of {number:d} is {digit}")
if digit > 5:
	print("greater than 5")
elif digit == 0:
	print("0")
else:
	print("less than 6 and not 0")