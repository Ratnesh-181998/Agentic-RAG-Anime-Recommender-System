
import streamlit as st
import os
import sys
import datetime
import pytz
from dotenv import load_dotenv

# Add the parent directory to sys.path to ensure we can import pipeline
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pipeline.pipeline import AnimeRecommendationPipeline

# -----------------------------------------------------------------------------
# Configuration & Setup
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Anime Recommender Dashboard",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_dotenv()

# --- Custom CSS for Premium Design ---
st.markdown("""
<style>
    /* Global Theme & Colors */
    :root {
        --primary-color: #FF4B4B;
        --secondary-color: #1E1E1E;
        --accent-gold: #FFD700;
        --accent-cyan: #00E5FF;
        --text-light: #FAFAFA;
        --bg-dark: #0E1117;
    }
    
    /* App Background */
    .stApp {
        background: linear-gradient(to right, #141E30, #243B55);
        color: var(--text-light);
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    [data-testid="stSidebar"] h1 {
        color: var(--accent-gold) !important;
        font-size: 1.8rem;
    }

    /* Header Styling */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        text-shadow: 0px 2px 4px rgba(0,0,0,0.5);
    }
    h1 { color: var(--accent-cyan); }
    h2 { color: var(--accent-gold); }

    /* Button Styling */
    .stButton>button {
        background: linear-gradient(45deg, #FF512F 0%, #DD2476 100%);
        color: white;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        font-weight: bold;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(221, 36, 118, 0.4);
    }

    /* Input Field Styling */
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 8px;
    }
    .stTextInput>div>div>input:focus {
        border-color: var(--accent-cyan);
        box-shadow: 0 0 8px rgba(0, 229, 255, 0.3);
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 8px 8px 0 0;
        color: #ddd;
        font-weight: 600;
        border: none;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(0, 229, 255, 0.1) !important;
        color: var(--accent-cyan) !important;
        border-bottom: 3px solid var(--accent-cyan);
    }

    /* Card/Container Styling */
    div.stMarkdown > div {
       color: #e0e0e0;
    }
    
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

def get_ist_time():
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_now = utc_now.astimezone(ist_timezone)
    return ist_now.strftime("%Y-%m-%d %H:%M:%S IST")

def load_file_content(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File not found at {path}"
    except Exception as e:
        return f"Error reading file: {str(e)}"

# -----------------------------------------------------------------------------
# Layout Components
# -----------------------------------------------------------------------------

# Render Top-Right Professional Badge
def render_profile_badge():
    col1, col2 = st.columns([6, 1.5])
    with col1:
        st.write("") # Spacer
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); 
                    padding: 10px; border-radius: 10px; 
                    box-shadow: 0 4px 6px rgba(0,0,0,0.3); 
                    text-align: center; border: 1px solid rgba(255,255,255,0.1);'>
            <div style='color: #FFD700; font-weight: bold; font-size: 0.9rem; margin-bottom: 2px;'>Ratnesh Kumar Singh</div>
            <div style='color: #00E5FF; font-size: 0.75rem; font-weight: 500;'>Data Scientist (AI/ML Engineer)</div>
            <div style='color: #e0e0e0; font-size: 0.7rem;'>4+ Years Experience</div>
        </div>
        """, unsafe_allow_html=True)

