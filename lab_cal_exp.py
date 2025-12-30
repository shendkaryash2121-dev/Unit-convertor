import streamlit as st
import math

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="Biotechnology Lab Unit Converter",
    page_icon="🧪",
    layout="centered"
)

# ======================================================
# MODERN BIOTECH UI CSS
# ======================================================
st.markdown("""
<style>

/* Global */
body {
    background-color: #F8FAFC;
    font-family: 'Inter', sans-serif;
}

/* Card */
.card {
    background: #FFFFFF;
    padding: 26px;
    border-radius: 20px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.05);
    margin-bottom: 25px;
    border: 1px solid #E5E7EB;
}

/* Titles */
.title {
    font-size: 2.4rem;
    font-weight: 800;
    color: #0F172A;
}
.subtitle {
    color: #64748B;
    font-size: 1rem;
}

/* Results */
.result {
    background: linear-gradient(135deg, #2563EB, #14B8A6);
    color: white;
    padding: 18px;
    border-radius: 16px;
    font-size: 1.3rem;
    font-weight: 700;
    text-align: center;
    margin-top: 14px;
}

/* Sidebar */
.sidebar-title {
    font-size: 1.6rem;
    font-weight: 800;
    color: #2563EB;
}

/* Inputs */
div[data-baseweb="input"] input,
div[data-baseweb="select"] {
    border-radius: 12px !important;
}

/* Buttons */
button[kind="primary"] {
    background: linear-gradient(135deg, #2563EB, #14B8A6);
    border-radius: 14px;
    font-weight: 700;
}
button:hover {
    transform: scale(1.02);
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# SIDEBAR
# ======================================================
st.sidebar.markdown('<div class="sidebar-title">🧪 Lab Calculator</div>', unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🧮 Calculators"]
)

# ======================================================
# HOME PAGE
# ======================================================
if page == "🏠 Home":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title">🧬 Biotechnology Lab Unit Converter</div>', unsafe_allow_html=True)
    st.markdown(
        "<p class='subtitle'>Modern scientific calculator for chemistry, biotechnology & molecular biology labs.</p>",
        unsafe_allow_html=True
    )

    st.markdown("""
### 🔬 Features
- ⚖️ Unit conversions
- ⚗️ Solution chemistry formulas
- 📘 Physical chemistry tools
- 🧬 Biomolecular calculations
- 🧬 Genetics equations

### 👩‍🔬 Designed For
Students • Researchers • Laboratory Professionals

### 🚀 How to Use
Use the sidebar → open **Calculators** → select category → calculate instantly.
""")
    st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# CALCULATORS PAGE
# ======================================================
elif page == "🧮 Calculators":

    category = st.selectbox(
        "📂 Select Category",
        [
            "Basic Unit Conversions",
            "Solution Chemistry",
            "Physical Chemistry",
            "Biomolecular Calculations",
            "Genetics"
        ]
    )

    # ======================================================
    # BASIC UNIT CONVERSIONS
    # ======================================================
    if category == "Basic Unit Conversions":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("⚖️ Unit Conversions")

        tool = st.selectbox("Select Tool", ["Mass", "Volume", "Temperature"])

        if tool == "Mass":
            col1, col2, col3 = st.columns(3)
            with col1:
                value = st.number_input("Value", min_value=0.0)
            with col2:
                f = st.selectbox("From", ["kg", "g", "mg", "oz"])
            with col3:
                t = st.selectbox("To", ["kg", "g", "mg", "oz"])

            factor = {"kg":1000, "g":1, "mg":0.001, "oz":28.35}

            if st.button("Convert"):
                result = value * factor[f] / factor[t]
                st.markdown(f"<div class='result'>{result:.4f} {t}</div>", unsafe_allow_html=True)

        elif tool == "Volume":
            col1, col2, col3 = st.columns(3)
            with col1:
                value = st.number_input("Value", min_value=0.0)
            with col2:
                f = st.selectbox("From", ["L", "mL", "µL", "m³"])
            with col3:
                t = st.selectbox("To", ["L", "mL", "µL", "m³"])

            factor = {"L":1, "mL":0.001, "µL":1e-6, "m³":1000}

            if st.button("Convert"):
                result = value * factor[f] / factor[t]
                st.markdown(f"<div class='result'>{result:.6f} {t}</div>", unsafe_allow_html=True)

        elif tool == "Temperature":
            temp = st.number_input("Temperature")
            option = st.selectbox("Conversion", ["C → K", "K → C", "C → F", "F → C"])

            if st.button("Convert"):
                if option == "C → K":
                    result = temp + 273.15
                elif option == "K → C":
                    result = temp - 273.15
                elif option == "C → F":
                    result = temp * 9/5 + 32
                else:
                    result = (temp - 32) * 5/9

                st.markdown(f"<div class='result'>{result:.2f}</div>", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # ======================================================
    # SOLUTION CHEMISTRY
    # ======================================================
    elif category == "Solution Chemistry":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("⚗️ Solution Chemistry")

        tool = st.selectbox("Tool", ["C1V1 = C2V2", "Molarity (grams)", "Molarity → Normality", "Molality"])

        if tool == "C1V1 = C2V2":
            col1, col2 = st.columns(2)
            with col1:
                C1 = st.text_input("C1")
                V1 = st.text_input("V1")
            with col2:
                C2 = st.text_input("C2")
                V2 = st.text_input("V2")

            if st.button("Calculate"):
                vals = [C1, V1, C2, V2]
                if vals.
