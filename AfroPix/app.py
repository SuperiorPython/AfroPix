import streamlit as st
import time
from PIL import Image


col1, col2, col3 = st.columns([1, 2, 1])

def change_background_color(color):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

def change_divider_color(color):
    st.markdown(
        f"""
        <style>
        .st-b1 {{ /* This is the class of Streamlit's divider */
            border-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

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
    change_background_color("#E11505")
    with col2:
        if st.button("Hello"):
            st.write_stream(title_stream_data)
            time.sleep(2)
            image = Image.open("IMG_0727.jpg")
            st.image(image, use_container_width=True)
            st.title(":orange[Scarab Legacy]")
        time.sleep(2)
        if st.button("Let's Begin"):
            st.session_state.page = "preferences" # Update session state

def preference_page():
    change_background_color("#E0CD00")
    with col1:
        st.write(prefer_stream_data)
        if st.button("Go Back"):
            st.session_state.page = "title"
    with col2:
        image = Image.open("Martin_Luther_King,_Jr..jpg")
        st.image(image, use_container_width=True)
    with col3:
        st.write("Which topic would you like to learn about?")
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
    st.write("Black Excellence in STEM")
    st.divider()
    st.write("Granville T. Woods \"The Black Edison\" (1880s–1900s)")
    st.write("Granville T. Woods was a prolific African American inventor and electrical engineer, often called 'The Black Edison' due to his contributions to electrical and mechanical engineering. He held over 60 patents, with many focusing on improving railway systems. One of his most significant inventions was the induction telegraph, which allowed trains to communicate with stations and other trains, enhancing railway safety and efficiency. His work greatly influenced the development of modern transportation and electrical systems.")
    st.divider()
    st.write("Marie Van Brittan Brown Inventor of the Home Security System (1966)")
    st.write("In 1966, Marie Van Brittan Brown and her husband patented the first-ever home security system in response to rising crime rates and slow police response times in their neighborhood. Her system featured a closed-circuit television (CCTV) setup, peepholes, a two-way microphone, and an alarm button—the foundation for modern home security systems. Today, her pioneering work continues to influence surveillance technology and smart home security solutions.")
    st.divider()
    st.write("Dr. Shirley Ann Jackson First Black Woman to Earn a Ph.D. from MIT in Physics (1970s–Present)")
    st.write("Dr. Shirley Ann Jackson made history in 1973 as the first Black woman to earn a Ph.D. in theoretical physics from the Massachusetts Institute of Technology (MIT). Her groundbreaking research in particle physics contributed to advancements in fiber optic cables, touch-tone telephones, caller ID, and solar cell technology. She later became the President of Rensselaer Polytechnic Institute, where she continues to inspire future scientists and engineers.")
    st.divider()
    st.write("First Black Astronaut in Space Guion Bluford (1983)")
    st.write("On August 30, 1983, Guion 'Guy' Bluford made history as the first African American to travel to space aboard NASA's STS-8 Space Shuttle Challenger mission. As a U.S. Air Force officer and aerospace engineer, he played a crucial role in space shuttle operations, including satellite deployment and scientific experiments. Over his career, he completed four spaceflights, logging over 688 hours in space, and paving the way for future Black astronauts.")
    st.divider()
    st.write("### Lonnie Johnson's Super Soaker Invention (1989)")
    st.write("While working as a NASA aerospace engineer, Lonnie Johnson accidentally invented the Super Soaker water gun while experimenting with a heat pump system in his home workshop. The high-powered water gun was introduced in 1990 and quickly became one of the best-selling toys of all time, generating over $1 billion in sales. Johnson's expertise in mechanical and nuclear engineering has led him to develop innovations in energy storage and green technology, further cementing his legacy as a great inventor.")
    
    if st.button("Go Back"):
        st.session_state.page = "preferences"

def arts_page():
    change_background_color("#4AE014")
    st.write("Black Excellence in Arts content goes here.")
    st.divider()
    st.write("James Baldwin’s Go Tell It on the Mountain (1953)")
    st.divider()
    st.write("Spike Lee’s Do the Right Thing (1989)")
    st.divider()
    st.write("Alvin Ailey & the Creation of the Alvin Ailey American Dance Theater (1958)")
    st.divider()
    st.write("Jean-Michel Basquiat’s Rise in Contemporary Art (1980s)")
    st.divider()
    st.write("Lorraine Hansberry’s A Raisin in the Sun (1959)")
    if st.button("Go Back"):
        st.session_state.page = "preferences"

def politics_page():
    change_background_color("#4AE014")
    st.write("Black Excellence in Politics content goes here.")
    st.divider()
    st.write("Thurgood Marshall Becomes the First Black Supreme Court Justice (1959)")
    st.divider()
    st.write("The Founding of the Congressional Black Caucus (1971)")
    st.divider()
    st.write("Carol Moseley Braun the First Black Woman in the U.S. Sena (1983)")
    st.divider()
    st.write("John Lewis & the Voting Rights Act (1965)")
    st.divider()
    st.write("Shirley Chisholm Becomes the First Black Woman in Congress (1968)")
    if st.button("Go Back"):
        st.session_state.page = "preferences"

def health_page():
    change_background_color("#4AE014")
    st.write("Black Excellence in Health content goes here.")
    st.divider()
    st.write("Dr. Charles Drew & the Blood Bank Revolution (1940s)")
    st.divider()
    st.write("Dr. Daniel Hale Williams Performs the First Successful Open-Heart Surgery (1893)")
    st.divider()
    st.write("The Black Panther Party’s Free Health Clinics (1960s–1970s)")
    st.divider()
    st.write("The Establishment of Meharry Medical College (1876)")
    st.divider()
    st.write("Mary Eliza Mahoney Becomes the First Black Professional Nurse (1879)")
    if st.button("Go Back"):
        st.session_state.page = "preferences"

def sports_page():
    change_background_color("#4AE014")
    st.write("Black Excellence Intro Message in Sports content goes here.")
    st.divider()
    st.write("Jackie Robinson Breaks the MLB Color Barrier (1947)")
    st.divider()
    st.write("LeBron James Opens the I PROMISE School (2018)")
    st.divider()
    st.write("Kareem Abdul-Jabbar Becomes the NBA’s All-Time Leading Scorer (1984)")
    st.divider()
    st.write("Wilma Rudolph Becomes the First American Woman to Win Three Gold Medals in One Olympics (1960)")
    st.divider()
    st.write("Muhammad Ali Becomes Heavyweight Champion (1964)")
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