# Sidebar
def render_sidebar():
    st.sidebar.markdown("""
    <div style='text-align: center; margin-bottom: 20px;'>
        <h1 style='margin-bottom: 0;'>🎬 AI Anime</h1>
        <p style='color: #aaa; font-size: 0.9rem;'>Recommender System</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("### ⏱️ System Status")
    st.sidebar.info(f"**Server Time (IST):**\n{get_ist_time()}")

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📂 Project Navigation")
    
    # Using expanders for cleaner look
    with st.sidebar.expander("📁 Core Codebase", expanded=True):
        st.code("""
Code/
├── app/
├── config/
├── data/
├── pipeline/
├── src/
└── logs/
        """, language="text")
        
    with st.sidebar.expander("📄 Documentation"):
        st.code("""
Project Doc/
├── About.txt
├── Architecture.txt
└── Tech Stack.txt
        """, language="text")

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 👨‍💻 Developer Info")
    st.sidebar.markdown("**Ratnesh Kumar Singh**")
    st.sidebar.caption("Data Scientist (AI/ML Engineer)")
    st.sidebar.caption("4+ Years Experience")

# Main Content
def render_main():
    render_profile_badge()
    
    st.markdown("""
    <div style='text-align: center; padding: 20px 0 40px 0;'>
        <h1 style='font-size: 3rem; margin-bottom: 10px;'>🎬 AI Anime Recommender System</h1>
        <p style='font-size: 1.2rem; color: #ccc;'>Discover your next favorite anime using advanced AI embeddings and semantic search.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🚀 Project Demo", 
        "ℹ️ About Project", 
        "🛠 Tech Stack", 
        "🏗 Architecture", 
        "📊 System Logs"
    ])

    # --- Tab 1: Demo ---
    with tab1:
        st.markdown("### 🧠 AI Recommendation Engine")
        st.markdown("Type a description of what you want to watch. Be as specific or vague as you like!")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            pipeline = init_pipeline()
            query = st.text_input("Describe your preferences:", placeholder="e.g., A dark fantasy with psychological elements and epic battles")
            
            if st.button("🔍 Get Recommendations", type="primary"):
                if query:
                    with st.spinner("🤖 Analyzing semantics & searching vector database..."):
                        try:
                            # Start timer
                            start_time = datetime.datetime.now()
                            response = pipeline.recommend(query)
                            end_time = datetime.datetime.now()
                            duration = (end_time - start_time).total_seconds()
                            
                            st.success(f"Analysis Complete in {duration:.2f} seconds!")
                            
                            st.markdown("#### 🎯 Top AI Picks For You")
                            st.markdown(f"""
                            <div style='background-color: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px; border-left: 5px solid #00E5FF;'>
                                {response}
                            </div>
                            """, unsafe_allow_html=True)
                        except Exception as e:
                            st.error(f"An error occurred: {str(e)}")
                else:
                    st.warning("Please enter a description to get recommendations.")
                    
        with col2:
            st.markdown("#### 💡 Try These:")
            if st.button("School Romance"):
                st.info("Try searching: 'Sweet high school romance with drama'")
            if st.button("Cyberpunk Action"):
                st.info("Try searching: 'Futuristic cyberpunk action with robots'")
            if st.button("Dark Fantasy"):
                st.info("Try searching: 'Dark fantasy world with magic and demons'")

    # --- Tab 2: About ---
    with tab2:
        st.markdown("### 📖 About This Project")
        about_path = os.path.join(os.path.dirname(__file__), '..', '..', 'Project Doc', 'About.txt')
        content = load_file_content(about_path)
        
        st.markdown(f"""
        <div style='background-color: rgba(0,0,0,0.2); padding: 25px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.1);'>
            {content}
        </div>
        """, unsafe_allow_html=True)

    # --- Tab 3: Tech Stack ---
    with tab3:
        st.markdown("### 🛠 Technologies Used")
        tech_path = os.path.join(os.path.dirname(__file__), '..', '..', 'Project Doc', 'Teck Stack.txt')
        content = load_file_content(tech_path)
        
        col_tech1, col_tech2 = st.columns([1, 1])
        with col_tech1:
            st.markdown(f"""
            <div style='background-color: rgba(0,0,0,0.2); padding: 25px; border-radius: 10px; height: 100%; border: 1px solid rgba(255,255,255,0.1);'>
                {content}
            </div>
            """, unsafe_allow_html=True)
        with col_tech2:
             st.image("https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white")
             st.image("https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white")
             st.image("https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white")
             st.image("https://img.shields.io/badge/ChromaDB-Search-brightgreen?style=for-the-badge")
             st.image("https://img.shields.io/badge/Groq-Inference-orange?style=for-the-badge")

    # --- Tab 4: Architecture ---
    with tab4:
        st.markdown("### 🏗 System Architecture Diagram")
        
        st.info("Visual representation of the High Level Design (HLD) and Low Level Design (LLD) of the system.")
        
        img_path1 = os.path.join(os.path.dirname(__file__), '..', 'HLD&LLD.png')
        if os.path.exists(img_path1):
            st.image(img_path1, caption="High Level & Low Level Design", use_container_width=True)
        else:
            st.warning("HLD&LLD.png not found.")

        st.markdown("---")
        st.markdown("### 🔄 AI Workflow")

        img_path2 = os.path.join(os.path.dirname(__file__), '..', 'AI+Anime+Recommender+Workflow.png')
        if os.path.exists(img_path2):
            st.image(img_path2, caption="AI Workflow Diagram", use_container_width=True)
        else:
            st.warning("Workflow image not found.")

    # --- Tab 5: Logs ---
    with tab5:
        st.markdown("### 📊 System Execution Logs")
        logs_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
        
        if os.path.exists(logs_dir):
            log_files = [f for f in os.listdir(logs_dir) if f.endswith('.log')]
            if log_files:
                col_sel, col_btn = st.columns([3, 1])
                with col_sel:
                    selected_log = st.selectbox("Select Log File", log_files, index=len(log_files)-1)
                
                log_content = load_file_content(os.path.join(logs_dir, selected_log))
                
                with col_btn:
                     st.download_button("📥 Download Log", log_content, file_name=selected_log)

                st.markdown("#### Log Viewer")
                st.code(log_content, language="log")
            else:
                st.info("No log files found in logs directory.")
        else:
            st.error(f"Logs directory not found at {logs_dir}")

# -----------------------------------------------------------------------------
# Main Execution
# -----------------------------------------------------------------------------
render_sidebar()
render_main()
