import streamlit as st

def show_projects():
    """Display the Projects/Portfolio page"""

    # -------------------- First row: Web Applications --------------------
    st.markdown("<h3 style='color: #667eea; margin-top: 0;'>Web Applications 🌐</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "images/Screenshot 2026-02-07 192335.png",
            width=600
        )
        st.markdown("""
        <p><strong>Project:</strong> PAWthway - Veterinary Clinic Management System</p>
        <p><strong>Description:</strong> PAWthway streamlines veterinary care in Cebu by digitizing key processes. Features include online appointment booking, automated inventory management, centralized client and pet records, and an interactive map of nearby veterinary clinics.</p>
        """, unsafe_allow_html=True)

    with col2:
        st.image(
            "images/Screenshot 2026-02-13 173945.png",
            width=600
        )
        st.markdown("""
        <p><strong>Project:</strong> WildMart - Campus Marketplace</p>
        <p><strong>Description:</strong> WildMart is a campus marketplace for CIT-U students to buy, sell, and trade items within the community, making transactions faster, safer, and more accessible.</p>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # -------------------- Second row: Brochures --------------------
    st.markdown("<h3 style='color: #667eea; margin-top: 0;'>Brochures 🚀</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "images/1.png",
            width=600
        )
        st.markdown("""
        <p><strong>Project:</strong> Limasawa Island Brochure</p>
        <p><strong>Description:</strong> Created an informative and visually appealing brochure about Limasawa Island, highlighting its history, attractions, and culture.</p>
        <p><strong>Tools:</strong> Canva</p>
        """, unsafe_allow_html=True)

    with col2:
        st.image(
            "images/coffee.png",
            width=600
        )
        st.markdown(""" 
        <p><strong>Project:</strong> Everyday Coffee Brochure</p>
        <p><strong>Description:</strong> Created a brochure for Everyday Coffee, highlighting its passion for quality coffee, community, and daily moments of joy.</p>
        <p><strong>Tools:</strong> Canva</p>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # -------------------- Third row: Logo Projects --------------------
    st.markdown("<h3 style='color: #667eea; margin-top: 0;'>Logo Projects 🎨</h3>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image(
            "images/Everyday.png",
            width=200
        )

    with col2:
        st.image(
            "images/Bakery.png",
            width=200
        )

    with col3:
        st.image(
            "images/EverWrite.png",
            width=200
        )

    with col4:
        st.image(
             "images/pawthway.png",
            width=200
        )
        st.markdown("---")


# -------------------- Fourth row: Other Projects --------------------
    st.markdown("<h3 style='color: #667eea; margin-top: 0;'>Other Projects 🎨</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.image(
        "images/Homescreen.png",
        width=600
        )
        st.markdown("""
            <p><strong>Description:</strong> Designed a clean and visually engaging laptop home screen layout, focusing on usability and aesthetic appeal.</p>
            """, unsafe_allow_html=True)
    with col2:
        st.image(
        "images/Vector.png",
        width=600
        )
        st.markdown("""
            <p><strong>Description:</strong> Designed a clean and visually engaging vector illustration for a school activity.</p>
            """, unsafe_allow_html=True)


    st.markdown("---")
    st.markdown("<h3 style='color: #667eea;'>Share Your Project 📁</h3>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload your resume or project documentation (PDF, TXT)", type=["pdf", "txt"])
    if uploaded_file is not None:
        st.success(f"✅ File uploaded successfully: {uploaded_file.name}")
