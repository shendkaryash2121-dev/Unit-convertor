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
# MODERN UI CSS
# ======================================================
st.markdown("""
<style>

/* Global background */
body {
    background-color: #F8FAFC;
    font-family: 'Inter', sans-serif;
}

/* Card container */
.card {
    background: #FFFFFF;
    padding: 26px;
    border-radius: 20px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.06);
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

/* Result box */
.result {
    background: linear-gradient(135deg, #2563EB, #14B8A6);
    color: white;
    padding: 18px;
    border-radius: 16px;
    font-size: 1.3rem;
    font-weight: 700;
    text-align: center;
    margin-top: 15px;
}

/* Sidebar */
.sidebar-title {
    font-size: 1.6rem;
    font-weight: 800;
    color: #2563EB;
    margin-bottom: 10px;
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

page = st.sidebar.radio("Navigation", ["🏠 Home", "🧮 Calculators"])

# ======================================================
# HOME PAGE
# ======================================================
if page == "🏠 Home":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title">🧬 Biotechnology Lab Unit Converter</div>', unsafe_allow_html=True)
    st.markdown(
        "<p class='subtitle'>A modern laboratory calculator for Chemistry, Biotechnology & Molecular Biology.</p>",
        unsafe_allow_html=True
    )

    st.markdown("""
### 🔬 Features
- ⚖️ Unit conversions
- ⚗️ Solution chemistry formulas
- 📘 Physical chemistry tools
- 🧬 Biomolecular calculations
- 🧬 Genetics equations

### 👩‍🔬 Designed for
Students • Researchers • Lab Professionals

### 🚀 How to use
Open **Calculators** from sidebar → choose category → calculate instantly.
""")
    st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# CALCULATORS
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

        tool = st.selectbox("Tool", ["Mass", "Volume", "Temperature"])

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
                if vals.count("") != 1:
                    st.error("Leave exactly ONE value empty")
                else:
                    C1 = float(C1) if C1 else None
                    V1 = float(V1) if V1 else None
                    C2 = float(C2) if C2 else None
                    V2 = float(V2) if V2 else None

                    result = (
                        (C2*V2)/V1 if C1 is None else
                        (C2*V2)/C1 if V1 is None else
                        (C1*V1)/V2 if C2 is None else
                        (C1*V1)/C2
                    )

                    st.markdown(f"<div class='result'>{result}</div>", unsafe_allow_html=True)

        elif tool == "Molarity (grams)":
            col1, col2, col3 = st.columns(3)
            with col1:
                M = st.number_input("Molarity (M)")
            with col2:
                MW = st.number_input("Molecular Weight (g/mol)")
            with col3:
                V = st.number_input("Volume (L)")

            if st.button("Calculate"):
                st.markdown(f"<div class='result'>{M*MW*V:.4f} g</div>", unsafe_allow_html=True)

        elif tool == "Molarity → Normality":
            M = st.number_input("Molarity")
            n = st.number_input("n-factor")
            if st.button("Convert"):
                st.markdown(f"<div class='result'>{M*n}</div>", unsafe_allow_html=True)

        elif tool == "Molality":
            moles = st.number_input("Moles of solute")
            kg = st.number_input("Mass of solvent (kg)")
            if st.button("Calculate"):
                st.markdown(f"<div class='result'>{moles/kg}</div>", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # ======================================================
    # PHYSICAL CHEMISTRY
    # ======================================================
    elif category == "Physical Chemistry":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📘 Physical Chemistry")

        tool = st.selectbox("Tool", ["pH", "Density", "Osmotic Pressure"])

        if tool == "pH":
            h = st.number_input("[H⁺] (M)")
            if st.button("Calculate"):
                st.markdown(f"<div class='result'>{-math.log10(h):.3f}</div>", unsafe_allow_html=True)

        elif tool == "Density":
            m = st.number_input("Mass")
            v = st.number_input("Volume")
            if st.button("Calculate"):
                st.markdown(f"<div class='result'>{m/v}</div>", unsafe_allow_html=True)

        elif tool == "Osmotic Pressure":
            i = st.number_input("van't Hoff factor")
            M = st.number_input("Molarity")
            T = st.number_input("Temperature (K)")
            if st.button("Calculate"):
                st.markdown(f"<div class='result'>{i*M*0.0821*T:.3f} atm</div>", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # ======================================================
    # BIOMOLECULAR
    # ======================================================
    elif category == "Biomolecular Calculations":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🧬 Biomolecular Calculations")

        tool = st.selectbox("Tool", ["Protein", "DNA", "RNA", "DNA Purity"])

        if tool == "Protein":
            A280 = st.number_input("A280")
            if st.button("Calculate"):
                st.markdown(f"<div class='result'>{A280*1.5:.3f} mg/mL</div>", unsafe_allow_html=True)

        elif tool == "DNA":
            A260 = st.number_input("A260")
            d = st.number_input("Dilution factor")
            if st.button("Calculate"):
                st.markdown(f"<div class='result'>{A260*50*d} µg/mL</div>", unsafe_allow_html=True)

        elif tool == "RNA":
            A260 = st.number_input("A260")
            d = st.number_input("Dilution factor")
            if st.button("Calculate"):
                st.markdown(f"<div class='result'>{A260*40*d} µg/mL</div>", unsafe_allow_html=True)

        elif tool == "DNA Purity":
            A260 = st.number_input("A260")
            A280 = st.number_input("A280")
            if st.button("Calculate"):
                st.markdown(f"<div class='result'>{A260/A280:.2f}</div>", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # ======================================================
    # GENETICS
    # ======================================================
    elif category == "Genetics":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🧬 Genetics – Hardy Weinberg")

        p = st.number_input("Allele frequency (p)", min_value=0.0, max_value=1.0)
        q = 1 - p

        st.markdown(
            f"<div class='result'>p² = {p**2:.3f} | 2pq = {2*p*q:.3f} | q² = {q**2:.3f}</div>",
            unsafe_allow_html=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# FOOTER
# ======================================================
st.markdown("""
<hr>
<center style="color:#64748B;">
🧪 Biotechnology Lab Unit Converter<br>
Built for Students & Researchers
</center>
""", unsafe_allow_html=True)
