import nltk
nltk.download('punkt')
from nltk.chat.util import Chat, reflections

# Download required data
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I’m your AI Chatbot. 😊"]
    ],
    [
        r"how are you ?",
        ["I'm doing well! How about you?", "I'm just a bot, but I'm working perfectly!"]
    ],
    [
        r"(.*) your name ?",
        ["You can call me ChatBuddy!", "I'm ChatBot, your assistant."]
    ],
    [
        r"(.*) help (.*)",
        ["I can help you with general questions. Try asking me something!"]
    ],
    [
        r"(.*) (weather|temperature) (.*)",
        ["I'm not connected to live weather yet, but I can help you build a weather bot!"]
    ],
    [
        r"(.*) created you ?",
        ["I was created by Aman using Python and NLTK. 🔧"]
    ],
    [
        r"(.*)(bye|exit|quit)",
        ["Goodbye! Have a great day. 👋", "Bye! Talk to you soon."]
    ],
    [
        r"(.*)",
        ["Sorry, I didn’t understand that. Can you rephrase?"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chatting
print("🤖 ChatBot: Hello! I'm your chatbot. Type 'bye' to exit.")
chatbot.converse()
