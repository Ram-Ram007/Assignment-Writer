import streamlit as st
import wikipedia
from wikipedia.exceptions import DisambiguationError
from txt2hnd import text_to_handwritten

def main():
    st.title("Assignments Writer APP!!")
    title = st.text_input("What's your Title?")
    n = st.slider("Number of lines?", min_value=1, max_value=100)
    submit = st.button("Write")

    if submit and title:
        try:
            data = wikipedia.summary(title, sentences=n)
            handwritten_path = text_to_handwritten(data)
            st.image(handwritten_path)
        except DisambiguationError as e:
            st.warning(f"Disambiguation Error: {e}")
            options = e.options
            selected_option = st.selectbox("Select a specific page:", options)
            try:
                data = wikipedia.summary(selected_option, sentences=n)
                handwritten_path = text_to_handwritten(data)
                st.image(handwritten_path)
            except wikipedia.exceptions.PageError:
                st.error(f"Error: Unable to retrieve information for '{selected_option}'.")

if __name__ == '__main__':
    main()
