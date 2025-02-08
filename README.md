# AI-CHATBOT-WITH-NLP

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: VIVEK VARDHAN VENKATA NAGA SARASWATI

*INTERN ID*: CT08SKU

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

### Description: AI Chatbot with NLP(Natural Language Processing)

**Introduction**

The development of chatbots has revolutionized the way users interact with applications, providing immediate and automated responses to queries. This theory explains how to build a simple rule-based chatbot in Python using `spaCy`, a popular natural language processing (NLP) library. The chatbot can recognize basic user intents, such as greetings and farewells, and respond accordingly.

**Understanding Chatbot Components**

1. **Natural Language Processing (NLP)**
   
   NLP is a field of artificial intelligence that enables computers to understand, interpret, and respond to human language. The chatbot leverages `spaCy`, which provides pre-trained models capable of tokenization, part-of-speech tagging, and named entity recognition.

2. **User Intent Classification**
   
   Intent classification is a critical component of chatbots. It involves identifying the user’s goal based on their input. In this chatbot, intents like greetings, goodbyes, and inquiries about the chatbot's name are predefined.

3. **Response Generation**
   
   For each recognized intent, the chatbot returns a corresponding response. If the input does not match any predefined intent, a default response is generated.

**Implementation Steps**

1. **Loading the Language Model**

   The `en_core_web_sm` model is loaded using `spacy.load()`. This model provides essential NLP features required for processing user input.

   ```python
   self.nlp = spacy.load("en_core_web_sm")
   ```

2. **Classifying User Intent**

   The chatbot uses `spaCy` to process user input and checks for specific keywords or phrases to classify intents. For instance, if the input contains "hello" or "hi," the chatbot classifies it as a greeting.

   ```python
   if any(token.lemma_ in ["hello", "hi", "hey"] for token in doc):
       return "greeting"
   ```

3. **Generating Responses**

   Based on the classified intent, the chatbot selects an appropriate response from the predefined dictionary:

   ```python
   self.responses = {
       "greeting": "Hello! How can I assist you today?",
       "goodbye": "Goodbye! Have a great day!",
       "name_query": "I'm a simple chatbot created using spaCy.",
       "default": "I'm sorry, I didn't understand that. Can you please rephrase?"
   }
   ```

4. **Starting the Chat Session**

   The chatbot continues to interact with the user until the user types "exit." The `while` loop ensures the conversation remains active:

   ```python
   while True:
       user_input = input("You: ")
       if user_input.lower() == "exit":
           print("Chatbot: Goodbye!")
           break
       intent = self.classify_intent(user_input)
       response = self.get_response(intent)
       print(f"Chatbot: {response}")
   ```

**Advantages of the Approach**

1. **Modularity:** The chatbot is easily extensible by adding more intents and responses.
2. **Efficiency:** By leveraging `spaCy`, the chatbot performs NLP tasks quickly and efficiently.
3. **Simplicity:** The rule-based approach is straightforward and suitable for basic conversational use cases.

**Limitations and Future Improvements**

- The current chatbot is rule-based and limited in its ability to handle complex conversations.
- Incorporating machine learning techniques, such as intent detection models, would make the chatbot more robust.
- Enhancing the NLP pipeline to support named entity recognition and context-aware responses could further improve user interactions.

**Conclusion**

This simple chatbot implementation demonstrates the power of Python and NLP libraries like `spaCy` in building conversational agents. While basic, it provides a strong foundation for developing more sophisticated chatbots capable of handling dynamic user queries.

#OUTPUT

