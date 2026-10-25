
def chatbot_response(user_input):
    message = user_input.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hi! Welcome to the Basic Chatbot."

    elif message == "how are you":
        return "I'm fine, thanks! How can I help you?"

    elif message == "what is your name":
        return "I'm CodeAlpha Chatbot, your virtual assistant."

    elif message == "help":
        return "You can say hello, ask how I am, or say bye."

    elif message in ["bye", "exit", "quit"]:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand. Please try another message."


def main():
    print("=== CODEALPHA BASIC CHATBOT ===")
    print("Type 'help' for options and 'bye' to exit.")

    while True:
        user_input = input("\nYou: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break


if __name__ == "__main__":
    main()
