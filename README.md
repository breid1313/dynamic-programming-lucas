# Overview
This program provides a Dynamic Programming solution to calculate any desired value in the sequence of Lucas nubmers.
If you are not familiar with Lucas nubmers, they are quite similar to the Fibonacci numbers.
Lucas numbers are defined as: 2 if n=2, 1 if n=1, and Lucas(n-1) + Lucas(n-2) if n > 1.
The Dynamic Programming solution is significantly faster than the recursive solution.

# Usage
Only 1 argument is required to run this program, the number in the sequence (starting from 0) you wish to calculate.
This is provided through the `-n` or `--number` argument.
For example:

`python3 lucas.py -n 0` calculates the 0th element in the sequence of Lucas numbers (2).

`python3 lucas.py -n 10` calculates the 10th element in the sequence of Lucas numbers (123).
