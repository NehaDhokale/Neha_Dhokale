import re 
string = input("enter a string:")
if re.fullmatch(r'[a-zA-Z0-9]+', string):
    print("string contains a-z A-Z 0-9")
else:
    print("string contains other characters")