#https://github.com/webaverse-studios/webaverse/issues/117
#fixes issues 117

import random
import json
from textblob import TextBlob
from Text_generator import generate_text

class Agent:
    def __init__(self, name, faction, personality):
        self.name = name
        self.faction = faction
        self.personality = personality

    def __str__(self):
        return f"{self.name} ({self.faction}, {self.personality})"

    def respond(self, input_text, previous_conversations):
        tone = self.determine_tone(input_text)
        response = self.generate_response(input_text, tone, previous_conversations)
        return response

    def determine_tone(self, input_text):
        sentiment = TextBlob(input_text).sentiment.polarity
        print(sentiment)
        if self.personality == "Friendly":
            if sentiment > 0:
                return "positive"
            else:
                return "neutral"
        elif self.personality == "Aggressive":
            if sentiment < 0:
                return "Hostile"
            else:
                return "neutral"
        elif self.personality == "Hostile":
            return "Hostile"

        else:  # Reserved personality
            return "neutral"

    def generate_response(self, input_text, tone, previous_conversations):
        prev_points = "\n".join([conv["input_text"] for conv in previous_conversations])
        if prev_points:
            varation_prompt = f"Reply to this from the pov of {self.name} who is part of the {self.faction} faction, return the reply and nothing else. The reply should sound casual and human. The tone should be {tone}:\n{input_text}\nHere are previous conversation points, if they something relevant to the conversation point was mentioned before comment on it otherwise reply normally\n{prev_points}"
        else:
            varation_prompt = f"Reply to this from the pov of {self.name} who is part of the {self.faction} faction, return the reply and nothing else. The reply should sound casual and human. The tone should be {tone}:\n{input_text}"
        return generate_text(varation_prompt)

def load_conversations():
    try:
        with open("conversations.json", "r") as infile:
            return json.load(infile)
    except FileNotFoundError:
        return []

def save_conversations(conversations):
    with open("conversations.json", "w") as outfile:
        json.dump(conversations, outfile)

factions = ["Mages", "Warriors", "Thieves"]
personalities = ["Friendly", "Aggressive", "Reserved","Hostile"]

agent1 = Agent("Alice", random.choice(factions), random.choice(personalities))
agent2 = Agent("Bob", random.choice(factions), random.choice(personalities))

print(agent1)
print(agent2)

previous_conversations = load_conversations()

while True:
    input_text = input("Enter your message: ")

    if input_text.lower() == "quit":
        break

    response1 = agent1.respond(input_text, previous_conversations)
    response2 = agent2.respond(input_text, previous_conversations)

    print(response1)
    print(response2)

    conversation = {
        "input_text": input_text,
        "responses": [
            {"agent": agent1.name, "response": response1},
            {"agent": agent2.name, "response": response2}
        ]
    }

    previous_conversations.append(conversation)
    save_conversations(previous_conversations)
