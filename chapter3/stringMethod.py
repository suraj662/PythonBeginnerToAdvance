str= "Suraj yadav"
print(str.upper())
print(str.lower())
print(str.title())
print(str.find("ng"))
print(str.replace("yadav", "Best"))
print(str.count("a")) #count the occurence

#escape sequence

print("Hello World")
print("Hello\nWorld")
print("Hello \t World")


#Task1 --
#convert the text-based into emojis
msg = input("Enter a message")

# Replace text smileys with actual emojis sequentially
msg = msg.replace(":)", "😊")
msg = msg.replace(":(", "🙁")
msg = msg.replace(":D", "😃")
msg = msg.replace(";)", "😉")

# Print the final converted message
print(msg)

#I/P -  Enter your message: Hello :) I am learning Python from Saumya :D
#O/P -  Hello 😊 I am learning Python from Saumya 😃


#Task2 --
#Problem: Write a program that takes a sentence as input and prints:
#Total characters (len())
#Uppercase version
#Lowercase version

# Take a sentence as input from the user
sentence = input("Input: ")

# Calculate the required outputs
total_chars = len(sentence)
upper_version = sentence.upper()
lower_version = sentence.lower()

# Print the results in the exact format required
print("Output:")
print(f"Total characters: {total_chars}")
print(f"Uppercase: {upper_version}")
print(f"Lowercase: {lower_version}")


#Task3 --
#Problem: Write a Python program that takes any word or sentence as input and prints:
#The first character
#The last character
#The total number of characters

# Take a word or sentence as input
text = input("Enter a word or sentence: ")

# Check if the input is empty to avoid errors
if len(text) > 0:
    first_char = text[0]       # Index 0 gets the first character
    last_char = text[-1]       # Index -1 gets the last character
    total_chars = len(text)    # len() gets the total count

    # Print the results
    print(f"The first character: {first_char}")
    print(f"The last character: {last_char}")
    print(f"The total number of characters: {total_chars}")
else:
    print("You didn't enter anything!")
