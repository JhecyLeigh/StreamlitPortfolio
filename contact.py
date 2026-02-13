import streamlit as st


def show_contact():
    """Display the Contact page"""
    st.markdown("<h3 style='color: #667eea; margin-top: 0;'>Get In Touch 📧</h3>", unsafe_allow_html=True)
    st.markdown("Don’t be a stranger! Let’s make the internet a little friendlier—start by saying hi through the links below.")
    st.markdown("---")

    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>📍 Contact Information</h3>
            <p><strong>School Email:</strong> jhecyleigh.mando@cit.edu</p>
            <p><strong>Personal Email:</strong> jhecyleightolibasmando@gmail.com</p>
            <p><strong>Location:</strong> Duljo Fatima, Cebu City, Philippines</p>
            <p><strong>Phone:</strong> +63 968 456 6417</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>🔗 Connect With Me</h3>
            <p>
                <a href="https://github.com/JhecyLeigh" target="_blank">
                    <strong>🖤 GitHub</strong>
                </a>
            </p>
            <p>
                <a href="https://www.facebook.com/jhecy.mando" target="_blank">
                    <strong>ⓕ Facebook</strong>
                </a>
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>📝 Send me a Message</h3>
        </div>
        """, unsafe_allow_html=True)
        
        name = st.text_input("Your Name", placeholder="Enter your full name")
        email = st.text_input("Your Email", placeholder="your.email@example.com")
        subject = st.text_input("Subject", placeholder="What's this about?")
        message = st.text_area("Your Message", placeholder="Tell me something interesting...", height=120)
        
        col_button1, col_button2 = st.columns(2)
        
        with col_button1:
            if st.button("📤 Send Message", use_container_width=True):
                if name and email and subject and message:
                    st.success(f"✅ Thank you {name}! Your message has been sent successfully. I'll get back to you soon!")
                else:
                    st.error("❌ Please fill in all fields before submitting.")
        
        with col_button2:
            if st.button("🔄 Clear Form", use_container_width=True):
                st.rerun()
