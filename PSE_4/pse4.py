import string
def is_Palindrome(input_string):
    input_string = input_string.lower() #convert string to lowercase
    #s = s.translate(None, string.punctuation) #removes all punctuation
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
  
# Removing punctuations in string
# Using loop + punctuation string
    for element in input_string: 
        if element in punc: 
            input_string = input_string.replace(element, "")

    input_string = input_string.replace(" ", "") #removes all white space 
        
    print(input_string)
    print(input_string[::-1])
    return input_string == input_string[::-1] #checks string to reverse string 

string_1 = "Apple"
string_2 = "Radar"
string_3 = "Dammit I'm mad."    

print(is_Palindrome(string_1))
print(is_Palindrome(string_2))
print(is_Palindrome(string_3))





