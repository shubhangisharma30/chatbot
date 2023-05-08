import random


responses = {
    "hi": ["Hello!", "Hi there!"],
    "hello": ["Hi there!", "Hello!"],
    "how are you": ["I'm good, thank you.", "I'm doing fine, thanks for asking!"],
    "what is your name": ["My name is Chatbot.", "I'm Chatbot!"],
    "bye": ["Goodbye!", "See you later."]
}


print("Hi, I'm Chatbot. How can I help you today?")
while True:
    user_input = input("You: ").lower()
    chatbot_response = None
    
    
    for key in responses.keys():
        if key in user_input:
            chatbot_response = random.choice(responses[key])
            break
    
    
    if not chatbot_response:
        chatbot_response = "Sorry, I did not understand that."
    
    print("Chatbot:", chatbot_response)
    
    # Exit chatbot if user says bye
    if user_input == 'bye':
        break
