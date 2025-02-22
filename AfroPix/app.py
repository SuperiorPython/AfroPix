import streamlit as st
import time
from streamlit_timeline import timeline
import pandas as pd



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
    with col1:
        st.write(prefer_stream_data)
        if st.button("Go Back"):
            st.session_state.page = "title"
            title_page()
    with col2:
        if st.button("Black Excellence in STEM"):
            st.session_state.page = "stem"
        if st.button("Black Excellence in Arts"):
            st.session_state.page = "arts"
        if st.button("Black Excellence in Politics"):
            st.session_state.page = "politics"
        if st.button("Black Excellence in Health"):
            st.session_state.page = "health"
        if st.button("Black Excellence in Sports"):
            st.session_state.page = "sports"


def stem_page():
    st.write("Black Excellence in STEM content goes here.")
    st.divider()
    st.write("Granville T. Woods – “The Black Edison\”")
    st.divider()
    st.write("Marie Van Brittan Brown – Inventor of the Home Security System")
    st.divider()
    st.write("Dr. Shirley Ann Jackson – First Black Woman to Earn a Ph.D. from MIT in Physics")
    st.divider()
    st.write("First Black Astronaut in Space – Guion Bluford")
    st.divider()
    st.write("Lonnie Johnson’s Super Soaker Invention")
    if st.button("Go Back"):
        st.session_state.page = "preferences"

def arts_page():
    st.write("Black Excellence in Arts content goes here.")
    st.divider()
    st.write("James Baldwin’s Go Tell It on the Mountain")
    st.divider()
    st.write("Spike Lee’s Do the Right Thing")
    st.divider()
    st.write("Alvin Ailey & the Creation of the Alvin Ailey American Dance Theater")
    st.divider()
    st.write("Jean-Michel Basquiat’s Rise in Contemporary Art")
    st.divider()
    st.write("Lorraine Hansberry’s A Raisin in the Sun")
    if st.button("Go Back"):
        st.session_state.page = "preferences"

def politics_page():
    st.write("Black Excellence in Politics content goes here.")
    st.divider()
    st.write("Thurgood Marshall the First Black Supreme Court Justice")
    st.divider()
    st.write("The Founding of the Congressional Black Caucus")
    st.divider()
    st.write("Carol Moseley Braun the First Black Woman in the U.S. Sena")
    st.divider()
    st.write("John Lewis & the Voting Rights Act")
    st.divider()
    st.write("Shirley Chisholm Becomes the First Black Woman in Congress")
    if st.button("Go Back"):
        st.session_state.page = "preferences"

def health_page():
    st.write("Black Excellence in Health content goes here.")
    st.divider()
    st.write("Event 1")
    st.divider()
    st.write("Event 2")
    st.divider()
    st.write("Event 3")
    st.divider()
    st.write("Event 4")
    st.divider()
    st.write("Event 5")
    if st.button("Go Back"):
        st.session_state.page = "preferences"

def sports_page():
    st.write("Black Excellence Intro Message in Sports content goes here.")
    st.divider()
    st.write("Event 1")
    st.divider()
    st.write("Event 2")
    st.divider()
    st.write("Event 3")
    st.divider()
    st.write("Event 4")
    st.divider()
    st.write("Event 5")
    if st.button("Go Back"):
        st.session_state.page = "preferences"


# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "title"

# Page routing
if st.session_state.page == "title":
    title_page()
elif st.session_state.page == "preferences":
    preference_page()
elif st.session_state.page == "stem":
    stem_page()
elif st.session_state.page == "arts":
    arts_page()
elif st.session_state.page == "politics":
    politics_page()
elif st.session_state.page == "health":
    health_page()
elif st.session_state.page == "sports":
    sports_page()
