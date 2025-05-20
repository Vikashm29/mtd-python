'''
A company wishes to encode its data. The data is in the form of a string and is case sensitive. They wish to encode the data with respect to a specific character. They wish to count the number of times the character reoccurs in the given data so that they can encode the data accordingly.

> Data is in the form of string and is case sensitive.
> They wish to count the number of times the character reoccurs.

define count_specific_character
read data and coder (in sting form and case sensitive)
coder = 1
count occurences of the character in the string
'''

str_data = input("Enter the input string to be encoded:")
search_char = input("Enter the character to be counted:")

count_of_search_char = str_data.count(search_char) # case sensitive
count_of_search_char = str_data.lower().count(search_char.lower()) # case in sensitive

print(f'The character {search_char} is found {count_of_search_char} times in the {str_data}')