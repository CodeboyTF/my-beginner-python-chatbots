
import tkinter as tk
from nltk.chat.util import Chat, reflections


career_advice_pairs = [
    ["how to write a resume", ["To write a great resume, focus on your achievements and use action verbs.", "A well-structured resume includes a summary, work experience, skills, and education."]],
    ["job interview tips", ["Prepare for interviews by researching the company, practicing common questions, and dressing professionally."]],
    ["career change advice", ["Consider your skills, interests, and values when planning a career change. Networking and upskilling can be beneficial."]],
    ["quit", ["Thank you for using the career advice chatbot. Goodbye!"]],
]


career_advice_bot = Chat(career_advice_pairs, reflections)


def send_message():
    user_input = input_entry.get()
    response = career_advice_bot.respond(user_input)
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "You: " + user_input + "\n")
    chat_box.insert(tk.END, "Career Bot: " + response + "\n")
    chat_box.config(state=tk.DISABLED)
    input_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Career Advice Chatbot")

chat_box = tk.Text(root, state=tk.DISABLED)
input_entry = tk.Entry(root)
send_button = tk.Button(root, text="Send", command=send_message)

chat_box.pack()
input_entry.pack(fill=tk.BOTH)
send_button.pack()

root.mainloop()
