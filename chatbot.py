import json
import random

with open("intents.json", "r") as file:
    intents = json.load(file)

def get_response(message):
    message = message.lower()

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern in message:
                return random.choice(intent["responses"])

    return "Sorry, I don't understand your question."