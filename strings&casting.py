# # strings and Casting
#
# # Let's habe a look at some industry practices
# # single and double quotes
#
#
# # single_quotes = 'single quotes \'Wow\''
# # double_quotes = "double quotes 'Wow'"
# # print(single_quotes)
# # print(double_quotes)
#
# # string slicing
#
# greetings = 'hello world!' # string
# # indexing in Python starts from 0
# # H e l l o   w o r l d !
# # 0 1 2 3 4 5 6 7 8 9 10 11
# # H   E   L  L  0  W  O  R L   D  !
# #-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# # how can we fid out the length of this statement/string
#
# # print(len(greetings))
# # We have a method called len() to find out the total length of the statement/string
# #
# # print(greetings[0:5])
# #
# # print(greetings[6:11])
# # print(greetings[-6:])
#
# #reverse indexing starts with -1
#
#
#
#
# # Let's have a look at some string methods
# # white_space = "lot's of space at the end    "
# # strip helps us delete all white spaces
# # print(len(white_space))
# # print(len(white_space.strip()))
#
#
# # print(len(white_space))
# Example_text ="here's Some texts with lot's of text"
# print(Example_text.count("text"))
#
# #counts the number of times the word is mentioned in the statement
# print(Example_text)
# print(Example_text.upper()) # turns the string into all uppercase letters
# print(Example_text.lower()) # Turns the string into all lowercase letters
# print(Example_text.capitalize()) # Capitalizes first letter of the string
# print(Example_text.replace("with", ",")) # will replace the word "with" with "," in this case

#Concatenation and Casting
age = 99 # int
first_name = "Ben"
last_name = "Jerry"
print(first_name + " "  + last_name)

# F - String is an amazing magical formatting f
print(f"Your first name is {first_name} and your last name is {last_name} is {age} old")












