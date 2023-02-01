# Mad Libs story
story = "Once upon a time, there was a(n) _________ named _________. This person was very _________ and loved to _________. One day, they decided to go on an adventure to _________, where they would meet a(n) _________ who would change their life forever."

# Prompt user for input
adjective = input("Enter an adjective: ")
name = input("Enter a name: ")
verb = input("Enter a verb: ")
noun1 = input("Enter 1st noun: ")
noun2 = input("Enter 2nd noun: ")

# Fill in the blanks with the user input
filled_story = f"Once upon a time, there was man named {name}. This person was very {adjective} and loved to {verb}. One day, he decided to go on an adventure to {noun1}, where he would meet {noun2} who would change their life forever."

# Print the completed story
print(filled_story)