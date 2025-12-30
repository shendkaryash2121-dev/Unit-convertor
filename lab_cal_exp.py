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
# NODE COLOR THEME (Biotech)
# ======================================================
st.markdown("""
<style>
body {
    background-color: #ffffff;
}
.card {
    background: #f9fbfd;
    padding: 20px;
    border-radius: 12px;
    border-left: 6px solid #2aa198;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}
h1, h2, h3 {
    color: #073642;
}
.stButton>button {
    background-color: #268bd2;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# TITLE
# ======================================================
st.title("🧪 Biotechnology Lab Unit Converter")
st.caption("Scientific • Accurate • Laboratory-Grade")

# ======================================================
# SIDEBAR MENU
# ======================================================
tool = st.sidebar.selectbox(
    "Select Calculator",
    [
        "Mass Converter",
        "Volume Converter",
        "Dilution (C₁V₁ = C₂V₂)",
        "Molarity (from grams)",
        "Molarity ↔ Normality",
        "Percentage Solution",
        "Molality",
        "Temperature Converter",
        "Protein Concentration",
        "DNA / RNA Concentration",
        "pH Calculator",
        "Osmotic Pressure",
        "Hardy–Weinberg Equation"
    ]
)

# ======================================================
# MASS CONVERTER
# ======================================================
if tool == "Mass Converter":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("⚖️ Mass Converter")

    units = {
        "kg": 1000,
        "g": 1,
        "mg": 0.001,
        "oz": 28.35
    }

    value = st.number_input("Enter value", min_value=0.0)
    from_u = st.selectbox("From", units.keys())
    to_u = st.selectbox("To", units.keys())

    if st.button("Convert"):
        grams = value * units[from_u]
        result = grams / units[to_u]
        st.success(f"{result:.6f} {to_u}")

    st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# VOLUME CONVERTER
# ======================================================
elif tool == "Volume Converter":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧪 Volume Converter")

    units = {
        "L": 1,
        "mL": 0.001,
        "µL": 0.000001,
        "m³": 1000
    }

    value = st.number_input("Enter value", min_value=0.0)
    from_u = st.selectbox("From", units.keys())
    to_u = st.selectbox("To", units.keys())

    if st.button("Convert"):
        liters = value * units[from_u]
        result = liters / units[to_u]
        st.success(f"{result:.6f} {to_u}")

    st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# DILUTION
# ======================================================
elif tool == "Dilution (C₁V₁ = C₂V₂)":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔬 Dilution Calculator")

    C1 = st.number_input("C1", value=0.0)
    V1 = st.number_input("V1", value=0.0)
    C2 = st.number_input("C2", value=0.0)
    V2 = st.number_input("V2", value=0.0)

    if st.button("Calculate"):
        if C1 == 0:
            st.success(f"C1 = {(C2*V2)/V1}")
        elif V1 == 0:
            st.success(f"V1 = {(C2*V2)/C1}")
        elif C2 == 0:
            st.success(f"C2 = {(C1*V1)/V2}")
        elif V2 == 0:
            st.success(f"V2 = {(C1*V1)/C2}")
        else:
            st.info("All values provided")

    st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# PROTEIN CONCENTRATION
# ======================================================
elif tool == "Protein Concentration":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧬 Protein Concentration")

    A280 = st.number_input("A280", min_value=0.0)

    if st.button("Calculate"):
        protein = A280 * 1.5
        st.success(f"{protein:.3f} mg/mL")

    st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# DNA / RNA
# ======================================================
elif tool == "DNA / RNA Concentration":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧬 DNA / RNA Concentration")

    type_ = st.radio("Type", ["DNA", "RNA"])
    A260 = st.number_input("A260")
    dilution = st.number_input("Dilution Factor", value=1.0)

    if st.button("Calculate"):
        factor = 50 if type_ == "DNA" else 40
        conc = A260 * factor * dilution
        st.success(f"{conc:.2f} µg/mL")

    st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# PH
# ======================================================
elif tool == "pH Calculator":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧪 pH Calculator")

    h = st.number_input("[H⁺] (M)", min_value=0.0000000001)

    if st.button("Calculate"):
        st.success(f"pH = {-math.log10(h):.3f}")

    st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# OSMOTIC PRESSURE
# ======================================================
elif tool == "Osmotic Pressure":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧫 Osmotic Pressure")

    i = st.number_input("van’t Hoff factor (i)")
    M = st.number_input("Molarity (M)")
    T = st.number_input("Temperature (K)")

    if st.button("Calculate"):
        pi = i * M * 0.0821 * T
        st.success(f"{pi:.3f} atm")

    st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# HARDY WEINBERG
# ======================================================
elif tool == "Hardy–Weinberg Equation":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧬 Hardy–Weinberg Equation")

    p = st.number_input("Allele frequency (p)", min_value=0.0, max_value=1.0)
    q = 1 - p

    if st.button("Calculate"):
        st.write("p² =", p**2)
        st.write("2pq =", 2*p*q)
        st.write("q² =", q**2)

    st.markdown('</div>', unsafe_allow_html=True)
