import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Iron Lady Internal Dashboard", layout="wide")

# ---------------- DATABASE CONNECTION ---------------- #

conn = sqlite3.connect("ironlady.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS learners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT,
    cohort TEXT,
    mentor TEXT,
    goal TEXT,
    progress TEXT
)
""")
conn.commit()

# ---------------- HEADER ---------------- #

st.title("Iron Lady Cohort & Transformation Management System")
st.write(
    "Internal dashboard to manage cohort-based programs, mentor assignments, "
    "and leadership transformation tracking."
)

menu = st.sidebar.selectbox(
    "Select Operation",
    ["Add Learner", "View Learners", "Update Progress", "Delete Learner"]
)

# =====================================================
# CREATE
# =====================================================

if menu == "Add Learner":

    st.subheader("Add New Learner to Cohort")

    with st.form("add_form"):

        name = st.text_input("Learner Name")

        role = st.selectbox("Current Role", [
            "Individual Contributor",
            "Team Lead",
            "Mid-Level Manager",
            "Senior Manager / Director",
            "Entrepreneur"
        ])

        cohort = st.selectbox("Select Cohort", [
            "Leadership Essentials – Jan 2026",
            "Advanced Leadership Cohort – Mar 2026",
            "Board Readiness – Q2 2026",
            "Business Growth Accelerator – 2026"
        ])

        mentor = st.text_input("Assigned Mentor")

        goal = st.selectbox("Leadership Goal", [
            "Promotion",
            "Leadership Role",
            "Board Position",
            "Business Growth"
        ])

        progress = st.selectbox("Progress Stage", [
            "Enrolled",
            "In Progress",
            "Completed"
        ])

        submitted = st.form_submit_button("Add Learner")

        if submitted:
            if name and mentor:
                c.execute("""
                    INSERT INTO learners (name, role, cohort, mentor, goal, progress)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (name, role, cohort, mentor, goal, progress))
                conn.commit()
                st.success("Learner successfully added to cohort.")
                st.rerun()
            else:
                st.warning("Please fill required fields.")

# =====================================================
# READ
# =====================================================

elif menu == "View Learners":

    st.subheader("Cohort Overview")

    c.execute("SELECT * FROM learners")
    data = c.fetchall()

    if data:
        df = pd.DataFrame(data, columns=[
            "ID", "Name", "Role", "Cohort", "Mentor", "Goal", "Progress"
        ])

        st.dataframe(df, use_container_width=True, hide_index=True)

        # Operational Metrics
        st.markdown("### Operational Insights")

        total = len(df)
        in_progress = len(df[df["Progress"] == "In Progress"])
        completed = len(df[df["Progress"] == "Completed"])

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Learners", total)
        col2.metric("In Progress", in_progress)
        col3.metric("Completed", completed)

    else:
        st.info("No learners found in the system.")

# =====================================================
# UPDATE
# =====================================================

elif menu == "Update Progress":

    st.subheader("Update Learner Progress")

    c.execute("SELECT id, name, progress FROM learners")
    records = c.fetchall()

    if records:
        df = pd.DataFrame(records, columns=["ID", "Name", "Current Progress"])
        st.dataframe(df, use_container_width=True, hide_index=True)

        learner_id = st.number_input("Enter Learner ID", min_value=1, step=1)

        new_progress = st.selectbox("New Progress Status", [
            "Enrolled",
            "In Progress",
            "Completed"
        ])

        if st.button("Update Progress"):
            c.execute("UPDATE learners SET progress=? WHERE id=?", (new_progress, learner_id))
            conn.commit()
            st.success("Progress updated successfully.")
            st.rerun()
    else:
        st.info("No learners available to update.")

# =====================================================
# DELETE
# =====================================================

elif menu == "Delete Learner":

    st.subheader("Remove Learner from Cohort")

    c.execute("SELECT id, name FROM learners")
    records = c.fetchall()

    if records:
        df = pd.DataFrame(records, columns=["ID", "Name"])
        st.dataframe(df, use_container_width=True, hide_index=True)

        learner_id = st.number_input("Enter Learner ID to Delete", min_value=1, step=1)

        if st.button("Delete Learner"):
            c.execute("DELETE FROM learners WHERE id=?", (learner_id,))
            conn.commit()
            st.success("Learner removed successfully.")
            st.rerun()
    else:
        st.info("No learners available to delete.")