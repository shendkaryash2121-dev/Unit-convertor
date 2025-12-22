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

# ================= BIOTECH THEME =================
st.markdown("""
<style>
header, footer {visibility: hidden;}
[data-testid="stToolbar"] {display: none;}

.stApp {
    background: linear-gradient(135deg, #eef3f7, #e6edf3);
    display: flex;
    justify-content: center;
}

.block-container {
    max-width: 900px;
    padding: 2.8rem 3.2rem;
    background: #f8fafc;
    border-radius: 18px;
    box-shadow: 0 18px 40px rgba(15,42,68,0.12);
}

h1 {
    color: #0f2a44 !important;
    font-weight: 800;
}

h2, h3 {
    color: #163a5f !important;
    font-weight: 650;
}

p, label {
    color: #334155 !important;
    font-size: 15px;
}

.stButton > button {
    background: linear-gradient(135deg, #1f6f8b, #2a9d8f) !important;
    color: white !important;
    border-radius: 12px;
    padding: 11px 26px;
    font-weight: 700;
    border: none;
    box-shadow: 0 10px 22px rgba(42,157,143,0.35);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 28px rgba(42,157,143,0.45);
}

input, select {
    background: white !important;
    border-radius: 10px !important;
    border: 1.5px solid #94a3b8 !important;
    color: #0f172a !important;
}

hr {
    border-top: 1px solid #cbd5e1;
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

# ================= HOME =================
if st.session_state.page == "home":

    image_path = Path("LAB_CAL_2.png")
    if image_path.exists():
        st.image(Image.open(image_path), width=380)

    st.markdown("<h1>Biotechnology Lab Calculator</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p>Accurate laboratory calculations for biotechnology, molecular biology "
        "and chemical research.</p>",
        unsafe_allow_html=True
    )

    if st.button("Enter Calculator"):
        st.session_state.page = "select"
        st.rerun()

# ================= SELECTION =================
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
        if st.button("Molarity (grams)"):
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
        from_u = st.selectbox("From", ["kg", "g", "mg"])
        to_u = st.selectbox("To", ["kg", "g", "mg"])
        factor = {"kg":1000, "g":1, "mg":0.001}
        if st.button("Convert"):
            st.success(f"{(value*factor[from_u])/factor[to_u]:.4f} {to_u}")

    # VOLUME
    elif st.session_state.tool == "volume":
        st.header("Volume Conversion")
        value = st.number_input("Volume", min_value=0.0)
        from_u = st.selectbox("From", ["L", "mL", "µL"])
        to_u = st.selectbox("To", ["L", "mL", "µL"])
        factor = {"L":1, "mL":0.001, "µL":0.000001}
        if st.button("Convert"):
            st.success(f"{(value*factor[from_u])/factor[to_u]:.4f} {to_u}")

    # C1V1
    elif st.session_state.tool == "c1v1":
        st.header("C1V1 = C2V2")
        st.caption("Leave exactly one field empty")
        C1 = st.number_input("C1", value=None)
        V1 = st.number_input("V1", value=None)
        C2 = st.number_input("C2", value=None)
        V2 = st.number_input("V2", value=None)
        vals = [C1, V1, C2, V2]
        if st.button("Calculate"):
            if vals.count(None) != 1:
                st.error("Leave exactly one field empty")
            else:
                try:
                    if C1 is None: st.success(f"C1 = {(C2*V2)/V1:.4f}")
                    elif V1 is None: st.success(f"V1 = {(C2*V2)/C1:.4f}")
                    elif C2 is None: st.success(f"C2 = {(C1*V1)/V2:.4f}")
                    elif V2 is None: st.success(f"V2 = {(C1*V1)/C2:.4f}")
                except ZeroDivisionError:
                    st.error("Division by zero error")

    # MOLARITY
    elif st.session_state.tool == "molarity":
        st.header("Molarity from Grams")
        M = st.number_input("Molarity (M)")
        MW = st.number_input("Molecular Weight (g/mol)")
        V = st.number_input("Volume (L)")
        if st.button("Calculate"):
            st.success(f"Required mass = {M*MW*V:.4f} g")

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
