import streamlit as st
import math

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Biotechnology Lab Unit Converter",
    page_icon="🧪",
    layout="centered"
)

# =========================
# CUSTOM CSS (NODE STYLE)
# =========================
st.markdown("""
<style>
body {
    background-color: #ffffff;
}
h1, h2, h3 {
    color: #1f3c88;
}
.card {
    background: #f8f9fa;
    padding: 20px;
    border-radius: 12px;
    border-left: 6px solid #17a2b8;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}
.result {
    font-size: 20px;
    color: #28a745;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🧪 Lab Tools")

tool = st.sidebar.selectbox(
    "Select Calculator",
    [
        "Mass Converter",
        "Volume Converter",
        "Molarity",
        "Molarity (Dilution)",
        "Normality (Dilution)",
        "Percentage Solution",
        "Protein Concentration",
        "DNA Concentration",
        "RNA Concentration",
        "pH Calculator",
        "Temperature Converter",
        "Osmotic Pressure",
        "Hardy–Weinberg"
    ]
)

st.title("Biotechnology Lab Unit Converter")

# =========================
# MASS CONVERTER
# =========================
if tool == "Mass Converter":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("⚖️ Mass Converter")

    units = {
        "Kilogram (kg)": 1000,
        "Gram (g)": 1,
        "Milligram (mg)": 0.001,
        "Ounce (oz)": 28.35
    }

    value = st.number_input("Enter mass value", min_value=0.0)
    from_u = st.selectbox("From", units.keys())
    to_u = st.selectbox("To", units.keys())

    if st.button("Convert"):
        grams = value * units[from_u]
        result = grams / units[to_u]
        st.markdown(f'<div class="result">{result:.6f}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# VOLUME CONVERTER
# =========================
elif tool == "Volume Converter":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧪 Volume Converter")

    units = {
        "Liter (L)": 1,
        "Milliliter (mL)": 0.001,
        "Microliter (µL)": 0.000001,
        "Cubic meter (m³)": 1000
    }

    value = st.number_input("Enter volume", min_value=0.0)
    from_u = st.selectbox("From", units.keys())
    to_u = st.selectbox("To", units.keys())

    if st.button("Convert"):
        liters = value * units[from_u]
        result = liters / units[to_u]
        st.markdown(f'<div class="result">{result:.6f}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# MOLARITY
# =========================
elif tool == "Molarity":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧬 Molarity")

    moles = st.number_input("Moles of solute", min_value=0.0)
    volume = st.number_input("Volume (Liters)", min_value=0.0)

    if st.button("Calculate"):
        M = moles / volume if volume != 0 else 0
        st.markdown(f'<div class="result">{M:.4f} M</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# PROTEIN CONCENTRATION
# =========================
elif tool == "Protein Concentration":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧫 Protein Concentration")

    st.markdown("**Formula:** Protein (mg/mL) = A280 × 1.5")

    A280 = st.number_input("Absorbance at 280 nm", min_value=0.0)

    if st.button("Calculate"):
        protein = A280 * 1.5
        st.markdown(f'<div class="result">{protein:.3f} mg/mL</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# DNA CONCENTRATION
# =========================
elif tool == "DNA Concentration":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧬 DNA Concentration")

    A260 = st.number_input("A260", min_value=0.0)
    dilution = st.number_input("Dilution Factor", min_value=1.0)

    if st.button("Calculate"):
        dna = A260 * 50 * dilution
        st.markdown(f'<div class="result">{dna:.2f} µg/mL</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# pH CALCULATOR
# =========================
elif tool == "pH Calculator":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("⚗️ pH Calculator")

    h = st.number_input("[H⁺] (M)", min_value=0.0000000001, format="%.10f")

    if st.button("Calculate"):
        pH = -math.log10(h)
        st.markdown(f'<div class="result">pH = {pH:.3f}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
