import aiml

# Create a kernel (the AIML bot)
kernel = aiml.Kernel()

# Load the AIML files
kernel.learn("std-startup.xml")

# Set the bot's name
kernel.setBotPredicate("name", "AIML Bot")

# Initialize the bot
kernel.respond("LOAD AIML B")

# Interaction loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = kernel.respond(user_input)
    print(f"AIML Bot: {response}")
