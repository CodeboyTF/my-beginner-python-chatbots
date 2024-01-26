
import nltk
from nltk.chat.util import Chat , reflections

Pairs = [
  ["Hi|Hello|Hey", ["Hello","Hey","Hi"]],
  ["Can you Help me with",["Yes!!Ofcause how may i help you with your career exposure??!"]],
  ["information technology",["information technology needs you to have obtain a bachelor in matric"]],
  ["bye|goodbye", ["Goodbye!", "See you later!", "Have a great day!"]],
]

Live_chatbot = Chat(Pairs, reflections)

def chat_with_bot():
    print("Hello! I'm your chatbot. You can start a conversation. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = Live_chatbot.respond(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    chat_with_bot()
