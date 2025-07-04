# chatbot_if_else.py
# Simple rule-based chatbot using if-elif-else statements

print("Hi! I'm Chatty, your chatbot. Type 'bye' to exit.")

def chatbot():
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatty: Hello! How can I assist you today?")
        elif "how are you" in user_input:
            print("Chatty: I'm just code, but I'm doing great! 😄")
        elif "name" in user_input or "who are you" in user_input:
            print("Chatty: I'm Chatty — your friendly chatbot!")
        elif "your age" in user_input or "old are you" in user_input:
            print("Chatty: I was created just now, so I'm pretty young! 🤖")
        elif "help" in user_input:
            print("Chatty: I can answer greetings, tell you about myself, and respond to basic queries.")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatty: Goodbye! Have a wonderful day! 👋")
            break
        else:
            print("Chatty: I'm not sure how to respond to that. Try saying 'help'.")



if __name__ ==  '__main__':
    chatbot()