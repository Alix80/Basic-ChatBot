import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data
nltk.download('punkt')

# Define the conversation patterns
patterns = [
    (r"hi|hello|hey", ["Hello! How can I assist you today?", "Hey there! What can I do for you?"]),
    (r"how are you ?", ["I'm just a bot, but I'm functioning properly! How about you?"]),
    (r"(.*) your name ?", ["I am a chatbot created for conversation. You can call me Bot!"]),
    (r"what can you do ?", ["I can chat with you, answer some questions, and help you with simple tasks!"]),
    (r"(.*) help (.*)", ["I am here to help you! What do you need assistance with?"]),
    (r"what is (.*)", ["You can ask me anything, and I will try my best to explain it!"]),
    (r"quit|exit", ["Goodbye! Have a nice day!"]),
]

# Create the chatbot using NLTK's Chat class
chatbot = Chat(patterns, reflections)

# Define the chat function
def start_chat():
    print("Hi, I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Bot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            if response:
                print("Bot:", response)
            else:
                print("Bot: I'm sorry, I don't understand that.")

# Start the chatbot
if __name__ == "__main__":
    start_chat()
