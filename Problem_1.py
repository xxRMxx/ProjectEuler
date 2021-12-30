'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''


numbers = []
for i in range(1000):
    if i % 3 == 0:
        numbers.append(i)
    elif i % 5 == 0:
        numbers.append(i)
    else:
        pass

debug = False
if debug:
    print(numbers)

sum = 0
for x in numbers:
    sum += x

# sum of all numbers multiple by 3 or 5    
print(sum)