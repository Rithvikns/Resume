# Explanation of the Streamlit App with LangChain and Google Generative AI

## Overview
This Python script builds a Streamlit web application that displays profile information and allows users to ask AI-generated questions using Google's Generative AI (Gemini-Pro). The application is divided into three main sections: a sidebar for profile selection, a main content area for displaying details, and a right column for AI-powered Q&A.

---

## Libraries Used
- `streamlit`: For creating an interactive web application.
- `langchain.llms.HuggingFaceHub`: (Imported but not used in the script)
- `langchain_google_genai.ChatGoogleGenerativeAI`: For integrating Google’s Generative AI with LangChain.
- `langchain.prompts.PromptTemplate`: Used to structure AI prompts.
- `google.generativeai`: Official library for accessing Google’s AI models.

---

## API Key Configuration
```python
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)
```
- The Google API key is required to authenticate and interact with the Gemini-Pro model.
- The `genai.configure()` function initializes the API connection.

---

## Initializing the AI Model
```python
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY, temperature=0.7)
```
- `ChatGoogleGenerativeAI` is used to connect to Gemini-Pro.
- The `temperature=0.7` setting controls the randomness of AI responses.

---

## Streamlit Page Layout
```python
st.set_page_config(layout="wide")
st.title("Rithvik Narayana Swamy")
```
- `st.set_page_config(layout="wide")`: Enables a wide-screen layout for better UI presentation.
- `st.title()`: Sets the main title of the web app.

---

## Sidebar for Profile Sections
```python
st.sidebar.header("Profile Sections")
section = st.sidebar.selectbox("Pick a Subsection", (...))
```
- The sidebar contains a dropdown menu for selecting profile sections.
- Sections include "Personal Information," "Education," "Skills," etc.

---

## Displaying Profile Information
```python
section_data = {
    "Personal Information": "**Name:** Rithvik Narayana Swamy...",
    "Education": "**Degree:** B.Tech in Computer Science - XYZ University",
    "Work Experience": "**Position:** Software Engineer at ABC Corp",
    ...
}

st.write(section_data.get(section, "No data available"))
```
- A dictionary stores predefined profile data.
- The selected section’s information is displayed using `st.write()`.

---

## AI-Powered Q&A Section
```python
user_question = st.text_input("Enter your question:")
if user_question:
    with st.spinner("Thinking..."):
        prompt_template = PromptTemplate.from_template("Answer the following question as accurately as possible:\n\n{question}")
        prompt = prompt_template.format(question=user_question)
        response = llm.invoke(prompt)
        st.write("**Answer:**", response.content)
```
- Users can type a question in `st.text_input()`.
- The question is formatted using `PromptTemplate` and sent to the AI model.
- The AI-generated response is displayed on the page.

---

## Conclusion
This Streamlit app effectively combines AI with a user-friendly interface to showcase profile information and provide an interactive Q&A experience. The integration of Google Generative AI allows for dynamic responses to user queries.

