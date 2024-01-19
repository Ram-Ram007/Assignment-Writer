import streamlit as st

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi there! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but thanks for asking!"
    elif "your name" in user_input:
        return "I'm a friendly chatbot."
    else:
        return "I'm sorry, I didn't understand that. Ask me another question!"

def main():
    st.title("Simple Chatbot")

    # Input for the user's question
    user_question = st.text_input("Ask me a question")

    # Button to get chatbot response
    if st.button("Get Response"):
        chatbot_response_text = chatbot_response(user_question)
        st.write("Chatbot: ", chatbot_response_text)

if __name__ == "__main__":
    main()
