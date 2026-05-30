import streamlit as st
import requests
import os
import json

API_URL = "http://127.0.0.1:8000"

# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="AI Face Recognition",
    page_icon="🧠",
    layout="wide"
)

# ================= PREMIUM CSS ================= #

st.markdown("""
<style>

/* Background */

.stApp {
    background: linear-gradient(
        135deg,
        #141e30,
        #243b55
    );
    color: white;
}

/* Main Container */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Glass Cards */

[data-testid="stVerticalBlock"] {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    margin-bottom: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* Buttons */

.stButton > button {

    width: 100%;
    border-radius: 15px;
    height: 3em;

    background: linear-gradient(
        90deg,
        #00c6ff,
        #0072ff
    );

    color: white;
    font-size: 18px;
    font-weight: bold;

    border: none;

    transition: 0.3s;
}

.stButton > button:hover {

    transform: scale(1.03);

    box-shadow: 0 0 20px rgba(255,255,255,0.3);
}

/* Headers */

h1, h2, h3 {
    color: white;
    text-align: center;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: rgba(0,0,0,0.3);
}

/* Input Fields */

.stTextInput input {
    border-radius: 12px;
}

/* Metric Cards */

[data-testid="stMetric"] {

    background: rgba(255,255,255,0.08);

    padding: 15px;

    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ================= LOAD LOGS ================= #

logs = []

log_path = "data/activity_log.jsonl"

if os.path.exists(log_path):

    with open(log_path, "r") as f:

        for line in f:

            logs.append(json.loads(line))

# ================= SIDEBAR ================= #

st.sidebar.title("🧠 AI Dashboard")

st.sidebar.markdown("---")

# Total Users

total_users = len(os.listdir("data/embeddings"))

st.sidebar.metric(
    "👤 Registered Users",
    total_users
)

# Total Verifications

verify_count = 0
pass_count = 0

for log in logs:

    if log.get("event") == "VERIFY":

        verify_count += 1

    if log.get("decision") == "PASS":

        pass_count += 1

st.sidebar.metric(
    "🔍 Total Verifications",
    verify_count
)

st.sidebar.metric(
    "✅ Successful Matches",
    pass_count
)

st.sidebar.markdown("---")

st.sidebar.success("System Status: ONLINE")

# ================= TITLE ================= #

st.title("🧠 AI Face Recognition System")

st.markdown(
    "<h3 style='text-align:center;'> AI Verification Platform</h3>",
    unsafe_allow_html=True
)

# ================= TABS ================= #

tab1, tab2, tab3 = st.tabs([
    "📸 Enroll",
    "🔍 Verify",
    "🗑️ Delete User"
])

# ================= ENROLL ================= #

with tab1:

    st.subheader("Enroll Face")

    user_id = st.text_input(
        "Enter User ID"
    )

    enroll_method = st.radio(
        "Choose Input Method",
        ["📁 Upload Image", "📸 Live Webcam"]
    )

    image = None

    if enroll_method == "📁 Upload Image":

        image = st.file_uploader(
            "Upload Face Image",
            type=["jpg", "jpeg", "png"]
        )

    else:

        image = st.camera_input(
            "Capture Face"
        )

    if image is not None:

        st.image(image, width=250)

    if st.button("🚀 Enroll Face"):

        if image is not None and user_id != "":

            with st.spinner("🧠 AI Processing Face..."):

                response = requests.post(
                    f"{API_URL}/enroll_face",
                    files={"image": image},
                    data={"user_id": user_id}
                )

            result = response.json()

            st.markdown(
                """
                <div style="
                    background: rgba(0,255,100,0.15);
                    padding: 20px;
                    border-radius: 15px;
                    text-align: center;
                    font-size: 24px;
                    font-weight: bold;
                    color: #00ff99;
                    border: 1px solid #00ff99;
                ">
                    ✅ FACE ENROLLED SUCCESSFULLY
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.warning(
                "Please provide image and user ID"
            )

# ================= VERIFY ================= #

with tab2:

    st.subheader("Verify Face")

    verify_id = st.text_input(
        "Enter User ID to Verify"
    )

    verify_method = st.radio(
        "Choose Verification Method",
        ["📁 Upload Image", "📸 Live Webcam"],
        key="verify_method"
    )

    verify_image = None

    if verify_method == "📁 Upload Image":

        verify_image = st.file_uploader(
            "Upload Verification Image",
            type=["jpg", "jpeg", "png"],
            key="verify_upload"
        )

    else:

        verify_image = st.camera_input(
            "Capture Verification Face"
        )

    if verify_image is not None:

        st.image(verify_image, width=250)

    if st.button("🔍 Verify Face"):

        if verify_image is not None and verify_id != "":

            with st.spinner("🧠 Running AI Verification..."):

                response = requests.post(
                    f"{API_URL}/verify_face",
                    files={"image": verify_image},
                    data={"user_id": verify_id}
                )

            result = response.json()

            if "decision" in result:

                score = result["score"]

                decision = result["decision"]

                st.markdown(
                    "## AI Similarity Score"
                )

                st.progress(
                    min(score, 1.0)
                )

                st.metric(
                    label="Similarity Score",
                    value=f"{round(score * 100, 2)}%"
                )

                # PASS

                if decision == "PASS":

                    st.markdown(
                        """
                        <div style="
                            background: rgba(0,255,100,0.15);
                            padding: 20px;
                            border-radius: 15px;
                            text-align: center;
                            font-size: 28px;
                            font-weight: bold;
                            color: #00ff99;
                            border: 1px solid #00ff99;
                        ">
                            ✅ FACE VERIFIED
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                # FAIL

                elif decision == "FAIL":

                    st.markdown(
                        """
                        <div style="
                            background: rgba(255,0,0,0.12);
                            padding: 20px;
                            border-radius: 15px;
                            text-align: center;
                            font-size: 28px;
                            font-weight: bold;
                            color: #ff4d4d;
                            border: 1px solid #ff4d4d;
                        ">
                            ❌ FACE NOT MATCHED
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                # INCONCLUSIVE

                else:

                    st.markdown(
                        """
                        <div style="
                            background: rgba(255,165,0,0.12);
                            padding: 20px;
                            border-radius: 15px;
                            text-align: center;
                            font-size: 28px;
                            font-weight: bold;
                            color: orange;
                            border: 1px solid orange;
                        ">
                            ⚠️ INCONCLUSIVE RESULT
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            else:

                st.error(
                    result["error"]
                )

        else:

            st.warning(
                "Please provide image and user ID"
            )

# ================= DELETE USER ================= #

with tab3:

    st.subheader("Delete User")

    delete_id = st.text_input(
        "Enter User ID to Delete"
    )

    if st.button("🗑️ Delete User"):

        response = requests.delete(
            f"{API_URL}/delete_user/{delete_id}"
        )

        result = response.json()

        if "message" in result:

            st.success(
                result["message"]
            )

        else:

            st.error(
                result["error"]
            )