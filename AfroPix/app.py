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
    st.write("Black Excellence in Arts")
    st.divider()
    st.write("James Baldwin's *Go Tell It on the Mountain*")
    st.write("Published in 1953, *Go Tell It on the Mountain* is a semi-autobiographical novel by James Baldwin that explores themes of race, religion, and identity. The book follows a young Black boy growing up in Harlem, grappling with faith and family struggles. Baldwin's literary contributions continue to shape discussions on race and justice in America.")
    st.divider()
    st.write("Spike Lee's *Do the Right Thing*")
    st.write("Released in 1989, *Do the Right Thing* is a film directed by Spike Lee that examines racial tensions in a Brooklyn neighborhood on the hottest day of the year. The film carries powerful social commentary and distinctive cinematography have cemented it as one of the most influential films in American cinema history.")
    st.divider()
    st.write("Alvin Ailey & the Creation of the Alvin Ailey American Dance Theater")
    st.write("Alvin Ailey, a visionary choreographer, founded the Alvin Ailey American Dance Theater in 1958 to celebrate African American culture through dance. His most famous work, *Revelations*, is a masterpiece that blends modern dance with African American spirituals, gospel, and blues, continuing to inspire dancers worldwide.")
    st.divider()
    st.write("Jean-Michel Basquiat's Rise in Contemporary Art")
    st.write("Jean-Michel Basquiat, an artist who emerged from the 1980s New York graffiti scene, became one of the most celebrated contemporary artists. His neo-expressionist paintings, filled with bold imagery and social critique, addressed themes of race, power, and identity, leaving a lasting impact on the art world.")
    st.divider()
    st.write("Lorraine Hansberry's *A Raisin in the Sun*")
    st.write("In 1959, Lorraine Hansberry made history as the first Black woman to have a play performed on Broadway with *A Raisin in the Sun*. The play tells the story of a Black family in Chicago struggling with poverty and discrimination, tackling themes of dreams, racial identity, and perseverance. It remains a classic in American theater.")
    
    if st.button("Go Back"):
        st.session_state.page = "preferences"

def politics_page():
    change_background_color("#4AE014")
    st.write("Black Excellence in Politics content goes here.")
    st.divider()
    st.write("Thurgood Marshall Becomes the First Black Supreme Court Justice (1959)")
    st.write("Thurgood Marshall made history in 1967 as the first Black Supreme Court Justice, breaking barriers in the highest court of the United States. Before his appointment, Marshall was a trailblazing civil rights lawyer, most famously arguing Brown v. Board of Education (1954), which led to the desegregation of public schools. As a justice, he championed civil rights, racial equality, and justice for marginalized communities, leaving a lasting legacy in American law. His influence continues to shape the fight for equal rights today.")
    st.divider()
    st.write("The Founding of the Congressional Black Caucus (1971)")
    st.write("The Congressional Black Caucus (CBC) was founded in 1971 to amplify the voices of African American lawmakers and advocate for policies addressing racial and social justice. Formed by 13 Black members of Congress, the CBC sought to combat discrimination, push for civil rights legislation, and ensure Black communities had representation at the highest levels of government. Over the decades, the CBC has played a critical role in shaping policies on voting rights, education, healthcare, and criminal justice reform, solidifying its legacy as a powerful force for equity and progress in American politics.")
    st.divider()
    st.write("Carol Moseley Braun the First Black Woman in the U.S. Sena (1983)")
    st.write("Carol Moseley Braun made history in 1992 as the first Black woman elected to the U.S. Senate, breaking barriers in a space long dominated by white men. Representing Illinois, she was also the first African American senator from the Democratic Party. During her tenure, she advocated for civil rights, education reform, and women’s rights, while fighting against discrimination and racial injustice. Her election marked a major milestone in American politics, paving the way for more Black women in leadership roles at the national level.")
    st.divider()
    st.write("John Lewis & the Voting Rights Act (1965)")
    st.write("John Lewis was a key leader in the fight for voting rights, playing a crucial role in the passage of the Voting Rights Act of 1965. As chairman of the Student Nonviolent Coordinating Committee (SNCC), Lewis organized and participated in protests demanding equal voting rights for Black Americans. He was one of the leaders of the Selma to Montgomery march on Bloody Sunday, where he and other activists were brutally attacked by police while crossing the Edmund Pettus Bridge. The violent response to the peaceful protest shocked the nation and pushed Congress to pass the Voting Rights Act, which outlawed racial discrimination in voting. Lewis continued his lifelong fight for justice as a congressman, leaving behind a legacy of courage and activism.")
    st.divider()
    st.write("Shirley Chisholm Becomes the First Black Woman in Congress (1968)")
    st.write("Shirley Chisholm made history in 1968 as the first Black woman elected to the U.S. Congress, representing New York’s 12th congressional district. A fearless advocate for racial and gender equality, she broke barriers in a political system that often excluded Black women. Chisholm championed policies supporting education, healthcare, and workers’ rights, earning her the nickname “Fighting Shirley.” In 1972, she took her trailblazing efforts even further by becoming the first Black woman to run for President of the United States, paving the way for future generations of Black women in politics.")
    if st.button("Go Back"):
        st.session_state.page = "preferences"



