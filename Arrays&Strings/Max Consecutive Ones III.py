def longestOne(nums,k):
    left = 0 #Start Window
    max_length = 0 #The Largest length that find
    zero_count = 0 #The number of zeros inculde window
    for right in range(len(nums)):
        if nums[right] ==0:
            zero_count+=1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left+=1
        max_length = max(max_length,right-left+1)
    return max_length
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
result = longestOne(nums,k)
print(result)

