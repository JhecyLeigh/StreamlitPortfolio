import streamlit as st


def show_about_me():
    """Display the About Me page"""
    st.markdown("<h3 style='color: #667eea; margin-top: 0;'>About Me 👤</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(
            r"C:\Users\jhecy\OneDrive\Pictures\Screenshots\pic.png",
            use_container_width=True
        )
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>Personal Information</h3>
            <ul>
                <li><strong>Name:</strong> Jhecy Leigh T. Mando</li>
                <li><strong>Education:</strong> Bachelor of Science in Information Technology at Cebu Institute of Technology - University</li>
                <li><strong>Location:</strong> Duljo Fatima, Cebu City, Philippines</li>
                <li><strong>Passion:</strong> Web Design & Software Development</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<h3 style='color: #667eea;'>My Journey 📖</h3>", unsafe_allow_html=True)
    st.markdown("""
    When I first saw this course on my schedule, I wasn’t thrilled. It wasn’t my first choice, and I spent days overthinking whether I was on the right path. I even considered switching to another program, wondering if I’d be happier elsewhere. But then, something unexpected happened. I started attending classes, tackling projects, and slowly—but surely—I began to enjoy it. 
    
    The challenges that once felt overwhelming became opportunities to learn, and those late nights figuring things out turned into small victories I could be proud of. I learned that it’s okay to question your path, that growth often comes from discomfort, and that sometimes the journeys we resist the most turn out to be the ones we love. 
    
    What started as doubt has become excitement. 
    
    I’m curious, I’m eager, and I’m ready to embrace every lesson, challenge, and opportunity this journey in tech will bring my way.
    """)
    
    st.markdown("---")
    st.markdown("<h3 style='color: #667eea;'>Skills & Expertise 💡</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Programming Languages:**
        - Python 🐍
        - JavaScript
        - HTML & CSS
        - SQL
        """)
    
    col2.markdown("""
        **Tools & Technologies:**
        - Streamlit
        - React
        - Git & GitHub
        - VS Code
        - HTML, CSS & JavaScript
        - SQL
        - Python
        - Figma / Canva 
    """)

