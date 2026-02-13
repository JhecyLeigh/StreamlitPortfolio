import streamlit as st


def show_home():
    """Display the Home page"""
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(
        "images/profile.png",
        caption="Jhecy Leigh T. Mando\n22-3389-294",
        width=250
    )

    
    with col2:
        st.markdown("<h3 style='color: #667eea; margin-top: 0;'>Welcome! 👋</h3>", unsafe_allow_html=True)
        st.markdown("""
        I'm **Jhecy Leigh T. Mando**, a BSIT-3 student at **Cebu Institute of Technology - University**.
        
        I'm passionate about **Web Design** and **Software Development**. This portfolio showcases my journey, skills, and projects in the tech world.
        
        **My Interests:**
        - 💻 Web Development
        - 🎨 User Interface Design
        - 📐 Wireframing and Prototyping
        """)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>📚 Passion</h3>
            <p>Love for reading books, watching movies, cooking, exploring new places</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>👨‍💻 Skills</h3>
            <p>Web Development (HTML, CSS, React), Programming (Python, JavaScript), UI/UX Design, and Wireframing and Prototyping</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h3>🎯 Goals</h3>
            <p>To be a skilled web designer or developer, creating user-friendly websites and innovative solutions that make a real-world impact.</p>
        </div>
        """, unsafe_allow_html=True)
