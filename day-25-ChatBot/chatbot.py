



# def ChatBot():
#     print("Hello ! I am your python chatbot . Type exit to quit.")
#     while True:
#         user_input = input("You: ").lower()
#         if user_input == "exit":
#             print("ChatBot: GoodBye ! Have a great day !")
#             break
#         elif "hello" in user_input or "hi" in user_input:
#             print("ChatBot: Hello! How can I assist you today ?")
#         elif "how are you" in user_input:
#             print("ChatBot: I'm doing great, thanks for asking!")
#         elif "your name" in user_input:
#             print("Chatbot: I'm your helpful Python chatbot.")
#         else:
#             print("ChatBot: Sorry, I didn't understand that. Can you try again later ")

# def ChatBot():
#     print("Hello! I am your Python chatbot. Type exit to quit.")
#     while True:
#         user_input = input("You: ").lower()
#         intent = detect_intent(user_input)
#         if intent:
#             print("ChatBot:", intent_responses[intent])
#             if intent == "goodbye":
#                 break
#         else:
#             print("ChatBot: Sorry, I didn't understand that. Can you try again later?")

# Example
from datetime import datetime

intent_keywords = {
    "greet": ["hello", "hi", "hey"],
    "how_are_you": ["how are you", "how r u"],
    "name": ["your name"],
    "goodbye": ["bye", "exit", "quit"],
    "project_info": ["project", "github", "portfolio"],
}

intent_responses = {
    "greet": "Hello! How can I assist you today?",
    "how_are_you": "I'm doing great, thanks for asking!",
    "name": "I'm your helpful Python chatbot.",
    "goodbye": "GoodBye! Have a great day!",
    "project_info": "You can see my code on GitHub at https://github.com/ketkivmohite/python-aiml-projects.",
}

def detect_intent(user_input):
    for intent, keywords in intent_keywords.items():
        for keyword in keywords:
            if keyword in user_input:
                return intent
    return None

def ChatBot():
    print("Hello! I am your Python chatbot. Type exit to quit.")
    while True:
        user_input = input("You: ").lower()
        intent = detect_intent(user_input)
        if intent:
            bot_response = intent_responses[intent]
            print("ChatBot:", bot_response)
            # Logging conversation
            time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("chat_log.txt", "a") as log_file:
                log_file.write(f"[{time_stamp}] You: {user_input}\n")
                log_file.write(f"[{time_stamp}] ChatBot: {bot_response}\n")
            if intent == "goodbye":
                break
        else:
            bot_response = "Sorry, I didn't understand that. Can you try again later?"
            print("ChatBot:", bot_response)
            time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("chat_log.txt", "a") as log_file:
                log_file.write(f"[{time_stamp}] You: {user_input}\n")
                log_file.write(f"[{time_stamp}] ChatBot: {bot_response}\n")

if __name__ == "__main__":
    ChatBot()
