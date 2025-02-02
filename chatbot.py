# Simple Chatbot in Python

import random

# Predefined responses
greetings = ["Hello!", "Hi there!", "Greetings!", "Nice to meet you!"]
farewells = ["Goodbye!", "See you later!", "Bye!", "Have a great day!"]
questions = {
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what's your name": "I'm a simple chatbot. You can call me ChatBot!",
    "what can you do": "I can chat with you, answer simple questions, and tell jokes!",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "who created you": "I was created by a Python programmer.",
}

# Function to generate a response
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Check for greetings
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return random.choice(greetings)

    # Check for farewells
    if any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return random.choice(farewells)

    # Check for predefined questions
    for question, response in questions.items():
        if question in user_input:
            return response

    # Default response
    return "I'm not sure how to respond to that. Can you ask me something else?"

# Main loop
print("ChatBot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye", "exit"]:
        print("ChatBot:", random.choice(farewells))
        break
    response = chatbot_response(user_input)
    print("ChatBot:", response)