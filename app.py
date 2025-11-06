import streamlit as st
import requests
from streamlit_lottie import st_lottie

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Marouane Laamiri | My Portfolio",
    page_icon="/home/malaamir/Downloads/mali.svg",
    layout="wide",
)

# --- HELPER FUNCTION ---
# This function loads a Lottie animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- 1. HEADER SECTION ---
with st.container():
    col1, col2 = st.columns([0.6, 0.4])

    with col1:
        st.title("Hi, I'm Marouane Laamiri ")
        st.subheader("A 42 Network Student | Aspiring AI developer")
        st.write(
            "I'm learning to build web applications with Python, and other programming languages while integrating AI concepts into my projects. "
            "This portfolio is my first project using Streamlit!"
        )
        
        # --- SOCIALS ---
        st.header("🌐 Socials:")
        st.markdown(
            """
            [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marouane-laamiri-0197a317a/) 
            [![Medium](https://img.shields.io/badge/Medium-12100E?logo=medium&logoColor=white)](https://medium.com/@laamirimarouane8) 
            [![email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:laamirimarouane8@gmail.com)
            """
        )

    with col2:
        # --- LOTTIE ANIMATION ---
        # We load a Lottie animation from a URL. 
        # You can find more at https://lottiefiles.com/
        lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
        
        if lottie_coding:
            st_lottie(
                lottie_coding,
                speed=6,
                reverse=False,
                loop=True,
                quality="high", # "low", "medium", "high"
                height=300,
                width=None,
                key="coding_animation",
            )
        else:
            st.warning("Could not load Lottie animation.")


st.divider() # Adds a horizontal line

# --- 2. ABOUT ME SECTION ---
st.header("About Me")
st.write(
    """
    A computer science professional with acquired experience in computer hardware and OS maintenance, I have developed a strong background in computers and server setups as an IT technician within various local associations, and schools.
	Furthermore, I am a computer technician who is dedicated to continually improving my skills and growing in the programming field. During my university studies in Ukraine, I developed a keen interest in programming and cloud computing, and I have pursued numerous training and certification programs, including AWS Certified Cloud Computing.
	I would describe myself as a problem solver who is agile and results-oriented. I believe that my skills make me a valuable asset to the IT industry.
    
    When I'm not coding, Im asleep or playing video games.
    """
)

st.divider()

# --- 3. PROJECTS SECTION ---
st.header("My Projects")
st.write("Here are a few projects I've been working on. You can find more on my GitHub.")

# --- Project 1 ---
st.subheader("Cub3D Fake 3D Game")
st.write(
    "Cub3D is a simple 3D game engine project inspired by the classic game Wolfenstein 3D. "
	"It is developed using the C programming language and utilizes the MiniLibX graphics library for rendering. "
	"The project focuses on implementing raycasting techniques to create a 3D environment from a 2D map, allowing players to navigate through a maze-like structure. "
	"Cub3D showcases fundamental concepts of computer graphics, game development, and low-level programming."
)
st.write("[View on GitHub](https://github.com/Marouanelaamiri/cub3D)") #<-- Update this link


st.divider()

# --- 4. CONTACT ME SECTION ---
st.header("Get In Touch!")
st.write("Have a question or want to work together? Send me a message!")

# We use st.form to create a form that batches user inputs
with st.form(key="contact_form"):
    # Input fields for the form
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    
    # Submit button
    # The code inside the `if` block will only run when the button is clicked
    submit_button = st.form_submit_button(label="Send Message")
    
    if submit_button:
        # This is where you would add code to *do* something with the form.
        # For now, we'll just display a success message.
        
        # A more advanced version could use `smtplib` to send an email
        # or `st.secrets` to write to a Google Sheet.
        
        st.success(f"Hi {name}, your message was sent successfully! (This is a demo)")
        st.info(f"Email to: {email} \n\nMessage: \n\n{message}")