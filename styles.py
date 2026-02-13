import streamlit as st

def load_styles():
    """Load and apply custom CSS styles for the portfolio app"""
    st.markdown("""
    <style>
    /* Hide Streamlit menu */
    #MainMenu {visibility: hidden;}
    .stAppDeployButton {display: none;}
    
    .navbar {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0.3rem 2rem;
        margin: -1.5rem -1.5rem 0.5rem -1.5rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .navbar-title {
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        margin: 0;
        display: flex;
        align-items: center;
    }
    .card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 1rem;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .section-title {
        color: #667eea;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .project-card {
        background: white;
        border-radius: 1rem;
        padding: 1.5rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
    }
    </style>
    """, unsafe_allow_html=True)
