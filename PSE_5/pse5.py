# num_list = [5, 3, 4, 2, 8, -1]
# num_list = [10, 10, 12, 8, 18, 2]
num_list = [5, 3, 4, 2, 8, -1, 3]
# len_num_list = len(num_list)
# given_sum = 7


# def pair_sum(k):
#     count = 0
#     lookup = [] #set()
#     for num in num_list:
#         if k-num in lookup:
#             count +=1
#         else:
#             lookup.append(num)
#     return count
    
# print("Count of pairs is", pair_sum(7))

def pairs_with_given_sums(num_list, len_input_num, given_sum): 
    count = 0  # Initialize result
    # Consider all possible pairs
    # and check their sums
    for i in range(0, len_input_num): 
        for j in range(i + 1, len_input_num):
            if input_num[i] + input_num[j] == given_sum:
                count += 1
    return count

input_num = [5, 3, 4, 2, 8, -1, 3, 7, 0] #[1, 5, 7, -1, 5]
len_input_num = len(input_num)
given_sum = 7
print(f"The given sum is {given_sum}")
print("Count of pairs is", pairs_with_given_sums(num_list, len_input_num, given_sum))