def findMaxAverage(nums,k):
    #Sum of first
    sum_array = sum(nums[:k])
    max_sum = sum_array
    for i in range(len(nums)-k):
        sum_array = sum_array-nums[i]+nums[i+k] #Delete the last and add new
        max_sum = max(max_sum,sum_array)

    return max_sum/k
nums = [1, 12, -5, -6, 50, 3]
k = 4
result = findMaxAverage(nums, k)
print(result)



