"""
Write a function to find the missing number in a given integer array of 1 to 100.

Example

missing_number([1, 2, 3, 4, 6], 6) # 5
"""

numArr = [1,2,3,4,6]

def missingNumber(arr):
    for i in range(0, len(arr)):
        if i+1 != arr[i]:
            return i+1

print(missingNumber(numArr))