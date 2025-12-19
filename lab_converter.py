import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Lab Calculator",
    page_icon="🧪",
    layout="centered"
)

# ---------------- SESSION STATES ----------------
if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "tool" not in st.session_state:
    st.session_state.tool = None

# ---------------- STYLING (PEACOCK THEME) ----------------
st.markdown("""
<style>

/* ===== BACKGROUND ===== */
.stApp {
    background:
        radial-gradient(circle at top right, rgba(0,220,200,0.35), transparent 45%),
        radial-gradient(circle at bottom left, rgba(0,140,180,0.35), transparent 50%),
        linear-gradient(180deg, #0f3d3e 0%, #145c5d 45%, #1b7f7a 100%);
    overflow: hidden;
}

/* ===== TEXT ===== */
h1, h2, h3, p, label {
    color: #eaffff !important;
    font-weight: 600;
}

/* ===== BUTTONS ===== */
.stButton > button {
    background: linear-gradient(135deg, #00e5c0, #00bfa5);
    color: #083737;
    border-radius: 20px;
    font-size: 16px;
    font-weight: 700;
    padding: 12px 30px;
    border: none;
    box-shadow: 0 12px 30px rgba(0,229,192,0.45);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 0 18px 40px rgba(0,229,192,0.65);
}

/* ===== INPUTS ===== */
input, select {
    background-color: rgba(255,255,255,0.18) !important;
    color: #eaffff !important;
    border-radius: 14px !important;
    border: 1px solid rgba(0,229,192,0.6) !important;
    font-weight: 600;
}

/* ===== ALERTS ===== */
.stAlert {
    background-color: rgba(255,255,255,0.15);
    border-left: 5px solid #00e5c0;
}

/* ===== CARD EFFECT ===== */
.block-container {
    background: rgba(255,255,255,0.12);
    padding: 25px;
    border-radius: 24px;
    box-shadow: 0 30px 70px rgba(0,0,0,0.28);
}
</style>
""", unsafe_allow_html=True)

# =========================
# PAGE 1 — WELCOME
# =========================
if st.session_state.page == "welcome":

    st.markdown("<h1 style='text-align:center;'>🧪 Laboratory Calculator</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Biology • Chemistry • Lab Calculations</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Fast • Accurate • Scientific</p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Get Started"):
        st.session_state.page = "selection"
        st.rerun()

# =========================
# PAGE 2 — SELECTION
# =========================
elif st.session_state.page == "selection":

    st.markdown("<h2 style='text-align:center;'>🔬 Available Conversions</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Choose any laboratory calculation tool</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⚖️ Mass Converter"):
            st.session_state.tool = "mass"
        if st.button("🧴 Volume Converter"):
            st.session_state.tool = "volume"
        if st.button("🧪 Concentration (C1V1)"):
            st.session_state.tool = "concentration"
        if st.button("🧫 Molarity (Grams)"):
            st.session_state.tool = "molarity"

    with col2:
        if st.button("📘 Molarity by Dilution"):
            st.session_state.tool = "molarity_dilution"
        if st.button("📗 Normality"):
            st.session_state.tool = "normality"
        if st.button("⚗️ Normality by Dilution"):
            st.session_state.tool = "normality_dilution"

    if st.session_state.tool:
        st.session_state.page = "calculator"
        st.rerun()

# =========================
# PAGE 3 — CALCULATORS
# =========================
elif st.session_state.page == "calculator":

    st.button("⬅ Back", on_click=lambda: st.session_state.update(page="selection", tool=None))

    if st.session_state.tool == "mass":
        st.header("⚖️ Mass Converter")
        value = st.number_input("Mass", min_value=0.0)
        from_u = st.selectbox("From", ["kg", "g", "mg", "oz"])
        to_u = st.selectbox("To", ["kg", "g", "mg", "oz"])
        factor = {"kg":1000, "g":1, "mg":0.001, "oz":28.35}
        if st.button("Convert"):
            st.success((value * factor[from_u]) / factor[to_u])

    elif st.session_state.tool == "volume":
        st.header("🧴 Volume Converter")
        value = st.number_input("Volume", min_value=0.0)
        from_u = st.selectbox("From", ["L", "mL", "µL", "m³"])
        to_u = st.selectbox("To", ["L", "mL", "µL", "m³"])
        factor = {"L":1, "mL":0.001, "µL":0.000001, "m³":1000}
        if st.button("Convert"):
            st.success((value * factor[from_u]) / factor[to_u])

    elif st.session_state.tool == "concentration":
        st.header("🧪 Concentration (C1V1 = C2V2)")
        C1 = st.text_input("C1")
        V1 = st.text_input("V1")
        C2 = st.text_input("C2")
        V2 = st.text_input("V2")
        if st.button("Calculate"):
            vals = [C1, V1, C2, V2]
            if vals.count("") != 1:
                st.error("Leave exactly ONE blank")
            else:
                if C1 == "":
                    st.success((float(C2)*float(V2))/float(V1))
                elif V1 == "":
                    st.success((float(C2)*float(V2))/float(C1))
                elif C2 == "":
                    st.success((float(C1)*float(V1))/float(V2))
                elif V2 == "":
                    st.success((float(C1)*float(V1))/float(C2))

    elif st.session_state.tool == "molarity":
        st.header("🧫 Molarity (grams)")
        M = st.number_input("Molarity (M)")
        MW = st.number_input("Molecular Weight")
        V = st.number_input("Volume (L)")
        if st.button("Calculate"):
            st.success(M * MW * V)

    elif st.session_state.tool == "molarity_dilution":
        st.header("📘 Molarity by Dilution")
        M2 = st.number_input("Final Molarity")
        V1 = st.number_input("Initial Volume")
        V2 = st.number_input("Final Volume")
        if st.button("Calculate"):
            st.success((M2 * V2) / V1)

    elif st.session_state.tool == "normality":
        st.header("📗 Normality")
        M = st.number_input("Molarity")
        n = st.number_input("n-factor")
        if st.button("Calculate"):
            st.success(M * n)

    elif st.session_state.tool == "normality_dilution":
        st.header("⚗️ Normality by Dilution")
        V1 = st.number_input("Initial Volume")
        N2 = st.number_input("Final Normality")
        V2 = st.number_input("Final Volume")
        if st.button("Calculate"):
            st.success((N2 * V2) / V1)
