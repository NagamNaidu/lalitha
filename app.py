import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume - Lalitha Priya"
PAGE_ICON = ":wave:"
NAME = "Lalitha Priya"
DESCRIPTION = "Operations Manager | Training & Process Excellence | Lean Six Sigma | KPI Optimization | 10+ Years in People & Performance"
EMAIL = "priyalalitha0911@gmail.com"
PHONE = "+91-7981276741"
HYPERLINKS = {
    "LinkedIn": "https://www.linkedin.com/",
    "GitHub": "https://github.com/",
    "Website": "https://www.example.com/"
}
LOCATION = "Hyderabad, Telangana, India"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- FUNCTION TO LOAD LOTTIE ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- LOTTIE FILES URLS ---
lottie_summary = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_w51pcehl.json")
lottie_projects = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_vnikrcia.json")
lottie_experience = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_kkflmtur.json")
lottie_certifications = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_bhw1ul4g.json")
lottie_achievements = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_mkcnkspy.json")

# --- CUSTOM CSS ---
st.markdown(
    """
    <style>
    .header-card {
        background-color: #f0f2f6;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        animation: slideFade 1s ease-in-out;
    }
    .tab-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0px 4px 12px rgba(0, 123, 255, 0.1);
        animation: fadeInSlide 0.6s ease-in-out;
    }
    @keyframes fadeInSlide {
        0% {opacity: 0; transform: translateY(20px);}
        100% {opacity: 1; transform: translateY(0);}
    }
    @keyframes slideFade {
        0% {opacity: 0; transform: translateX(-20px);}
        100% {opacity: 1; transform: translateX(0);}
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- HEADER SECTION ---
with st.container():
    st.markdown("<div class='header-card'>", unsafe_allow_html=True)
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(f"📞 {PHONE} | ✉️ {EMAIL}")
    st.write(f"🌐 {LOCATION}")

    col1, col2, col3 = st.columns(3)
    with col1:
        if "LinkedIn" in HYPERLINKS:
            st.link_button("LinkedIn", HYPERLINKS["LinkedIn"])
    with col2:
        if "GitHub" in HYPERLINKS:
            st.link_button("GitHub", HYPERLINKS["GitHub"])
    with col3:
        if "Website" in HYPERLINKS:
            st.link_button("Website", HYPERLINKS["Website"])

    st.markdown("</div>", unsafe_allow_html=True)

# --- PROFESSIONAL SUMMARY ---
st_lottie(lottie_summary, height=200, key="summary")
st.markdown("<div class='tab-card'>", unsafe_allow_html=True)
st.header("Professional Summary")
st.write("""
Dynamic and results-oriented professional with over 10 years of experience in Operations, Training, Data Management, and Project Management...
""")
st.subheader("Core Competencies:")
st.write("""
- Project Management & Planning
- Operations & Team Leadership
- Master Data Management (MDM)
- ...
""")
st.markdown("</div>", unsafe_allow_html=True)

# --- PROJECTS ---
st_lottie(lottie_projects, height=200, key="projects")
st.markdown("<div class='tab-card'>", unsafe_allow_html=True)
st.header("Projects")
st.subheader("Lean & Six sigma Projects")
st.write("""
- Conducted a Value Stream Mapping (VSM)...
""")
st.markdown("</div>", unsafe_allow_html=True)

# --- EXPERIENCE ---
st_lottie(lottie_experience, height=200, key="experience")
st.markdown("<div class='tab-card'>", unsafe_allow_html=True)
st.header("Professional Experience")
st.subheader("LYROS, Hyderabad, TS - Operation Manager (Feb 2024 – Present)")
st.write("""
- Managed day-to-day operations across multiple teams...
""")
st.markdown("</div>", unsafe_allow_html=True)

# --- CERTIFICATIONS ---
st_lottie(lottie_certifications, height=200, key="certifications")
st.markdown("<div class='tab-card'>", unsafe_allow_html=True)
st.header("Certifications")
st.write("""
- Six Sigma – Yellow Belt
- Lean Management
- Agile Fundamentals
- TQM
- PMP (In Progress)
""")
st.markdown("</div>", unsafe_allow_html=True)

# --- ACHIEVEMENTS ---
st_lottie(lottie_achievements, height=200, key="achievements")
st.markdown("<div class='tab-card'>", unsafe_allow_html=True)
st.header("Achievements")
st.write("""
- Increased operational efficiency by 25% through process streamlining...
""")
st.markdown("</div>", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.header("Personal Profile")
# Replace image path as needed
st.sidebar.image("lalitha.jpg", width=120)
st.sidebar.write("**Full Name:** Lalitha Priya")
st.sidebar.write("**Date of Birth:** 11-09-1990")
st.sidebar.write("**Gender:** Female")
st.sidebar.write("**Religion:** Hindu")
st.sidebar.write("**Nationality:** Indian")
st.sidebar.write("**Languages Known:** Telugu, Tamil, English and Hindi")

# --- FOOTER ---
st.markdown("---")
st.write("© 2025 Lalitha Priya. All rights reserved.")
