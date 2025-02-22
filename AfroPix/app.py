import streamlit as st
import time

def stream_data():
    intro_message = """
    Hello viewer. I see you have decided to partake in soaking in the knowledge of 
    African-American history and our achievements. Allow us to introduce you to our website.
    """
    for word in intro_message.split(" "):
        yield word + " "
        time.sleep(0.1)

def title_page():
    if st.button("Hello"):
        st.write_stream(stream_data)
        time.sleep(2)
        st.title(":orange[Scarab Legacy]")
        time.sleep(2)
        if st.button("Let's Begin"):
            st.session_state.page = "preferences" # Update session state

def preference_page():
    st.write("Hello")
    if st.button("Go Back"):
        st.session_state.page = "title"

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "title"

# Page routing
if st.session_state.page == "title":
    title_page()
elif st.session_state.page == "preferences":
    preference_page()