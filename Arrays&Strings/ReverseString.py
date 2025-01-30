def Reverse_string(input_file):
    #Define pointer
    left=0
    right=len(input_file)-1

    while left<right:
        #Swap Steps
        input_file[left],input_file[right]=input_file[right],input_file[left]
        left+= 1
        right-= 1
    return input_file

input_file = ["S", "I", "N", "A"]
reversed_list = Reverse_string(input_file)
print(reversed_list)

