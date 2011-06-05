#! /usr/bin/env python

sum1 = 0
num1 = 3
num2 = 3

while num2<1000:
    sum1 = sum1 + num2
    num2 = num2 + num1

sum2 = 0
num1 = 5
num2 = 5

while num2<1000:
    sum2 = sum2 + num2
    num2 = num2 + num1

sum3 = 0
num1 = 15
num2 = 15

while num2<1000:
    sum3 = sum3 + num2
    num2 = num2 + num1

answer = sum1 + sum2 - sum3
print answer

exit(0)
