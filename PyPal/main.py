import json
import re
import random_answers as ra
# import numpy as np

# Load JSON data
def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


# Store JSON data
response_data = load_json("bot.json")

def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1


        if required_score == len(required_words):

            for word in split_message:

                if word in response["user"]:
                    response_score += 1


        score_list.append(response_score)
        # Debugging: Find the best phrase


    best_response = max(score_list)
    response_index = score_list.index(best_response)


    if input_string == "":
        return "Please type something so we can chat :("

    # If there is no good response, return a random one.
    if best_response != 0:
        return response_data[response_index]["bot"]

    return ra.random_string()

print("Bot: I am the bot of IIIT Nagpur \n I am here to help :) ")

while True:
    f = open("demofile.txt", "a")
    user = input("You: ")
    f.write("You: ")
    f.write(user)
    f.write("\n")
    print("Bot:", get_response(user))
    f.write("Bot: ")
    f.write(get_response(user))
    f.write("\n")
    f.close()


