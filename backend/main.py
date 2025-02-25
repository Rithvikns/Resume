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

# Title (Centered)
st.markdown("<h2 style='text-align: center; color: #444;'>Rithvik Narayana Swamy</h2>", unsafe_allow_html=True)

# Sidebar - Profile Sections
st.sidebar.header("Profile Sections")
section = st.sidebar.selectbox(
    "Pick a Subsection",
    ("Personal Information", "Education", "Work Experience", "Projects", "Skills", "Achievements", "Languages", "Hobby")
)

# Layout with Columns
col1, col2, col3 = st.columns([2, 4, 2])  # Center the content

with col2:
    st.subheader(section)

    # Section Data
    section_data = {
        "Personal Information": lambda: (
            st.image("profile.jpg", width=150, caption="Profile Image"),
            st.markdown("### Name: Rithvik Narayana Swamy"),
            st.markdown("📧 **Email:** rithviknswamy@gmail.com"),
            st.markdown("📞 **Phone:** +49 1577 8463738"),
        ),

        "Education": lambda: st.markdown("""
            ### 🎓 Education  
            **M.S in Information Technology - University Of Stuttgart (Nov 2022 - April 2025) **  
            📊 **Grade:** 2.0 GPA  
            🔬 ** Discription** I am currently pursuing my Master of Science in Information Technology (Infotech) at the University of Stuttgart, where I am deepening my knowledge and skills in advanced IT concepts, machine learning, DevOps practices, and their practical applications.<br><br>                            
            🏫 **Skills:** Docker, Cloud Computing, LSTM, C++, Embedded Systems, AI, Kubernetes  
            
            **B.Tech - Dayananda Sagar College of Engineering (Jun 2017 - Aug 2021)**  
            📊 **Grade:** 9.05 CGPA  
            🔬 ** Discription** I completed my Bachelor of Engineering (BE) in Electronics and Communication Engineering (ECE) from Dayananda Sagar College of Engineering, This program provided me with a strong foundation in both theoretical knowledge and practical skills, preparing me for a career in the ever-evolving field.<br><br>                            
            🏫 **Skills:** Digital Electronics, Cloud Computing, FPGA, VHDL, Neural Networks  
        """, unsafe_allow_html=True),

        "Work Experience": lambda: st.markdown("""
            ### 💼 Work Experience  
            **Master Thesis - University of Stuttgart (Oct 2024 - April 2025)**  
            - The work deep dives into various causality mining approaches, including both linear and non-linear methods, and concludes with a discussion of root cause analysis techniques.
            - The work is particularly focused on extending the dependency graph using topology and temporal information.
            - Next applying a specific causal mining method GNN to generate a causal graph , which is further sampled to form sub graphs. using this sub graphs and root cause analysis method a ranking of root causes would be displayed in the UI 
            - ** Skills **: Python  , Machine Learning , Causal Inference , Causal Analysis , Root Cause Analysis , Grafana , docker , Kubernetes , Linux , prometheus , zipkin , Neo4j.

            **Analyst - KPMG Global Services (Aug 2021 - Nov 2022)**  
            - Experienced in designing, deploying, and managing cloud-based solutions across AWS and Azure, with a strong focus on multi-cloud strategies and infrastructure-as-code (IaC) using Terraform. Proficient in containerization technologies such as Docker and orchestration with Kubernetes, enabling scalable and efficient deployment of microservices and applications.
            - Skilled in API development using FastAPI, creating robust and high-performance RESTful APIs to facilitate seamless integration between systems. Experienced in workflow automation, leveraging tools like Power Automate to streamline business processes and improve operational efficiency. 
            - Hands-on experience in system monitoring and performance optimization using Grafana, ensuring real-time visibility into system health and resource utilization. Managed virtual machines (VMs) across platforms, including IDERA and Helios VM, ensuring high availability and performance.
            - Expertise in CI/CD pipeline management using Jenkins, automating deployment processes and integrating version control systems (e.g., Git), Docker, and cloud platforms to enable continuous integration and delivery. Developed and supported SaaS service models using PowerApps, SharePoint, and Power Automate, delivering scalable and user-friendly solutions for enterprise clients.
            - ** Skills:** Python (Programming Language) , docker , Cloud Computing , Cluster Analysis , Kubernetes , Computer Science , Grafana , prometheus , Amazon Web Services (AWS) , Microsoft Azure , Microsoft Power Automate , SharePoint , Microsoft Power Apps , FastAPI. 

            **Hardware Engineer - Digitectura Technology (Mar 2021 - Apr 2021 )**  
            - As a Hardware Engineer Intern, I worked on designing, testing, and troubleshooting electronic circuits and embedded systems. My role involved hands-on experience with communication protocols such as I2C, UART, and SPI, ensuring seamless data transfer between microcontrollers, sensors, and other peripherals. I also worked with microprocessors and FPGAs, gaining exposure to VHDL programming for hardware description and FPGA-based implementations.
            - Additionally, I performed soldering and PCB assembly for prototype development, ensuring proper component placement and connectivity. I worked on debugging electronic circuits using oscilloscopes, logic analyzers, and multimeters to validate system performance. This internship provided me with practical experience in electronics design, embedded systems, and FPGA development, strengthening my problem-solving and hardware development skills. 
            - **Skills:** Service Provider Interface (SPI) , Communication , I2C , Universal Asynchronous Receiver/Transmitter (UART) , Electrical Engineering , Electronics , VHDL , Field-Programmable Gate Arrays (FPGA) , Digital Electronics , Electronic Control Systems. 

            **Embedded & IoT Engineer - Tequed Labs(Jan 2020 - Feb 2020 )**  
            - As an IoT Engineer Intern, I worked on embedded systems development with a focus on Linux, UART communication, and C programming. My role involved interfacing electronic circuits with microcontrollers, particularly using Arduino, to develop and test IoT solutions.
            - I gained hands-on experience in serial communication (UART), debugging embedded systems, and writing firmware in C to control hardware components. Additionally, I worked with Arduino-based sensors and actuators, ensuring proper integration and functionality within IoT applications. This internship enhanced my skills in embedded development, electronics, and system troubleshooting, providing practical exposure to hardware-software interaction in IoT systems. 
            - ** Skills:** Automotive , Universal Asynchronous Receiver/Transmitter (UART) , Electronics , Digital Electronics , Electronic Control Systems , Linux , C (Programming Language) , Hardware.
        """, unsafe_allow_html=True),

        "Projects": lambda: st.markdown("""
            ### 🔬 Projects  
            - 🚀 **AI Chatbot** - NLP-based virtual assistant  
            - 🔍 **Web Scraper** - Automated data extraction  
            - 🌐 **Portfolio Website** - Personal branding  
        """, unsafe_allow_html=True),

        "Skills": lambda: st.markdown("""
            ### 🛠 Skills  
            ✅ **Languages:** Python, JavaScript, C++  
            ✅ **AI & ML:** Deep Learning, NLP, Computer Vision  
            ✅ **Cloud:** AWS, Azure, GCP  
            ✅ **DevOps:** Docker, Kubernetes, CI/CD  
        """, unsafe_allow_html=True),

        "Achievements": lambda: st.markdown("""
            ### 🏆 Achievements  
            🏅 **Winner - Hackathon 2023**  
            📜 **Published Research Paper on AI**  
            💡 **Developed ML Model with 98% Accuracy**  
        """, unsafe_allow_html=True),

        "Languages": lambda: st.markdown("""
            ### 🌍 Languages  
            🗣️ **English:** Fluent  
            🗣️ **German:** Intermediate  
            🗣️ **French:** Basic  
        """, unsafe_allow_html=True),

        "Hobby": lambda: st.markdown("""
            ### 🎭 Hobbies  
            📷 **Photography**  
            ♟️ **Chess**  
            ✍️ **Blogging**  
        """, unsafe_allow_html=True),
    }

    # Display Selected Section
    if section in section_data:
        section_data[section]()


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
