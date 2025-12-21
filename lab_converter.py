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

# ================= STRONG BIOTECH THEME =================
st.markdown("""
<style>

/* --- REMOVE STREAMLIT DEFAULT UI --- */
header, footer {visibility: hidden;}
[data-testid="stToolbar"] {display: none;}

/* --- APP BACKGROUND (soft lab tone) --- */
.stApp {
    background: linear-gradient(
        135deg,
        #eef3f7 0%,
        #e6edf3 100%
    );
    display: flex;
    justify-content: center;
}

/* --- MAIN CALCULATOR CARD --- */
.block-container {
    max-width: 880px;
    padding: 2.8rem 3.2rem;
    background: #f8fafc;
    border-radius: 18px;
    box-shadow: 0 18px 40px rgba(15, 42, 68, 0.12);
}

/* --- TITLES --- */
h1 {
    color: #0f2a44 !important;
    font-weight: 800;
    letter-spacing: -0.4px;
    margin-bottom: 0.3rem;
}

h2, h3 {
    color: #163a5f !important;
    font-weight: 650;
}

/* --- TEXT --- */
p, label {
    color: #334155 !important;
    font-size: 15px;
}

/* --- BUTTONS (FIXED VISIBILITY) --- */
.stButton > button {
    background: linear-gradient(
        135deg,
        #1f6f8b,
        #2a9d8f
    ) !important;
    color: #ffffff !important;
    border-radius: 12px;
    padding: 11px 26px;
    font-weight: 700;
    font-size: 15px;
    border: none;
    box-shadow: 0 10px 22px rgba(42, 157, 143, 0.35);
    transition: all 0.2s ease-in-out;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 28px rgba(42, 157, 143, 0.45);
}

/* --- INPUTS --- */
input, select {
    background-color: #ffffff !important;
    border-radius: 10px !important;
    border: 1.5px solid #94a3b8 !important;
    color: #0f172a !important;
    font-weight: 500;
}

/* --- ALERTS --- */
.stAlert {
    border-radius: 12px;
}

/* --- DIVIDER --- */
hr {
    border: none;
    border-top: 1px solid #cbd5e1;
    margin: 2rem 0;
}

</style>
""", unsafe_allow_html=True)

# ================= HOME PAGE =================
if st.session_state.page == "home":

    image_path = Path("LAB_CAL_2.png")
    if image_path.exists():
        img = Image.open(image_path)
        st.image(img, width=380)  # smaller, cleaner
    else:
        st.warning("LAB_CAL_2.png not found in repository root")

    st.markdown("<h1>Biotechnology Lab Calculator</h1>", unsafe_allow_html=True)

    st.markdown(
        "<p>Accurate, reliable laboratory calculations for biotechnology, "
        "molecular biology, and chemical research workflows.</p>",
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
            st.success(f"{(value * factor[from_u]) / factor[to_u]:.4f} {to_u}")

    # VOLUME
    elif st.session_state.tool == "volume":
        st.header("Volume Conversion")
        value = st.number_input("Volume", min_value=0.0)
        from_u = st.selectbox("From unit", ["L", "mL", "µL"])
        to_u = st.selectbox("To unit", ["L", "mL", "µL"])
        factor = {"L": 1, "mL": 0.001, "µL": 0.000001}
        if st.button("Convert"):
            st.success(f"{(value * factor[from_u]) / factor[to_u]:.4f} {to_u}")

    # C1V1
    elif st.session_state.tool == "c1v1":
        st.header("C1V1 = C2V2 Dilution")
        st.caption("Leave exactly ONE field empty")
        C1 = st.number_input("C1", value=None)
        V1 = st.number_input("V1", value=None)
        C2 = st.number_input("C2", value=None)
        V2 = st.number_input("V2", value=None)
        vals = [C1, V1, C2, V2]
        if st.button("Calculate"):
            if vals.count(None) != 1:
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
