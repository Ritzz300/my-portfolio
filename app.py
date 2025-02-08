import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="My Portfolio", layout="wide")

# Custom CSS for Navigation Bar
st.markdown(
    """
    <style>
    .topnav {
        background-color: #222;
        overflow: hidden;
        text-align: center;
        padding: 15px;
        border-radius: 10px;
    }
    .topnav button {
        background-color: #444;
        border: none;
        color: white;
        padding: 14px 20px;
        margin: 5px;
        cursor: pointer;
        font-size: 16px;
        font-weight: bold;
        border-radius: 5px;
    }
    .topnav button:hover {
        background-color: #666;
    }
    .profile-pic img {
        border-radius: 50%;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create Navigation Bar
col1, col2, col3, col4, col5, col6 = st.columns(6)
if col1.button("🏠 Home"):
    st.session_state.page = "Home"
if col2.button("📚 Education"):
    st.session_state.page = "Education"
if col3.button("🚀 Projects"):
    st.session_state.page = "Projects"
if col4.button("💻 Tech Stack"):
    st.session_state.page = "Tech Stack"
if col5.button("🎨 Hobbies"):
    st.session_state.page = "Hobbies"
if col6.button("ℹ️ More Info"):
    st.session_state.page = "More Info"

# Initialize session state if not set
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Home Page with Profile Picture in Top-Right Corner
if st.session_state.page == "Home":
    col1, col2 = st.columns([3, 1])  # 3:1 ratio for text and profile image
    with col1:
        st.title("Hi, I'm Priya 👋")
        st.markdown(
            "### Welcome to my professional portfolio! 🚀\n"
            "Explore my education, projects, skills, and hobbies by using the navigation buttons above."
        )
    with col2:
        st.markdown("<div class='profile-pic'>", unsafe_allow_html=True)
        st.image("https://media-hosting.imagekit.io//14cdf2c3c97f4f91/women-ico.webp?Expires=1833535347&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=bTm05Upsv7UXS~GqU-qwiypdkd8e415nDW8hmxS4~--B6nIbggDpVou2W9xdahfCNUYd5Wc1P36wOMjEtalUVt-LG2ktDuT8AmdmxR1vMZr8d-e9sjX28I1O-KkgZvomDwR9RLapZ5YmkJRa8qVW4kvYEAs2QSgxvSNxUGBgdZcZGCipncWOZECnR6LNslwbWYeMIPVtPlTubDlsYbQgOI9jo~Ph0oIjZqhY~fFIF8FXOLjAvCapxis0V0AFoDOJmG6aSMBWk8PkkxWUTxoOXZ1hLHT2QCOpz~lI~7mK~hv1rZGt-xCJyAtmhog2e0ZKph9TtHHwZIoR6XL6m5JLfQ__", width=180)
        st.markdown("</div>", unsafe_allow_html=True)

# Education Page
elif st.session_state.page == "Education":
    st.title("📚 Education")
    data = {
        "Grade": ["10th", "12th", "Graduation"],
        "School/College": ["PSBB Matric Higher Secondary School", "PSBB Matric Higher Secondary School", "Chennai Institute of Technology"],
        "Percentage (%)": [93.2, 85, 91.6],
    }
    df = pd.DataFrame(data)
    st.table(df)
    fig = px.bar(df, x="Grade", y="Percentage (%)", title="Academic Performance", color="Grade")
    st.plotly_chart(fig, use_container_width=True)

# Projects Page
elif st.session_state.page == "Projects":
    st.title("🚀 Projects")
    tab1, tab2, tab3 = st.tabs(["Project 1", "Project 2", "Project 3"])
    with tab1:
        st.subheader("AWS Glue ETL Pipeline")
        st.write("Developed an ETL pipeline using AWS Glue, PySpark, and Snowflake.")
    with tab2:
        st.subheader("PySpark Data Processing")
        st.write("Optimized big data processing with PySpark and AWS Glue.")
    with tab3:
        st.subheader("Snowflake Data Warehouse")
        st.write("Designed a scalable data warehouse in Snowflake for analytics.")

# Tech Stack Page
elif st.session_state.page == "Tech Stack":
    st.title("💻 Tech Stack")
    skills = {"Skill": ["AWS", "PySpark", "SQL", "Snowflake", "Python"], "Rating": [7, 6, 8, 5, 6]}
    df_skills = pd.DataFrame(skills)
    fig_skills = px.scatter(df_skills, x="Rating", y="Skill", size="Rating", color="Skill", title="Tech Proficiency")
    st.plotly_chart(fig_skills, use_container_width=True)

# Hobbies Page
elif st.session_state.page == "Hobbies":
    st.title("🎨 Hobbies")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://media-hosting.imagekit.io//10147d832b0d4499/photography.jfif?Expires=1833526315&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=B0fi~nAaRBpeqKbADH5CbgM0nlb7ZjBNzpRWLZ7eitmSY9xkHkEufcmkos8Nj-UhQlQ1ZQwc56ad4MaCrgelMPXSvUCNBoSZMxZsycpPstmNa3vfp7yspvT7rnRQKLjSFASBUtiZ3o7FEVulCCAOGXyHLI5zO6X~nrAauSEmSRwoQ8PvUMJA8tTAYL8dpUpSATXODtRI-P0hZHI3O9JcvFbuYDRt8XAG3t0N~h0QLzfMr83kfJot2r0xCFTxOBhV8is~O4chCsL6XSOMKWi34P3VmVKawf9O8YJ07i248v8o5slOiX~ToXilqox2HbjvFgqWfEcYn6KuIPtrd0dSQA__", caption="Photography", use_container_width=True)
    with col2:
        st.image("https://media-hosting.imagekit.io//df5e85dae3e04f6b/travelling.jfif?Expires=1833526590&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=Sas~pLu~mmxW4CQezOytaR71yICSmZ7zcoO-fcNSAR69BvonwN45Cvamou~Ehx0agY5MUxIJc75JhaVAhNt7BByBV5Y45foYcW7LjmqrJ4L1ds2ezl-z3wv9yOFGsICdA0wiz9WQgR-lMzqkNcRu8yCjFw60EbWqUH99aFAqPb1oQAQUzS-Obl68pZBycf5EjL-jSpBsBI3QPkJZ2WVdC8sNnknsMDEN9x-JbUfdfnofXcYl0QY34sWKg53WpBw-kupxAIbGHereyDsAcrbYhkqwHZjHnr0oZDQewHXjj9Rbj3WWYXfWnOLA6xef23pRHPGwJxqF4MZeCRfU4-ifNQ__", caption="Traveling", use_container_width=True)
    with col3:
        st.image("https://media-hosting.imagekit.io//abdc8a2a93bf42ad/OIP.jfif?Expires=1833613076&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=gX591vKHTKAucwY9cmIfRGYBRfP0f0XtmT4FdElB0YBv5NWYTyn4LBxtd9E34tbmsXsY7nbhF~eKKmPJtR8~GuBHCZ2Y3rvVzs7smMlmJ8n-JDaYnb6DEP~dkAuf-n2kMx4fHA86Dv6wuXMTCLtRwIUiQ-sMSWA-pydtqGsHYvXRV1vCBhON9o5eP27Du4lpSwo2wQPhedXT5AU3hmIhQNKLnT5xRA01dqVRXyFG-Q2RMMlRlLhgNL0n1TcG9LDOttr31hJqSo2nsM13Qpw4VeDV5ZYuY7LO-Jp41ZskDV0gHxDtwz63~U6JSXfbIwmC0-eEx~S09qqtc21~In8EtA__", caption="Reading", use_container_width=True)

# More Info Page
elif st.session_state.page == "More Info":
    st.title("ℹ️ More Info")
    st.write("Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/priya-a-44b9b2206/) or [GitHub](https://github.com/Ritzz30).")
