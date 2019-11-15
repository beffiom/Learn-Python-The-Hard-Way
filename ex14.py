from sys import argv

# accepts two terminal argument, the name and rank of the user
script, user_name, rank = argv
# prompt variable so the user has a uniform prompt
prompt = '--> '

print(f"Hi rank {rank} user {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
# prompts the users for a series of questions
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# returns a statement incorporating the user's answers
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
