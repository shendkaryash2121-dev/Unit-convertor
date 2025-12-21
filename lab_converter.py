import streamlit as st
from PIL import Image

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Biology Lab Unit Converter",
    page_icon="🧪",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ================= SESSION STATE =================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "tool" not in st.session_state:
    st.session_state.tool = None

# ================= STYLING (PROFESSIONAL MINIMAL) =================
st.markdown("""
<style>

/* Remove Streamlit UI clutter */
header, footer {visibility: hidden;}
[data-testid="stToolbar"] {display: none;}

/* App background */
.stApp {
    background-color: #f6f8fb;
    display: flex;
    justify-content: center;
}

/* Main container */
.block-container {
    max-width: 900px;
    padding: 3rem 3.5rem;
    background: #ffffff;
    border-radius: 14px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.05);
}

/* Typography */
h1 {
    color: #1f2a44;
    font-weight: 700;
    letter-spacing: -0.5px;
}
h2, h3 {
    color: #24324d;
    font-weight: 600;
}
p, label {
    color: #4b5563;
    font-size: 15px;
}

/* Buttons */
.stButton > button {
    background-color: #24324d;
    color: white;
    border-radius: 8px;
    padding: 10px 22px;
    font-weight: 600;
    border: none;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background-color: #1b253b;
    transform: translateY(-1px);
}

/* Inputs */
input, select {
    background-color: #f9fafb !important;
    border-radius: 8px !important;
    border: 1px solid #d1d5db !important;
    color: #111827 !important;
}

/* Alerts */
.stAlert {
    border-radius: 8px;
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

    img = Image.open("/mnt/data/7daada3f-0886-420f-966e-f917784b3304.png")
    st.image(img, use_container_width=True)

    st.markdown("<h1>Biology Lab Unit Converter</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p>A precise and professional calculator for routine laboratory computations "
        "used in biology, chemistry, and life-science research.</p>",
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

    # -------- MASS --------
    if st.session_state.tool == "mass":
        st.header("Mass Conversion")

        value = st.number_input("Mass", min_value=0.0)
        from_u = st.selectbox("From unit", ["kg", "g", "mg"])
        to_u = st.selectbox("To unit", ["kg", "g", "mg"])

        factor = {"kg": 1000, "g": 1, "mg": 0.001}

        if st.button("Convert"):
            result = (value * factor[from_u]) / factor[to_u]
            st.success(f"{result:.4f} {to_u}")

    # -------- VOLUME --------
    elif st.session_state.tool == "volume":
        st.header("Volume Conversion")

        value = st.number_input("Volume", min_value=0.0)
        from_u = st.selectbox("From unit", ["L", "mL", "µL"])
        to_u = st.selectbox("To unit", ["L", "mL", "µL"])

        factor = {"L": 1, "mL": 0.001, "µL": 0.000001}

        if st.button("Convert"):
            result = (value * factor[from_u]) / factor[to_u]
            st.success(f"{result:.4f} {to_u}")

    # -------- C1V1 --------
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

    # -------- MOLARITY --------
    elif st.session_state.tool == "molarity":
        st.header("Molarity (from grams)")

        M = st.number_input("Molarity (M)")
        MW = st.number_input("Molecular Weight (g/mol)")
        V = st.number_input("Volume (L)")

        if st.button("Calculate"):
            grams = M * MW * V
            st.success(f"Required mass = {grams:.4f} g")

    # -------- MOLARITY DILUTION --------
    elif st.session_state.tool == "molarity_dilution":
        st.header("Molarity by Dilution")

        M2 = st.number_input("Final Molarity (M)")
        V1 = st.number_input("Initial Volume")
        V2 = st.number_input("Final Volume")

        if st.button("Calculate"):
            st.success(f"Initial Molarity = {(M2*V2)/V1:.4f} M")

    # -------- NORMALITY --------
    elif st.session_state.tool == "normality":
        st.header("Normality")

        M = st.number_input("Molarity (M)")
        n = st.number_input("n-factor")

        if st.button("Calculate"):
            st.success(f"Normality = {M*n:.4f} N")

    # -------- NORMALITY DILUTION --------
    elif st.session_state.tool == "normality_dilution":
        st.header("Normality by Dilution")

        N2 = st.number_input("Final Normality (N)")
        V1 = st.number_input("Initial Volume")
        V2 = st.number_input("Final Volume")

        if st.button("Calculate"):
            st.success(f"Initial Normality = {(N2*V2)/V1:.4f} N")
