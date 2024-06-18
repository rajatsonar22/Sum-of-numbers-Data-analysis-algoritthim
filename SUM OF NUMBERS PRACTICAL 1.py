# Practical no .
# TO FIND THE ADDITION OF THE LIST NUMBERS

print(""" >>>THE SUM OF NUMBERS OF THE LIST GIVEN BELOW
            [1,2,3,4,5]""")
print("")#....space
def sum_num(num):
    total = 0
    for n in num:
        total += n
    return total
print("--- The sum of numbers are :",sum_num([1,2,3,4,5]))
