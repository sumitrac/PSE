'''
input: [1, 3, 5, 7]  [9]
output: [1, 3, 5, 7, 9]

input: [-20, 0, 20] [0, 5, 7, 12]
output: [-20, 0, 5, 7, 12, 20]
'''
def merge_list(nums1, nums2):
    new_list = []
    i = 0
    j = 0 

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            new_list.append(nums1[i])
            i+=1
        else:
            new_list.append(nums2[j])
            j+=1
    # if i < len(nums1):
    #     for n in range(i, len(nums1)):
    #         new_list.append(nums1[n])

    if j < len(nums2):
        for n in range(j, len(nums2)):
            new_list.append(nums2[n])

    return new_list

nums1 = [1, 3, 5, 7]
nums2 = [9, 20]
print(merge_list(nums1, nums2))
