import streamlit as st
import random

def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hi", "hello", "hey"]
    feelings = ["how are you", "how do you do", "how are you doing"]
    names = ["your name", "who are you", "what's your name"]
    
    if any(greeting in user_input for greeting in greetings):
        return random.choice(["Hi there!", "Hello!", "Hey!"])
    elif any(feeling in user_input for feeling in feelings):
        return random.choice(["I'm just a chatbot, but thanks for asking!", "I'm doing well, thanks!"])
    elif any(name in user_input for name in names):
        return random.choice(["I'm a friendly chatbot.", "You can call me ChatBot."])
    else:
        return "I'm sorry, I didn't understand that. Ask me another question!"

def main():
    st.title("Enhanced Chatbot")

    # Input for the user's question
    user_question = st.text_input("Ask me a question")

    # Button to get chatbot response
    if st.button("Get Response"):
        chatbot_response_text = chatbot_response(user_question)
        st.write("Chatbot: ", chatbot_response_text)

if __name__ == "__main__":
    main()
