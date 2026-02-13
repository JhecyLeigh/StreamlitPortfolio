import streamlit as st
from styles import load_styles
from home import show_home
from about_me import show_about_me
from projects import show_projects
from contact import show_contact

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="My Portfolio",
    page_icon=":sparkles:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom styles
load_styles()


# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Create compact navbar at the top
navbar_col1, navbar_col2, navbar_col3, navbar_col4, navbar_col5 = st.columns([1, 1, 1, 1, 1])

with navbar_col1:
    st.markdown("<div style='display: flex; align-items: center; height: 100%; color: black; font-size: 1.5rem; font-weight: bold;'>🌟 My Portfolio</div>", unsafe_allow_html=True)

with navbar_col2:
    if st.button("Home", use_container_width=True, key="btn_home"):
        st.session_state.page = "Home"

with navbar_col3:
    if st.button("About", use_container_width=True, key="btn_about"):
        st.session_state.page = "About Me"

with navbar_col4:
    if st.button("Projects", use_container_width=True, key="btn_portfolio"):
        st.session_state.page = "Portfolio"

with navbar_col5:
    if st.button("Contact", use_container_width=True, key="btn_contact"):
        st.session_state.page = "Contact"

st.markdown("---")

menu = st.session_state.page

# Display pages based on navigation
if menu == "Home":
    show_home()

elif menu == "About Me":
    show_about_me()

elif menu == "Portfolio":
    show_projects()

elif menu == "Contact":
    show_contact()
