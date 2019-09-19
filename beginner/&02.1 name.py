test1 = 'I told my friend, "Python is my favorite language!"'
test2 = "The language 'Python' is named after Monty Python, not the snake."
test3 = "One of Python's strengths is its diverse and supportive community."
print(test1) #82.8
print(test2) #82.8
print(test3) #82.8

name = "ada lovelace" #82.8
print(name.title())   #notice the A and L, it become uppercase
print(name.upper())	  #print to uppercase
print(name.lower())   #print to lowercase

first_name = "ada"		#85.0
last_name = "lovelace"
full_name = first_name + " " + last_name
#this is called concatenation (combining string)

print(full_name)     
print("Hello, " + full_name.title() + "!") #86.1

#you can use variable to store string
message = "Hello, " + full_name.title() + "!"
print(message)

#\n Newline ; \t Tab
print("Languages:\n\tPython\n\tC\n\tJavaScript") #87.2

#You can strip strings to ensure there are no whitespaces " "
favorite_language = '   python is god   ' #88-89 modified
print(favorite_language.rstrip())	#I want you to look and
print(favorite_language.lstrip())	#realise the whitespaces
print(favorite_language.strip())	#in middle, it remains!
