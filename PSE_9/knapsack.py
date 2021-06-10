# Given an array of integers and a target sum, determine the sum 
# nearest to but not exceeding the target that can be created. 

# To create the sum, use any element of your <---array zero or more times.-->

# For example, if `arr = [2, 3, 4]` and your target sum is 10, 
# you might select `[2, 2, 2, 2, 2]`, `[2, 2, 3, 3]`, `[3, 3, 4]` or `[2, 4, 4]`. 

# In this case, you can arrive at exactly the target.

# **Sample Input**
# k = 12 arr = [1, 6, 9]   
# **Sample Output**
# 12 => could be (6+6) or (1+1+1+1+1+1+1+1+1)

# **Sample Input**
# k = 11 arr = [2, 4, 6]
# **Sample Output**
# 10 => could be (4 + 6) or (2 + 2 + 2 + 2 + 2)

#pseudocode 
# Check if sum of arr element == target sum 
# if True, return target sum value 

# if not, start the loop to check if num/nums add up to the target sum 
# if True, return target sum 

# edge cases 
# if added nums is greater than target sum, skip 

# if added nums is less than target sum, 
# check which one is nearest num and return that num 


