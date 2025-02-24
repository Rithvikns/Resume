import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import google.generativeai as genai
# Set Hugging Face API Key (Replace with your key)

GOOGLE_API_KEY = "AIzaSyDHQ4oxBF3eYLy-vNKbA-U8AwhB2Eivm_E"
genai.configure(api_key=GOOGLE_API_KEY)


llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY, temperature=0.7)
# Set page layout
st.set_page_config(layout="wide")  # Wide mode for better spacing

st.markdown(
    "<h1 style='text-align: center; color: #3366cc;'>Rithvik Narayana Swamy</h1>", 
    unsafe_allow_html=True
)

# Left Sidebar - Profile Sections
st.sidebar.header("Profile Sections")
section = st.sidebar.selectbox(
    "Pick a Subsection",
    ("Personal Information", "Education", "Work Experience", "Projects", "Skills", "Achievements", "Languages", "Hobby")
)

# Layout with 3 Columns: Left (Sidebar), Middle (Main), Right (Empty)
col1, col2, col3 = st.columns([2, 4, 2])  # Adjust column widths

# Middle Column: Display Selected Profile Section
with col2:
    st.markdown(f"<h2 style='text-align: center; color: #444;'>{section}</h2>", unsafe_allow_html=True)

    # Profile Section Data
    section_data = {
        "Personal Information": f"""
            <div style="text-align: center;">
                <img src="profile.jpg" alt="Profile Image" width="150" style="border-radius: 50%;"><br><br>
                <b>Name:</b> Rithvik Narayana Swamy<br>
                <b>Email:</b> rithviknswamy@gmail.com<br>
                <b>Phone:</b> +49 1577 8463738
            </div>
        """,
        "Education": """
            <b>Degree:</b> M.S in Information Technology - University Of Stuttgart<br>
            <b>Grade:</b> 2.0 GPA<br><br>
            <b>Description:</b><br>
            I am currently pursuing my Master of Science in Information Technology (Infotech) at the University of Stuttgart, where I am deepening my knowledge and skills in advanced IT concepts, machine learning, DevOps practices, and their practical applications.<br><br>
            <b>Skills:</b> Docker, Cloud Computing, EDA, LSTM, C++, Embedded Systems, Machine Learning, Python, AI, VHDL, Kubernetes.<br><br>
            <b>Previous Degree:</b> B.Tech
        """,
        "Work Experience": """
            <b>Position:</b> Software Engineer at ABC Corp<br>
            <b>Responsibilities:</b><br>
            - Developed AI-driven applications.<br>
            - Managed cloud infrastructure.<br>
            - Automated DevOps pipelines.
        """,
        "Projects": """
            <ul>
                <li>🚀 <b>AI Chatbot</b> - NLP-based virtual assistant</li>
                <li>🔍 <b>Web Scraper</b> - Automated data extraction</li>
                <li>🌐 <b>Portfolio Website</b> - Personal branding</li>
            </ul>
        """,
        "Skills": """
            <b>Technical Skills:</b><br>
            ✅ Python, JavaScript, C++<br>
            ✅ Machine Learning, Deep Learning, NLP<br>
            ✅ Cloud Computing (AWS, Azure, GCP)<br>
            ✅ DevOps (Docker, Kubernetes, CI/CD)
        """,
        "Achievements": """
            🏆 Won <b>Hackathon 2023</b><br>
            📜 Published <b>Research Paper on AI</b><br>
            💡 Built a <b>Machine Learning Model</b> with 98% accuracy
        """,
        "Languages": """
            🗣️ English - Fluent<br>
            🗣️ German - Intermediate<br>
            🗣️ French - Basic
        """,
        "Hobby": """
            📷 Photography<br>
            ♟️ Chess<br>
            ✍️ Blogging
        """
    }

    # Display section content
    st.markdown(section_data[section], unsafe_allow_html=True)
    
    st.write(section_data.get(section, "No data available"))



# Right Column: Q&A Box
with col3:
    st.markdown(
        """
        <div style="background-color: #f4f4f4; padding: 20px; border-radius: 10px;">
            <h3 style="text-align: center;">Ask Me Anything</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    user_question = st.text_input("Enter your question:")
    
    if user_question:
        with st.spinner("Thinking..."):
            # Define prompt template
            prompt_template = PromptTemplate.from_template("Answer the following question as accurately as possible:\n\n{question}")
            prompt = prompt_template.format(question=user_question)

            # Generate response
            response = llm.invoke(prompt)
            st.write("**Answer:**", response.content)
