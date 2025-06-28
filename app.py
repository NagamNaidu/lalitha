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
    "GitHub": "https://www.example.com/"
    }
LOCATION = "Hyderabad, Telangana, India"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS ---
with open("style/style.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- SIDEBAR SECTION ---
with st.sidebar:
    img_width = 150
    img_height = 150
    image_path = "lalitha.jpg"
    import os
    image_path = os.path.abspath(image_path)
    try:
        img = Image.open(image_path)
        img = img.resize((img_width, img_height))
        st.image(img, width=img_width, use_container_width=False)
    except FileNotFoundError:
        st.error("Failed to load image")
    except Exception as e:
        st.error(f"Error: {e}")
    st.markdown('<style>img{border-radius: 50% !important;}</style>', unsafe_allow_html=True)
    st.title("Lalitha Priya")
    st.write("Date of Birth: 11-09-1990")
    st.write("Religion: Hindu")
    st.write("Nationality: Indian")
    st.write("Languages Known: Telugu, Tamil, English and Hindi")

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
lottie_achievements = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_w51pcehl.json")

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
    # --- GENERAL SETTINGS ---
    PAGE_TITLE = "Digital Resume - Lalitha Priya"
    PAGE_ICON = ":wave:"
    NAME = "Lalitha Priya"
    DESCRIPTION = "Operations Manager | Training & Process Excellence | Lean Six Sigma | KPI Optimization | 10+ Years in People & Performance"
    EMAIL = "priyalalitha0911@gmail.com"
    PHONE = "+91-7981276741"
    HYPERLINKS = {
        "LinkedIn": "https://www.linkedin.com/",
        "GitHub": "https://www.example.com/"
        }
    LOCATION = "Hyderabad, Telangana, India"
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


# --- TABS SECTION ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Professional Summary","Projects", "Experience", "Certifications", "Achievements"])

with tab1:
    if lottie_summary:
        st_lottie(lottie_summary, height=200, key="summary_tab_228")
    else:
        st.error("Failed to load summary animation")
    st.markdown("<div class='tab-card'>", unsafe_allow_html=True)
    st.header("Professional Summary")
    st.write("""
    Dynamic and results-oriented professional with over 10 years of experience in Operations, Training, Data Management, and Project Management. Proven ability to lead cross-functional teams, manage end-to-end project lifecycles, and deliver high-impact results. Adapt at stakeholder engagement, risk mitigation, process optimization, and continuous improvement. Seeking a role where I can apply my leadership, project execution, and operational strategy skills to contribute to organizational success.
    """)
    st.subheader("Core Competencies:")
    st.write("""
    - Project Management & Planning
    - Operations & Team Leadership
    - Master Data Management (MDM)
    - Process Improvement & Optimization
    - Stakeholder & Client Relationship Management
    - Learning & Development (L&D)
    - Risk Management & Escalation Handling
    - KPI Monitoring & MIS Reporting
    - Content Development & Virtual Training
    - MS Excel (Advanced), PowerPoint, Zoom, Teams
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    if lottie_projects:
        st_lottie(lottie_projects, height=200, key="projects_tab_253")
    else:
        st.error("Failed to load projects animation")
    st.markdown("<div class='tab-card'>", unsafe_allow_html=True)
    st.header("Projects")
    with st.expander("Lean & Six sigma Projects", expanded=False):
        st.write("""
        - Conducted a Value Stream Mapping (VSM) exercise across the new hire onboarding and post-training performance tracking workflow.
        - Identified redundant touchpoints, delays in content delivery, and manual reporting efforts.
        - Streamlined communication between training, HR, and operations, eliminating repeated documentation and delays in floor deployment.
        - Introduced checklists, automated reports, and a centralized SOP repository to standardize tasks.
        - Integrated lean principles into daily stand-up reviews and feedback loops.
        """)
    with st.expander("Process Optimization & SLA Alignment – LYROS (2024)", expanded=False):
        st.write("""
        - Conducted in-depth analysis of existing workflows across departments
        - Re-engineered operational processes to align with business SLAs, resulting in a 25% improvement in turnaround times and 15% increase in customer satisfaction.
        - Created SOPs and checklists for consistent service delivery
        """)
    with st.expander("Performance Dashboard Implementation – LYROS (2024)", expanded=False):
        st.write("""
        - Led the implementation of an interactive performance dashboard to track team metrics (productivity, quality, adherence).
        - Enabled real-time decision-making for team leads and managers.
        - Reduced manual reporting efforts by 40%.
        """)
    with st.expander("Cross-Team Resource Reallocation Strategy – Wipro (2023)", expanded=False):
        st.write("""
        - Developed a workforce optimization plan during a high-volume project phase.
        - Successfully reallocated resources between training, support, and operations to handle demand spikes without additional hires.
        - Improved efficiency by 20% and saved INR 3 lakhs/month in manpower costs.
        """)
    with st.expander("WFH Transition & Policy Setup – COVID/Post-COVID Period", expanded=False):
        st.write("""
        - Coordinated operational shift to remote work setup for 50+ employees.
        - Established WFH guidelines, compliance trackers, and daily team sync models.
        - Maintained business continuity at 98% with zero SLA breaches.
        """)
    with st.expander("Quality & Compliance Initiative – Internal Audit Readiness (2022)", expanded=False):
        st.write("""
        - Spearheaded an internal audit readiness program focusing on process documentation, compliance training, and mock audits.
        - Improved audit scores by 30%, ensuring alignment with corporate and client expectations.
        """)
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    if lottie_experience:
        st_lottie(lottie_experience, height=200, key="experience_tab_299")
    else:
        st.error("Failed to load experience animation")
    st.markdown("<div class='tab-card'>", unsafe_allow_html=True)
    st.header("Professional Experience")
    with st.expander("LYROS, Hyderabad, TS - Operation Manager (Feb 2024 – Present)", expanded=False):
        st.write("""
        - Managed day-to-day operations across multiple teams, ensuring adherence to defined SLAs, productivity metrics, and quality benchmarks.
        - Led workforce planning and resource allocation, including shift rosters, leave planning, and peak load management to maintain optimal team performance.
        - Collaborated with the L&D team to align training outcomes with operational needs, ensuring smooth transition of new hires from training to production.
        - Monitored and analyzed key operational KPIs such as TAT, AHT, CSAT, and FCR, driving regular performance reviews and improvement initiatives.
        - Developed and enforced Standard Operating Procedures (SOPs) and process manuals to ensure consistent and error-free service delivery.
        - Conducted daily stand-up meetings, performance syncs, and one-on-one coaching to track goals, resolve blockers, and promote accountability.
        - Handled escalations and coordinated with internal stakeholders to ensure timely issue resolution and customer satisfaction.
        - Oversaw reporting and MIS dashboards, enabling real-time decision-making through data-driven insights.
        - Led internal quality audits and participated in external reviews to ensure operational compliance and business continuity readiness.
        - Supported digital adoption by implementing automation tools and performance dashboards, streamlining workflows and reducing manual errors.
        """)
    with st.expander("Wipro, Hyderabad, TS - Deputy Manager Operations (Oct 2016 – Aug 2023)", expanded=False):
        st.write("""
        - Led daily operations for cross-functional teams, ensuring smooth workflow, SLA adherence, and quality compliance across training and service delivery units.
        - Collaborated with training, HR, and business units to align operational strategies with organizational objectives.
        - Designed and implemented SOPs for end-to-end processes, improving task consistency and onboarding efficiency.
        - Monitored team performance using KPIs and dashboards; analyzed trends and provided actionable feedback to drive improvements.
        - Coordinated resource allocation and workload management during peak periods, optimizing staffing across functions.
        - Conducted regular internal audits and process reviews, ensuring compliance with internal quality benchmarks and client expectations.
        - Facilitated communication between leadership and team leads through structured daily stand-ups and performance syncs.
        """)
    with st.expander("Call health - Sr. Trainer & Team Leader (Sep 2014 - Oct 2016)", expanded=False):
        st.write("""
        - Supervised a team of customer care executives, ensuring performance targets were met in terms of TAT, AHT, and CSAT.
        - Conducted daily team huddles, performance reviews, and coaching sessions to improve service delivery.
        - Handled escalations, managed shift schedules, and ensured adequate coverage during peak and off-peak hours.
        - Acted as a liaison between frontline teams and management to ensure communication, issue resolution, and policy updates were effectively shared.
        - Ensured compliance with company protocols, client SLAs, and quality parameters across all team functions.
        - Conducting Training Need Analysis and report training needs for the location.
        - Interact with Quality Team and finding out the training requirements. Setting expectations to achieve KPI and productivity targets for the team.
        - Conducting On Job Training modules and motivating the team to achieve set sales targets Monitoring the performance of the associated on daily basis.
        - Maintaining reports and giving instant feedback to them to improve the performance.
        - Escalating the issues to the client and see that the problem is rectified.
        - Preparing report after evaluating all trainees. Attending call calibrations with quality and training team internal as well external team.
        - Product and process training for the NHTs whenever required.
        - Preparing content as per the training requirement
        - Preparing Virtual videos for training
        - Expertise in conducting webinar sessions.
        - Setting expectations to achieve KPI and productivity targets for the team.
        - Handling Real Time Q Management to answer maximum numbers of calls and to maintain AHT & ACW.
        - Analyze various reports to enhance productivity.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
    with st.expander("Vertex Customer Solutions Pvt ltd - Sr. Team Leader (Jun 2013 - Aug 2014)", expanded=False):
        st.write("""
        - Handling a team of 20 associates.
        - Setting expectations to achieve KPI and productivity targets for the team.
        - Handling Real Time Q Management to answer maximum numbers of calls and to maintain AHT & ACW.
        - Analyse various reports to enhance productivity.
        - Monitoring the performance of the associated on daily basis.
        - Maintaining reports and giving instant feedback to them to improve the performance.
        - Escalating the issues to the client and see that the problem is rectified.
        - Taking Escalations and follow up on the same with the client.
        - Attending call calibrations with quality and training team internal as well external team.
        - Product and process training for the NHTs whenever required.
        """)
    with st.expander("Digicall Teleservices Pvt ltd - Sr. Team Leader (Mar 2010 - Dec-2012)", expanded=False):
        st.write("""
        - Handling a team of 20 associates.
        - Setting expectations to achieve KPI and productivity targets for the team.
        - Handling Real Time Q Management to answer maximum numbers of calls and to maintain AHT & ACW.
        - Analyse various reports to enhance productivity.
        - Monitoring the performance of the associated on daily basis.
        - Maintaining reports and giving instant feedback to them to improve the performance.
        - Escalating the issues to the client and see that the problem is rectified.
        - Taking Escalations and follow up on the same with the client.
        - Attending call calibrations with quality and training team internal as well external team.
        - Product and process training for the NHTs as required.
        """)

with tab4:
    if lottie_certifications:
        st_lottie(lottie_certifications, height=200, key="certifications_tab_353")
    else:
        st.error("Failed to load certifications animation")
    st.write("""
    - Six Sigma – Yellow Belt
    - Lean Management
    - Agile Fundamentals
    - TQM (Total Quality Management)
    - PMP (In Progress)
    """)

with tab5:
    if lottie_achievements:
        st_lottie(lottie_achievements, height=200, key="achievements_tab_366")
    else:
        st.error("Failed to load achievements animation")
    st.write("""
    - Increased operational efficiency by 25% through process streamlining, automation of reports, and removal of redundant steps in workflow.
    - Reduced average response and resolution time by 30%, aligning team output with client SLAs and improving service quality.
    - Successfully managed cross-functional teams of 20+, enhancing collaboration and productivity through structured performance reviews and daily huddles.
    - Lowered operational costs by INR 5 lakhs annually by implementing resource optimization strategies and reusing existing infrastructure.
    - Achieved 98% SLA compliance consistently for three quarters by introducing proactive monitoring tools and escalation matrices.
    - Developed and implemented SOPs and operational manuals, leading to a 20% decrease in process deviations and audit issues.
    - Spearheaded a Work-From-Home operational transition for over 50 employees, maintaining uninterrupted service delivery during COVID/post-COVID shifts.
    - Improved employee engagement scores by 35% by launching recognition programs and team-building initiatives focused on accountability and collaboration.
    - Introduced a daily performance dashboard, reducing manual reporting time by 40% and enabling faster data-driven decisions.
    - Played a key role in client retention and satisfaction, receiving positive feedback during quarterly reviews and external audits.
    """)
#st.write(\"\"\"
# - Increased operational efficiency by 25% through process streamlining, automation of reports, and removal of redundant steps in workflow.
# - Reduced average response and resolution time by 30%, aligning team output with client SLAs and improving service quality.
# - Successfully managed cross-functional teams of 20+, enhancing collaboration and productivity through structured performance reviews and daily huddles.
# - Lowered operational costs by INR 5 lakhs annually by implementing resource optimization strategies and reusing existing infrastructure.
# - Achieved 98% SLA compliance consistently for three quarters by introducing proactive monitoring tools and escalation matrices.
# - Developed and implemented SOPs and operational manuals, leading to a 20% decrease in process deviations and audit issues.
# - Spearheaded a Work-From-Home operational transition for over 50 employees, maintaining uninterrupted service delivery during COVID/post-COVID shifts.
# - Improved employee engagement scores by 35% by launching recognition programs and team-building initiatives focused on accountability and collaboration.
# - Introduced a daily performance dashboard, reducing manual reporting time by 40% and enabling faster data-driven decisions.
# - Played a key role in client retention and satisfaction, receiving positive feedback during quarterly reviews and external audits.
#\"\"\")
#
#
#

#    - Increased operational efficiency by 25% through process streamlining, automation of reports, and removal of redundant steps in workflow.
#    - Reduced average response and resolution time by 30%, aligning team output with client SLAs and improving service quality.
#    - Successfully managed cross-functional teams of 20+, enhancing collaboration and productivity through structured performance reviews and daily huddles.
#    - Lowered operational costs by INR 5 lakhs annually by implementing resource optimization strategies and reusing existing infrastructure.
#    - Achieved 98% SLA compliance consistently for three quarters by introducing proactive monitoring tools and escalation matrices.
#    - Developed and implemented SOPs and operational manuals, leading to a 20% decrease in process deviations and audit issues.
#    - Spearheaded a Work-From-Home operational transition for over 50 employees, maintaining uninterrupted service delivery during COVID/post-COVID shifts.
#    - Improved employee engagement scores by 35% by launching recognition programs and team-building initiatives focused on accountability and collaboration.
#    - Introduced a daily performance dashboard, reducing manual reporting time by 40% and enabling faster data-driven decisions.
#    - Played a key role in client retention and satisfaction, receiving positive feedback during quarterly reviews and external audits.
#    \"\"\")










































# --- CERTIFICATIONS AND ACHIEVEMENTS ---
# st.header("Certifications")
# if lottie_certifications:
#     st_lottie(lottie_certifications, height=200, key="certifications_tab_353")
# else:
#     st.error("Failed to load certifications animation")
# st.write("""
# - Six Sigma – Yellow Belt
# - Lean Management
# - Agile Fundamentals
# - TQM (Total Quality Management)
# - PMP (In Progress)
# """)

# st.header("Achievements")
# if lottie_achievements:
#     st_lottie(lottie_achievements, height=200, key="achievements_tab_366")
# else:
#     st.error("Failed to load achievements animation")
# st.write("""
# - Increased operational efficiency by 25% through process streamlining, automation of reports, and removal of redundant steps in workflow.
# - Reduced average response and resolution time by 30%, aligning team output with client SLAs and improving service quality.
# - Successfully managed cross-functional teams of 20+, enhancing collaboration and productivity through structured performance reviews and daily huddles.
# - Lowered operational costs by INR 5 lakhs annually by implementing resource optimization strategies and reusing existing infrastructure.
# - Achieved 98% SLA compliance consistently for three quarters by introducing proactive monitoring tools and escalation matrices.
# - Developed and implemented SOPs and operational manuals, leading to a 20% decrease in process deviations and audit issues.
# - Spearheaded a Work-From-Home operational transition for over 50 employees, maintaining uninterrupted service delivery during COVID/post-COVID shifts.
# - Improved employee engagement scores by 35% by launching recognition programs and team-building initiatives focused on accountability and collaboration.
# - Introduced a daily performance dashboard, reducing manual reporting time by 40% and enabling faster data-driven decisions.
# - Played a key role in client retention and satisfaction, receiving positive feedback during quarterly reviews and external audits.
# """)
