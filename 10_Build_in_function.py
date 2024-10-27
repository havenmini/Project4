# len() Returns the length of the given SyntaxWarning
name = "namaste \ndnigital nepal"
print(len(name))

# title() Return the string with first letter of every word
print(name.title())

# lower() Returns the string with all upper letter converted to lowercase
print(name.lower())

# Upper() Return the string with all lowercase letters converted to uppercase
print(name.upper())

# count() count no of word
print(name.count("n"))

# find() find word start from -1 when not found
print(name.find("a"))

# index() show error message when not found
print(name.index("a"))

# endswith() Return true if the gven string ends with the supplied substring otherwise return false
print(name.endswith("l"))

# startswith() Return true if the given string stars with the supplied substring otherwise returns fals
print(name.startswith("n"))

# isalum() Return true if character of the given string are either alphabets or nummeric. 
print(name.isalnum())

# isspace() Returns true if the string is non-empty and all characters are white space(blank, tab, newline, carriage return)
print(name.isspace())

# islower() start from lower is true and start from uppor letter and number is false
print(name.islower())

# isupper() start from upper is true and start from lower letter and number is false
print(name.isupper())

# lstrip() Return the string after removing the space only the left the string
print(name.lstrip())

# rstrip() Returns the striping after removing the space only the right of the string
print(name.rstrip())

# strip() Return the script after removing the space both the left and the right ot hte string.
print(name.strip)

# replace(oldstr,newstr) Replace all occurrences of old string with the new string
print(name.replace("n","m"))