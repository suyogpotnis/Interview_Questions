"""
Given a list of n integers seperate out all negatives and all positives in O(N)
complexity without using extra space.
Example:
Sample Input:
a = [1,7,-5,4]
output = [-5,1,4,7]

"""
def negativesPositives(a):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
#         print(a[i],a[j])
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
            else:
                pass
    return a
