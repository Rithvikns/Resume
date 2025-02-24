import streamlit as st
from langchain.llms import HuggingFaceHub
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import google.generativeai as genai
# Set Hugging Face API Key (Replace with your key)

GOOGLE_API_KEY = "AIzaSyDHQ4oxBF3eYLy-vNKbA-U8AwhB2Eivm_E"
genai.configure(api_key=GOOGLE_API_KEY)


llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY, temperature=0.7)
# Set page layout
st.set_page_config(layout="wide")  # Wide mode for better spacing

# Title
st.title("Rithvik Narayana Swamy")

# Left Sidebar - Profile Sections
st.sidebar.header("Profile Sections")
section = st.sidebar.selectbox(
    "Pick a Subsection",
    ("Personal Information", "Education", "Work Experience", "Projects", "Skills", "Achievements", "Languages", "Hobby")
)

# Layout with 3 Columns: Left (Sidebar), Middle (Main), Right (Q&A)
col1, col2, col3 = st.columns([2, 4, 2])  # Adjust column widths

# Middle Column: Display Selected Profile Section
with col2:
    st.subheader(section)
    
    section_data = {
        "Personal Information": "**Name:** Rithvik Narayana Swamy\n\n**Email:** rithvik@example.com\n\n**Phone:** +1234567890",
        "Education": "**Degree:** B.Tech in Computer Science - XYZ University",
        "Work Experience": "**Position:** Software Engineer at ABC Corp",
        "Projects": "1. AI Chatbot\n2. Web Scraper\n3. Portfolio Website",
        "Skills": "Python, JavaScript, Machine Learning, Web Development",
        "Achievements": "Won Hackathon 2023, Published Research Paper on AI",
        "Languages": "English, Spanish, French",
        "Hobby": "Photography, Chess, Blogging"
    }
    
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
