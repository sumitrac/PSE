#List Intersection 
list1 = [1, 2, 3]
list2 = [1, 2, 4, 3]

# #output = [1, 2]

def list_inter(list1, list2):
    list3 = []

    for i in list1:
        if i in list2:
            list3.append(i)
    return list3 

print(list_inter(list1, list2))


#string Interaction 
str1 = "Apple"
str2 = "Honeybee"
#output = Apple

def str_inter(str1, str2):
    new_string = " "

    for i in str1:
        if i in str2 and i not in new_string:
            new_string += i
    return new_string 

print(str_inter(str1, str2))

