nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3 
def merge(nums1, nums2):
    two_list = nums1 + nums2
    two_list.sort()
    return two_list

print (merge(nums1, nums2))