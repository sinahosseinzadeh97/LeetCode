def combine(arr1,arr2):

    #variable for store final array
    final_array= []
    #Define i,j for pointer
    i=j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            final_array.append(arr1[i])
            i+=1
        else:
            final_array.append(arr2[j])
            j+=1
    while i<len(arr1):
        final_array.append(arr1[i])
        i+=1
    while j<len(arr2):
        final_array.append(arr2[j])
        j+=1
    print(final_array)

arr1=[1,4,7,20]
arr2=[3,5,6]
combine(arr1,arr2)

