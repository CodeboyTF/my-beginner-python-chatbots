import tkinter as tk
from nltk.chat.util import Chat, reflections

# Define chatbot patterns and responses
pairs = [
    ["Hi|Hello|Hey", ["Hello", "Hey", "Hi"]],
    ["Can you Help me with", ["Yes!! Of course! How may I help you with your career exposure??!"]],
    ["information technology", ["Information technology needs you to have obtained a bachelor's degree in mathematics."]],
    ["bye|goodbye", ["Goodbye!", "See you later!", "Have a great day!"]],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to handle user input and chatbot responses   
def chat_with_bot():
    user_input = input_entry.get()
    response = chatbot.respond(user_input)
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_input}\n")
    chat_log.insert(tk.END, f"Chatbot: {response}\n\n")
    chat_log.config(state=tk.DISABLED)
    input_entry.delete(0, tk.END)

# Function to exit the application
def exit_app():
    root.destroy()

# Create a tkinter window
root = tk.Tk()
root.title("Chatbot")

# Create a chat log area
chat_log = tk.Text(root, state=tk.DISABLED, wrap=tk.WORD)
chat_log.pack(fill=tk.BOTH, expand=True)

# Create an input field
input_entry = tk.Entry(root)
input_entry.pack(fill=tk.BOTH)

# Create a send button
send_button = tk.Button(root, text="Send", command=chat_with_bot)
send_button.pack()

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack()

root.mainloop()
