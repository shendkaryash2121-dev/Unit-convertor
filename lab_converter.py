import streamlit as st
from PIL import Image
from pathlib import Path

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Biotechnology Lab Calculator",
    page_icon="🧪",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ================= SESSION STATE =================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "tool" not in st.session_state:
    st.session_state.tool = None

# ================= PROFESSIONAL THEME (DARK-BLUE SAFE) =================
st.markdown("""
<style>

/* Remove Streamlit UI */
header, footer {visibility: hidden;}
[data-testid="stToolbar"] {display: none;}

/* App background (safe for all modes) */
.stApp {
    background-color: #f4f6f9;
    display: flex;
    justify-content: center;
}

/* Main container */
.block-container {
    max-width: 900px;
    padding: 3rem 3.5rem;
    background: #ffffff;
    border-radius: 16px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.06);
}

/* ---- TITLE FIX (CRITICAL) ---- */
h1 {
    color: #0f2a44 !important;   /* deep biotech blue */
    font-weight: 800;
    letter-spacing: -0.4px;
}

/* Subheadings */
h2, h3 {
    color: #1e3a5f !important;
    font-weight: 600;
}

/* Text */
p, label {
    color: #334155 !important;
    font-size: 15px;
}

/* Buttons */
.stButton > button {
    background-color: #1e3a5f;
    color: #ffffff;
    border-radius: 10px;
    padding: 10px 24px;
    font-weight: 600;
    border: none;
}

.stButton > button:hover {
    background-color: #162c47;
    transform: translateY(-1px);
}

/* Inputs */
input, select {
    background-color: #f9fafb !important;
    border-radius: 10px !important;
    border: 1px solid #cbd5e1 !important;
    color: #0f172a !important;
}

/* Alerts */
.stAlert {
    border-radius: 10px;
}

/* Divider */
hr {
    border: none;
    border-top: 1px solid #e5e7eb;
    margin: 2rem 0;
}

</style>
""", unsafe_allow_html=True)

# ================= HOME PAGE =================
if st.session_state.page == "home":

    image_path = Path("LAB_CAL_2.png")

    if image_path.exists():
        img = Image.open(image_path)
        st.image(
            img,
            width=420,   # 🔽 smaller, professional size
        )
    else:
        st.warning("LAB_CAL_2.png not found in repository root")

    st.markdown(
        "<h1>Biotechnology Lab Calculator</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p>A professional laboratory calculator for accurate unit conversions "
        "used in biotechnology, molecular biology, and chemical laboratories.</p>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Enter Calculator"):
        st.session_state.page = "select"
        st.rerun()

# ================= TOOL SELECTION =================
elif st.session_state.page == "select":

    st.markdown("<h2>Select Calculation Type</h2>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Mass Conversion"):
            st.session_state.tool = "mass"
        if st.button("Volume Conversion"):
            st.session_state.tool = "volume"
        if st.button("C1V1 Dilution"):
            st.session_state.tool = "c1v1"
        if st.button("Molarity (from grams)"):
            st.session_state.tool = "molarity"

    with col2:
        if st.button("Molarity by Dilution"):
            st.session_state.tool = "molarity_dilution"
        if st.button("Normality"):
            st.session_state.tool = "normality"
        if st.button("Normality by Dilution"):
            st.session_state.tool = "normality_dilution"

    if st.session_state.tool:
        st.session_state.page = "calc"
        st.rerun()

# ================= CALCULATORS =================
elif st.session_state.page == "calc":

    st.button("← Back", on_click=lambda: st.session_state.update(page="select", tool=None))
    st.markdown("<hr>", unsafe_allow_html=True)

    # MASS
    if st.session_state.tool == "mass":
        st.header("Mass Conversion")

        value = st.number_input("Mass", min_value=0.0)
        from_u = st.selectbox("From unit", ["kg", "g", "mg"])
        to_u = st.selectbox("To unit", ["kg", "g", "mg"])

        factor = {"kg": 1000, "g": 1, "mg": 0.001}

        if st.button("Convert"):
            result = (value * factor[from_u]) / factor[to_u]
            st.success(f"{result:.4f} {to_u}")

    # VOLUME
    elif st.session_state.tool == "volume":
        st.header("Volume Conversion")

        value = st.number_input("Volume", min_value=0.0)
        from_u = st.selectbox("From unit", ["L", "mL", "µL"])
        to_u = st.selectbox("To unit", ["L", "mL", "µL"])

        factor = {"L": 1, "mL": 0.001, "µL": 0.000001}

        if st.button("Convert"):
            result = (value * factor[from_u]) / factor[to_u]
            st.success(f"{result:.4f} {to_u}")

    # C1V1
    elif st.session_state.tool == "c1v1":
        st.header("C1V1 = C2V2 Dilution")
        st.caption("Leave exactly ONE field empty")

        C1 = st.number_input("C1", value=None)
        V1 = st.number_input("V1", value=None)
        C2 = st.number_input("C2", value=None)
        V2 = st.number_input("V2", value=None)

        values = [C1, V1, C2, V2]

        if st.button("Calculate"):
            if values.count(None) != 1:
                st.error("Leave exactly ONE field empty")
            else:
                try:
                    if C1 is None:
                        st.success(f"C1 = {(C2*V2)/V1:.4f}")
                    elif V1 is None:
                        st.success(f"V1 = {(C2*V2)/C1:.4f}")
                    elif C2 is None:
                        st.success(f"C2 = {(C1*V1)/V2:.4f}")
                    elif V2 is None:
                        st.success(f"V2 = {(C1*V1)/C2:.4f}")
                except ZeroDivisionError:
                    st.error("Volume cannot be zero")

    # MOLARITY
    elif st.session_state.tool == "molarity":
        st.header("Molarity (from grams)")

        M = st.number_input("Molarity (M)")
        MW = st.number_input("Molecular Weight (g/mol)")
        V = st.number_input("Volume (L)")

        if st.button("Calculate"):
            grams = M * MW * V
            st.success(f"Required mass = {grams:.4f} g")

    # MOLARITY DILUTION
    elif st.session_state.tool == "molarity_dilution":
        st.header("Molarity by Dilution")

        M2 = st.number_input("Final Molarity (M)")
        V1 = st.number_input("Initial Volume")
        V2 = st.number_input("Final Volume")

        if st.button("Calculate"):
            st.success(f"Initial Molarity = {(M2*V2)/V1:.4f} M")

    # NORMALITY
    elif st.session_state.tool == "normality":
        st.header("Normality")

        M = st.number_input("Molarity (M)")
        n = st.number_input("n-factor")

        if st.button("Calculate"):
            st.success(f"Normality = {M*n:.4f} N")

    # NORMALITY DILUTION
    elif st.session_state.tool == "normality_dilution":
        st.header("Normality by Dilution")

        N2 = st.number_input("Final Normality (N)")
        V1 = st.number_input("Initial Volume")
        V2 = st.number_input("Final Volume")

        if st.button("Calculate"):
            st.success(f"Initial Normality = {(N2*V2)/V1:.4f} N")
