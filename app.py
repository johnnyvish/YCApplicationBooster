import streamlit as st

def get_greeting(name):
    return f"Hello, {name}! Welcome to the Streamlit app."

def main():
    st.title("My Streamlit App")
    
    name = st.text_input("Enter your name")
    if name:
        greeting = get_greeting(name)
        st.write(greeting)

if __name__ == "__main__":
    main()