import spacy

class SimpleChatbot:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.responses = {
            "greeting": "Hello! How can I assist you today?",
            "goodbye": "Goodbye! Have a great day!",
            "name_query": "I'm a simple chatbot created using spaCy.",
            "default": "I'm sorry, I didn't understand that. Can you please rephrase?"
        }

    def classify_intent(self, user_input):
        """
        Classify user input to identify the intent.
        """
        doc = self.nlp(user_input.lower())
        if any(token.lemma_ in ["hello", "hi", "hey"] for token in doc):
            return "greeting"
        elif any(token.lemma_ in ["bye", "goodbye"] for token in doc):
            return "goodbye"
        elif "your name" in user_input.lower():
            return "name_query"
        else:
            return "default"

    def get_response(self, intent):
        """
        Get the response based on the identified intent.
        """
        return self.responses.get(intent, self.responses["default"])

    def chat(self):
        """
        Start the chatbot conversation.
        """
        print("Chatbot: Hello! Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Chatbot: Goodbye!")
                break
            intent = self.classify_intent(user_input)
            response = self.get_response(intent)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.chat()
