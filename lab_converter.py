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

# ---------------- STYLING + ANIMATION ----------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #0f2027, #203a43, #2c5364);
    overflow: hidden;
}

h1, h2, h3, p, label {
    color: #e0f7fa !important;
}

.stButton > button {
    background-color: #00acc1;
    color: black;
    border-radius: 14px;
    font-size: 16px;
    padding: 10px 22px;
}

.card {
    background-color: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# =========================
# PAGE 1 — WELCOME
# =========================
if st.session_state.page == "welcome":

    st.markdown("<h1 style='text-align:center;'>🧪 Laboratory Calculator</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Biology • Chemistry • Lab Calculations</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Mass • Volume • Concentration • Molarity • Normality</p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Get Started"):
        st.session_state.page = "selection"
        st.rerun()

# =========================
# PAGE 2 — SELECTION PAGE
# =========================
elif st.session_state.page == "selection":

    st.markdown("<h2 style='text-align:center;'>🔬 Available Conversions</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>We provide 7 laboratory conversion tools</p>", unsafe_allow_html=True)

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
# PAGE 3 — CALCULATOR PAGE
# =========================
elif st.session_state.page == "calculator":

    st.button("⬅ Back", on_click=lambda: st.session_state.update(page="selection", tool=None))

    # -------- MASS --------
    if st.session_state.tool == "mass":
        st.header("⚖️ Mass Converter")
        value = st.number_input("Mass", min_value=0.0)
        from_u = st.selectbox("From", ["kg", "g", "mg", "oz"])
        to_u = st.selectbox("To", ["kg", "g", "mg", "oz"])
        factor = {"kg":1000, "g":1, "mg":0.001, "oz":28.35}

        if st.button("Convert"):
            st.success((value * factor[from_u]) / factor[to_u])

    # -------- VOLUME --------
    elif st.session_state.tool == "volume":
        st.header("🧴 Volume Converter")
        value = st.number_input("Volume", min_value=0.0)
        from_u = st.selectbox("From", ["L", "mL", "µL", "m³"])
        to_u = st.selectbox("To", ["L", "mL", "µL", "m³"])
        factor = {"L":1, "mL":0.001, "µL":0.000001, "m³":1000}

        if st.button("Convert"):
            st.success((value * factor[from_u]) / factor[to_u])

    # -------- CONCENTRATION --------
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

    # -------- MOLARITY --------
    elif st.session_state.tool == "molarity":
        st.header("🧫 Molarity (grams)")
        M = st.number_input("Molarity (M)")
        MW = st.number_input("Molecular Weight")
        V = st.number_input("Volume (L)")
        if st.button("Calculate"):
            st.success(M * MW * V)

    # -------- MOLARITY DILUTION --------
    elif st.session_state.tool == "molarity_dilution":
        st.header("📘 Molarity by Dilution")
        M2 = st.number_input("Final Molarity")
        V1 = st.number_input("Initial Volume")
        V2 = st.number_input("Final Volume")
        if st.button("Calculate"):
            st.success((M2 * V2) / V1)

    # -------- NORMALITY --------
    elif st.session_state.tool == "normality":
        st.header("📗 Normality")
        M = st.number_input("Molarity")
        n = st.number_input("n-factor")
        if st.button("Calculate"):
            st.success(M * n)

    # -------- NORMALITY DILUTION --------
    elif st.session_state.tool == "normality_dilution":
        st.header("⚗️ Normality by Dilution")
        V1 = st.number_input("Initial Volume")
        N2 = st.number_input("Final Normality")
        V2 = st.number_input("Final Volume")
        if st.button("Calculate"):
            st.success((N2 * V2) / V1)
