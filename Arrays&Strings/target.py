nums=[1,2,4,6,8,9,14,15]
target=13
def check_for_target(nums,target):
    left=0
    right=len(nums)-1
    while left<right:
        current=nums[left]+nums[right]
        if current==target:
            print(f"The Numbers SUm for Target is {nums[right]} {nums[left]}")
        if current>target:
            right-=1
        else:
            left+=1
    return False
check_for_target(nums, target)