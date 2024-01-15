import random

class ChatBot:
    def __init__(self):
        self.greeted = False
        self.farewelled = False
        self.conversation_history = []

    def greet(self):
        self.greeted = True
        return random.choice(["Hello there!", "Hi! How can I help you today?", "Hey, what's up?"])

    def farewell(self):
        self.farewelled = True
        return random.choice(["Goodbye!", "Have a great day!", "See you next time!"])

    def handle_question(self, question):
        responses = {
            "what is your name": "My name is Simple Chatbot.",
            "what can you do": "I can answer simple questions and have conversations.",
            "how are you": "I'm doing well, thanks for asking!",
            "what is your favorite color": "I don't have a favorite color, but I like blue and green.",
            "what is the weather like today": "It's currently sunny and warm in my digital world.",
        }
        return responses.get(question.lower(), "I'm not sure I understand that question.")

    def ask_questions(self):
        questions = ["What's your name?", "What do you like to do in your free time?", "What's your favorite food?"]
        for question in questions:
            answer = input(question + " ")
            print("That's cool! Hi " + answer)
            self.conversation_history.append(answer)

    def process_user_input(self, user_input):
        if user_input.lower() in ["goodbye", "bye", "quit"]:
            return self.farewell()
        elif user_input.lower().startswith(("what", "how")):
            response = self.handle_question(user_input)
            return f"Simple Chatbot: {response}"
        else:
            try:
                self.ask_questions()
            except ValueError:
                return "Simple Chatbot: I'm not sure I understand. Could you rephrase?"

def main():
    chatbot = ChatBot()
    print(chatbot.greet())

    while True:
        user_input = input("You: ")
        chatbot.conversation_history.append(user_input)

        if user_input.lower() in ["goodbye", "bye", "quit"]:
            print(chatbot.farewell())
            break
        else:
            response = chatbot.process_user_input(user_input)
            print(response)

if __name__ == "__main__":
    main()