def health_page():
    st.write("Black Excellence in Health")
    st.divider()
    st.write("Dr. Charles Drew & the Blood Bank Revolution")
    st.write("Dr. Charles Drew revolutionized the field of blood transfusion by developing improved techniques for blood storage and the large-scale blood bank system. His work led to the creation of the American Red Cross blood bank, saving countless lives during World War II and beyond. Despite facing racial discrimination, his pioneering research laid the foundation for modern blood donation practices.")
    st.divider()
    st.write("Dr. Daniel Hale Williams Performs the First Successful Open-Heart Surgery")
    st.write("In 1893, Dr. Daniel Hale Williams became the first surgeon to successfully perform an open-heart surgery. He operated on a man who had been stabbed in the chest, managing to repair the wound without modern surgical tools or antibiotics. Williams later founded Provident Hospital in Chicago, the first Black-owned and operated hospital in the United States, advancing opportunities for Black medical professionals.")
    st.divider()
    st.write("The Black Panther Party's Free Health Clinics")
    st.write("The Black Panther Party established free community health clinics across the United States in the 1960s and 1970s, providing essential medical services to underserved Black communities. These clinics offered screenings for conditions like sickle cell anemia and provided general healthcare, setting a precedent for grassroots health activism and community care.")
    st.divider()
    st.write("The Establishment of Meharry Medical College")
    st.write("Founded in 1876, Meharry Medical College in Nashville, Tennessee, became one of the first medical schools dedicated to training Black physicians. The institution played a crucial role in addressing racial disparities in healthcare and continues to produce top-tier medical professionals who serve communities in need.")
    st.divider()
    st.write("Mary Eliza Mahoney Becomes the First Black Professional Nurse")
    st.write("In 1879, Mary Eliza Mahoney became the first African American to earn a professional nursing license in the United States. Her achievements broke racial barriers in healthcare, and she later co-founded the National Association of Colored Graduate Nurses, advocating for diversity and equity in the medical field.")

    if st.button("Go Back"):
        st.session_state.page = "preferences"

def sports_page():
    change_background_color("#4AE014")
    st.write("Black Excellence Intro Message in Sports content goes here.")
    st.divider()
    st.write("Jackie Robinson Breaks the MLB Color Barrier (1947)")
    st.write("Jackie Robinson made history when he became the first African American to play Major League Baseball with the Brooklyn Dodgers, breaking the league’s long-standing color barrier. Facing intense racism from fans, teammates, and opponents, Robinson remained resilient, letting his talent and discipline speak for itself. His courage changed baseball forever, paving the way for Black athletes in professional sports and accelerating the Civil Rights Movement by challenging segregation in one of America’s most beloved pastimes.")
    st.divider()
    st.write("LeBron James Opens the I PROMISE School (2018)")
    st.write("LeBron James is not only one of the greatest basketball players of all time, but also a champion for education and social change. In 2018, he opened the I PROMISE School in Akron, Ohio, dedicated to providing free, high-quality education and support to at-risk children. The school offers free tuition, meals, bicycles, and guaranteed college scholarships for qualifying students. LeBron’s initiative extends beyond basketball, proving that athletes can be powerful forces for community upliftment and generational change.")
    st.divider()
    st.write("Kareem Abdul-Jabbar Becomes the NBA’s All-Time Leading Scorer (1984)")
    st.write("Kareem Abdul-Jabbar, known for his unstoppable skyhook shot, made history in 1984 by surpassing Wilt Chamberlain to become the NBA’s all-time leading scorer, a record that stood for nearly 40 years. Beyond his dominance on the court, Abdul-Jabbar has been a vocal advocate for civil rights, education, and social justice, using his platform to fight for equality. His influence as both an athlete and activist cements his legacy as one of the most important figures in sports history.")
    st.divider()
    st.write("Wilma Rudolph Becomes the First American Woman to Win Three Gold Medals in One Olympics (1960)")
    st.write("Wilma Rudolph overcame childhood polio, racial barriers, and gender discrimination to become one of the greatest track and field athletes of all time. At the 1960 Rome Olympics, she became the first American woman to win three gold medals in a single Olympic Games, dominating the 100m, 200m, and 4x100m relay. Her achievements made her a global icon, inspiring both women and African Americans to pursue their dreams despite obstacles. She later used her fame to advocate for racial and gender equality in sports and society.")
    st.divider()
    st.write("Muhammad Ali Becomes Heavyweight Champion (1964)")
    st.write("In 1964, a young and confident Muhammad Ali shocked the world by defeating Sonny Liston to become the youngest heavyweight boxing champion at just 22 years old. Ali’s charisma, bold personality, and unparalleled skill made him a global sensation, but his legacy extended far beyond the ring. A fierce advocate for civil rights, he refused to be drafted into the Vietnam War, famously stating, “I ain’t got no quarrel with them Viet Cong.” His decision cost him his title and nearly ended his career, but he stood firm in his beliefs. Ali’s combination of athletic dominance and social activism made him one of the most influential sports figures in history.")
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
