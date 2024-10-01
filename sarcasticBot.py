import random

# List of sarcastic responses
sarcastic_responses = [
    "Oh, wow! I never would have guessed that.",
    "Really? Tell me more. I am on the edge of my seat.",
    "Oh sure, because that's totally how things work.",
    "I think you are a roach..oh sorry coach!",
    "I would rather die",
    "Then throw yourself",
    "Jump of a cliff",
    "Yeah, right. And I'm the queen of England.",
    "No way! That's totally... not surprising at all.",
    "Wow, you're a real genius, aren't you?",
    "Go...check the mirror",
    "Better than you.smirk"
 
]

def chatbot():
    print("Welcome to the Sarcastic Chatbot. Say something, and I'll try my best not to laugh.")

    while True:
        # Taking user input
        user_input = input("You: ")

        # Exit condition check (case-insensitive)
        if user_input.lower() in ["exit", "quit","bye","stop","stop it"]:
            print("Chatbot: Oh, leaving so soon? I'll definitely miss you. eye roll")
            break

        # Select a random sarcastic response
        response = random.choice(sarcastic_responses)
        print("Chatbot: " + response)

# Run the chatbot function
if _name_ == "_main_":
    chatbot()
