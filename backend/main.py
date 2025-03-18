import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import google.generativeai as genai
# Set Hugging Face API Key (Replace with your key)

GOOGLE_API_KEY = "AIzaSyDHQ4oxBF3eYLy-vNKbA-U8AwhB2Eivm_E"
genai.configure(api_key=GOOGLE_API_KEY)
for model in genai.list_models():
    print(model.name)

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
            st.markdown("### Name: Rithvik Narayana Swamy"),
            st.markdown("📧 **Email:** rithviknswamy@gmail.com"),
            st.markdown("📞 **Phone:** +49 1577 8463738"),
        ),

        "Education": lambda: st.markdown("""
            ### 🎓 Education  
            **M.S in Information Technology - University Of Stuttgart (Nov 2022 - April 2025) **  
            📊 **Grade:** 2.0 GPA  
            🔬 ** Discription** I am currently pursuing my Master of Science in Information Technology (Infotech) at the University of Stuttgart, where I am deepening my knowledge and skills in advanced IT concepts, machine learning, DevOps practices, and their practical applications.                        
            🏫 **Skills:** Docker, Cloud Computing,causality mining,root cause anaysis, LSTM, C++, Embedded Systems, AI, Kubernetes  
            
            **B.Tech - Dayananda Sagar College of Engineering (Jun 2017 - Aug 2021)**  
            📊 **Grade:** 9.05 CGPA  
            🔬 ** Discription** I completed my Bachelor of Engineering (BE) in Electronics and Communication Engineering (ECE) from Dayananda Sagar College of Engineering, This program provided me with a strong foundation in both theoretical knowledge and practical skills, preparing me for a career in the ever-evolving field.                         
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
            🚀 **Implementation of masked and unmasked LSTM on FPGA (Nov 2023 - May 2024)** 
            - Built a LSTM model followed by an FCNN model for digit recognition using MNIST dataset. Masking of LSTM is done to secure the weights and biases of the LSTM network. The main focus of this was to prevent the side channel attacks. 
            - The projects consist of two main sections. Initially, an LSTM network was formulated and deployed on a Xilinx Spartan-6 FPGA. Then implementation of masking techniques customized for LSTM networks is carried out.
            - To commence, the trained neural network from TensorFlow undergoes unrolling to extract weights and biases. This data serves as the foundation for the neural network implementation. 
            - The first LSTM neural network comprises 28 LSTM layers, each containing 2 unit cells (memory units), followed by four fully connected layers with dimensions 30, 30, 10, and 10, respectively. 
            🔗 [For further details, refer to the GitHub repository](https://github.com/Rithvikns/Implementation-of-masked-and-unmasked-LSTM/tree/main).

            🔍 **AI Planning In Smart Warehousing (Oct 2023 - Mar 2024)** 
            - This Research explores the transformative role of AI planning in smart warehousing, highlighting its potential to streamline operations, enhance productivity, and reduce costs through advanced technologies like robotics and machine learning.
            -  It delves into various AI planning techniques, such as classical, heuristic, temporal, and contingency planning, and their applications in inventory management, task allocation, and predictive maintenance within smart warehouses. The paper also examines real-world implementations, including the RoboPlanner framework for autonomous robots, and discusses the challenges of AI integration, such as high costs, data security, and the need for skilled personnel.
            - Additionally, it compares formal languages like PDDL, OWL, Prolog, and ASP for AI planning in warehousing, emphasizing their unique strengths and use cases. The paper concludes by outlining future trends, including enhanced AI algorithms, human-robot collaboration, IoT integration, and sustainability, while advocating for a blended approach to AI planning to address the complex demands of modern logistics. 
            🔗 [For further details, refer to the GitHub repository](https://github.com/Rithvikns/Project_papers/blob/main/A3_Paper_Narayana_Swamy.pdf).

            🚀 **TRAFFIC RULES VIOLATION RECOGNITION FOR TWO-WHEELER USING YOLO ALGORITHM (Nov 2020 - Jul 2021)** 
            - This project presents a system for detecting traffic rule violations by two-wheeler riders, specifically focusing on identifying riders without helmets and those engaging in triple riding (three people on a single motorcycle). The system leverages the YOLO (You Only Look Once) algorithm for real-time object detection, combined with Optical Character Recognition (OCR) for license plate recognition and Twilio for sending SMS alerts to authorities. 
            - The proposed solution aims to automate the process of identifying traffic violators using surveillance footage, reducing the need for human intervention and improving efficiency in traffic rule enforcement. Vehicle Detection: YOLO is used to detect motorcycles in real-time from surveillance videos.
            - Helmet Detection: After detecting the motorcycle, the system isolates the rider's head region and classifies whether a helmet is worn using YOLO. Triple Riding Detection: The system detects if three people are on a motorcycle using bounding boxes and counts the number of riders.
            - License Plate Recognition: OCR is used to extract the license plate number of the violating vehicle. SMS Alert: Twilio API sends an SMS to the concerned authority with the vehicle details of the violator.
            - The system was trained on a dataset prepared from Kaggle, CCTV footage, and custom datasets, achieving accuracies of 85% for helmet detection, 90-93% for triple riding detection, and 88-92% for license plate recognition. The paper concludes with future work aimed at improving the system's accuracy and scalability for real-time traffic signal applications
            🔗 [For further details, refer to the GitHub repository](https://github.com/Rithvikns/Project_papers/blob/main/project%20paper%20(1).pdf).
            
            🌐 **Portfolio Website with LLM** 
            - This is a **Portfolio Website** that showcases my work and allows users to interact with an **LLM-powered chat** to learn more details about me. The website is built using **Streamlit**, integrates with **Google Bard**, and utilizes **Python tools** alongside **vector embedding** with **instructive embedding** for enhanced responses.
            - **Personal Portfolio**: Displays my projects, experience, and skills.
            - **Chatbot Integration**: A chat interface for users to ask questions about my portfolio.
            - **Google Bard API**: Enables responses from a large language model.
            - **Streamlit UI**: Provides a simple and interactive front end.
            - **Vector Embeddings**: Uses instructive embedding to improve chatbot responses.
            - **Python Utilities**: Backend utilities to process user queries and data.
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
            🗣️ **German:** Basic
            🗣️ **Hindi:** Intermediate
            🗣️ **Kannada:** Fluent 
        """, unsafe_allow_html=True),

        "Hobby": lambda: st.markdown("""
            ### 🎭 Hobbies  
            📷 **Travelling`**  
            ♟️ **Chess**  
            ✍️ **Blogging**
            🏏 **Cricket**
            
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
