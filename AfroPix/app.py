import streamlit as st
import time

col1, col2, col3 = st.columns([1, 2, 1])



def title_stream_data():
    intro_message = """
    Welcome to Scarab Legacy - where African-American History is reborn, reimagined, and remembered.
    Scarab Legacy offers innovative options to allow users to increase their knowledege on African-American
    History. Welcome to Scarab Legacy.
    """
    for word in intro_message.split(" "):
        yield word + " "
        time.sleep(0.1)

def prefer_stream_data():
    prefer_message = """
        We're estactic you want to celebrate the vast remarkable acheivements of African-American History,
        we have an expansize selection that you can choose from pertaining to acheivements in African-American History.
        """
    for word in prefer_message.split(" "):
        yield word + " "
        time.sleep(0.1)

def title_page():
    with col2:
        if st.button("Hello"):
            st.write_stream(title_stream_data)
            time.sleep(2)
            st.title(":orange[Scarab Legacy]")
        time.sleep(2)
        if st.button("Let's Begin"):
            st.session_state.page = "preferences" # Update session state

def preference_page():
    with col2:
        st.write(prefer_stream_data)
    if st.button("Go Back"):
        st.session_state.page = "title"
        title_page()

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "title"

# Page routing
if st.session_state.page == "title":
    title_page()
elif st.session_state.page == "preferences":
    preference_page()
