import sys
x = 0
n = sys.argv
for i in n:
	x += 1
if(x == 1):
	exit()
if(x > 2):
	print("AssertionError: more than one argument is provided")
	exit()
try:
	x = int(n[1])
except ValueError:
	print("AssertionError: argument is not an integer")
	exit()
if x < 0:
	x = x * -1
if x % 2 == 0:
	print("I'm Even")
else:
	print("I'm Odd.")