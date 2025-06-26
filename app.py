import streamlit as st
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

# --- HEADER SECTION ---
with st.container():
    st.markdown(
        """
        <style>
        .highlight-card {
            border: 2px solid #007bff; /* Blue highlight */
            border-radius: 5px;
            padding: 15px;
            margin-bottom: 10px;
            color: black; /* Black text */
        }
        .stButton>button {
            color: white;
            background-color: #007bff; /* Blue button */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
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

    st.markdown("---")

# --- BODY SECTION ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Professional Summary", "Projects", "Experience", "Certifications",  "Achievements"])

with tab1:
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

with tab2:
    st.header("Projects")
    st.subheader("Lean & Six sigma Projects")
    st.write("""
    - Conducted a Value Stream Mapping (VSM) exercise across the new hire onboarding and post-training performance tracking workflow.
    - Identified redundant touchpoints, delays in content delivery, and manual reporting efforts.
    - Streamlined communication between training, HR, and operations, eliminating repeated documentation and delays in floor deployment.
    - Introduced checklists, automated reports, and a centralized SOP repository to standardize tasks.
    - Integrated lean principles into daily stand-up reviews and feedback loops.
    """)
    st.markdown("---")
    st.subheader("Process Optimization & SLA Alignment – LYROS (2024)")
    st.write("""
    - Conducted in-depth analysis of existing workflows across departments
    - Re-engineered operational processes to align with business SLAs, resulting in a 25% improvement in turnaround times and 15% increase in customer satisfaction.
    - Created SOPs and checklists for consistent service delivery
    """)
    st.markdown("---")
    st.subheader("Performance Dashboard Implementation – LYROS (2024)")
    st.write("""
    - Led the implementation of an interactive performance dashboard to track team metrics (productivity, quality, adherence).
    - Enabled real-time decision-making for team leads and managers.
    - Reduced manual reporting efforts by 40%.
    """)
    st.markdown("---")
    st.subheader("Cross-Team Resource Reallocation Strategy – Wipro (2023)")
    st.write("""
    - Developed a workforce optimization plan during a high-volume project phase.
    - Successfully reallocated resources between training, support, and operations to handle demand spikes without additional hires.
    - Improved efficiency by 20% and saved INR 3 lakhs/month in manpower costs.
    """)
    st.markdown("---")
    st.subheader("WFH Transition & Policy Setup – COVID/Post-COVID Period")
    st.write("""
    - Coordinated operational shift to remote work setup for 50+ employees.
    - Established WFH guidelines, compliance trackers, and daily team sync models.
    - Maintained business continuity at 98% with zero SLA breaches.
    """)
    st.markdown("---")
    st.subheader("Quality & Compliance Initiative – Internal Audit Readiness (2022)")
    st.write("""
    - Spearheaded an internal audit readiness program focusing on process documentation, compliance training, and mock audits.
    - Improved audit scores by 30%, ensuring alignment with corporate and client expectations.
    """)
    st.markdown("---")

with tab3:
    st.header("Professional Experience")
    st.subheader("LYROS, Hyderabad, TS - Operation Manager (Feb 2024 – Present)")
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
    st.markdown("---")
    st.subheader("Wipro, Hyderabad, TS - Deputy Manager Operations (Oct 2016 – Aug 2023)")
    st.write("""
    - Led daily operations for cross-functional teams, ensuring smooth workflow, SLA adherence, and quality compliance across training and service delivery units.
    - Collaborated with training, HR, and business units to align operational strategies with organizational objectives.
    - Designed and implemented SOPs for end-to-end processes, improving task consistency and onboarding efficiency.
    - Monitored team performance using KPIs and dashboards; analyzed trends and provided actionable feedback to drive improvements.
    - Coordinated resource allocation and workload management during peak periods, optimizing staffing across functions.
    - Conducted regular internal audits and process reviews, ensuring compliance with internal quality benchmarks and client expectations.
    - Facilitated communication between leadership and team leads through structured daily stand-ups and performance syncs.
    """)
    st.markdown("---")
    st.subheader("Call health - Sr. Trainer & Team Leader (Sep 2014 - Oct 2016)")
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
    st.markdown("---")
    st.subheader("Vertex Customer Solutions Pvt ltd - Sr. Team Leader (Jun 2013 - Aug 2014)")
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
    st.markdown("---")
    st.subheader("Digicall Teleservices Pvt ltd - Sr. Team Leader (Mar 2010 - Dec-2012)")
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
    st.markdown("---")

with tab4:
    st.header("Certifications")
    st.write("""
    - Six Sigma – Yellow Belt
    - Lean Management
    - Agile Fundamentals
    - TQM (Total Quality Management)
    - PMP (In Progress)
    """)

with tab5:
    st.header("Achievements")
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

# --- SIDEBAR SECTION ---
st.sidebar.header("Personal Profile")
# Replace with a placeholder image or remove the image loading
st.sidebar.image("lalitha.jpg", width=200)
st.sidebar.write(f"**Full Name:** Lalitha Priya")
st.sidebar.write(f"**Date of Birth:** 11-09-1990")
st.sidebar.write(f"**Gender:** Female")
st.sidebar.write(f"**Religion:** Hindu")
st.sidebar.write(f"**Nationality:** Indian")
st.sidebar.write(f"**Languages Known:** Telugu, Tamil, English and Hindi")

# --- FOOTER SECTION ---
st.markdown("---")
st.write("© 2025 Lalitha Priya. All rights reserved.")