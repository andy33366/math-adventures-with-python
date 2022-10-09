
def sumRange(beg, end):
    running_sum = 0
    for i in range(beg, end+1):
        running_sum += i
    return running_sum

print('from __?')
beginNum=int(input())
print('to __?')
end=int(input())

print(sumRange(beginNum, end))
