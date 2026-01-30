import streamlit as st

st.set_page_config(page_title="Iron Lady Career Journey Advisor", layout="centered")

st.title("Iron Lady AI Leadership Journey Advisor")
st.write("A personalized leadership roadmap aligned with Iron Lady’s transformation model.")

st.markdown("## Tell us about your current career stage")

# ---------------- INPUT SECTION ---------------- #

role = st.selectbox(
    "Your Current Role",
    [
        "Select your role",
        "Individual Contributor (Engineer / Analyst)",
        "Team Lead / Supervisor",
        "Mid-Level Manager",
        "Senior Manager / Director",
        "Entrepreneur / Business Owner"
    ]
)

experience = st.slider("Years of Experience", 0, 25, 0)

income = st.selectbox(
    "Current Income Range",
    [
        "Select your income range",
        "Below 5 LPA",
        "5–10 LPA",
        "10–20 LPA",
        "20–35 LPA",
        "Above 35 LPA"
    ]
)

goal = st.selectbox(
    "Your Primary Career Goal",
    [
        "Select your goal",
        "Promotion",
        "Leadership Role",
        "Board Position",
        "Business Growth"
    ]
)

# ---------------- DECISION ENGINE ---------------- #

def generate_journey(role, experience, income, goal):

    # Determine Career Stage
    if experience <= 3:
        stage = "Emerging Leader"
    elif experience <= 8:
        stage = "Growth-Stage Leader"
    else:
        stage = "Strategic Leader"

    # Determine Program
    if goal == "Board Position":
        program = "Board Readiness Program"
    elif goal == "Business Growth":
        program = "Business Growth Program"
    elif role in ["Mid-Level Manager", "Senior Manager / Director"] or experience >= 7:
        program = "Advanced Leadership Cohort"
    else:
        program = "Leadership Essentials Program"

    # Structured Transformation Model
    journey = f"""
    ### 🛤 Your Iron Lady Leadership Journey

    *Current Career Stage:* {stage}

    #### Phase 1: Foundation Building
    Strengthening leadership mindset, confidence, and executive communication.

    #### Phase 2: Strategic Visibility
    Learning influence, negotiation, and stakeholder management through cohort-based learning.

    #### Phase 3: Leadership Expansion
    Positioning yourself for higher roles, income growth, and strategic authority.

    ---

    ### 🌟 Recommended Starting Program: {program}

    This program aligns with your experience level and goal of *{goal}*, 
    and fits Iron Lady’s structured transformation pathway.
    """

    process = """
    ### 📚 How Iron Lady’s Model Works

    - Structured cohort-based learning
    - Expert-led mentorship
    - Peer accountability network
    - Real-world leadership implementation
    - Outcome-focused transformation
    """

    next_step = "Enroll in the next cohort to begin your structured leadership transformation journey."

    return journey, process, next_step


# ---------------- OUTPUT SECTION ---------------- #

if st.button("Generate My Leadership Roadmap"):

    if (
        role == "Select your role"
        or income == "Select your income range"
        or goal == "Select your goal"
    ):
        st.warning("Please complete all fields to generate your roadmap.")
    else:
        journey, process, next_step = generate_journey(
            role, experience, income, goal
        )

        st.markdown("---")
        st.markdown(journey)
        st.markdown(process)
        st.success(next_step)
        st.markdown("---")

        st.info("This roadmap is generated based on your career stage, goals, and Iron Lady’s structured leadership model.")