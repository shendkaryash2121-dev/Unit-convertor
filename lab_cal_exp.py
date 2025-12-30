import streamlit as st
import math

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Biotechnology Laboratory Calculator",
    layout="wide"
)

# --------------------------------------------------
# PROFESSIONAL LAB CSS
# --------------------------------------------------
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-family: "Segoe UI", sans-serif;
    background-color: #f4f6f8;
}
header {visibility: hidden;}
.lab-panel {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 4px;
    border-left: 4px solid #008080;
}
h1, h2, h3 { color: #1f2d3d; }
.stButton > button {
    background-color: #008080;
    color: white;
    border-radius: 3px;
    border: none;
    padding: 8px 18px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("Biotechnology Laboratory Calculator")
st.caption("Accurate scientific calculations for biotechnology & life science labs")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
tool = st.sidebar.radio(
    "Calculators",
    [
        "Mass",
        "Volume",
        "Dilution",
        "Molarity",
        "Normality",
        "Molality",
        "Percentage Solutions",
        "Protein",
        "DNA / RNA",
        "pH",
        "Osmotic Pressure",
        "Hardy–Weinberg"
    ]
)

st.markdown('<div class="lab-panel">', unsafe_allow_html=True)

# --------------------------------------------------
# MASS
# --------------------------------------------------
if tool == "Mass":
    st.subheader("Mass Conversion")
    units = {"kg":1000, "g":1, "mg":0.001, "oz":28.35}
    value = st.number_input("Value", min_value=0.0)
    from_u = st.selectbox("From unit", units.keys())
    to_u = st.selectbox("To unit", units.keys())
    if st.button("Calculate"):
        st.write("Result:", (value * units[from_u]) / units[to_u], to_u)

# --------------------------------------------------
# VOLUME
# --------------------------------------------------
elif tool == "Volume":
    st.subheader("Volume Conversion")
    units = {"L":1, "mL":0.001, "µL":0.000001, "m³":1000}
    value = st.number_input("Value", min_value=0.0)
    from_u = st.selectbox("From unit", units.keys())
    to_u = st.selectbox("To unit", units.keys())
    if st.button("Calculate"):
        st.write("Result:", (value * units[from_u]) / units[to_u], to_u)

# --------------------------------------------------
# DILUTION
# --------------------------------------------------
elif tool == "Dilution":
    st.subheader("Dilution (C₁V₁ = C₂V₂)")
    c1 = st.number_input("C₁", value=0.0)
    v1 = st.number_input("V₁", value=0.0)
    c2 = st.number_input("C₂", value=0.0)
    v2 = st.number_input("V₂", value=0.0)
    if st.button("Calculate"):
        if c1 == 0: st.write("C₁ =", (c2*v2)/v1)
        elif v1 == 0: st.write("V₁ =", (c2*v2)/c1)
        elif c2 == 0: st.write("C₂ =", (c1*v1)/v2)
        elif v2 == 0: st.write("V₂ =", (c1*v1)/c2)

# --------------------------------------------------
# MOLARITY
# --------------------------------------------------
elif tool == "Molarity":
    st.subheader("Molarity (M)")
    moles = st.number_input("Moles of solute (mol)")
    volume = st.number_input("Volume of solution (L)")
    if st.button("Calculate"):
        st.write("Molarity (M) =", moles / volume)

# --------------------------------------------------
# NORMALITY
# --------------------------------------------------
elif tool == "Normality":
    st.subheader("Normality (N)")
    gram_eq = st.number_input("Gram equivalents")
    volume = st.number_input("Volume of solution (L)")
    if st.button("Calculate"):
        st.write("Normality (N) =", gram_eq / volume)

# --------------------------------------------------
# MOLALITY
# --------------------------------------------------
elif tool == "Molality":
    st.subheader("Molality (m)")
    moles = st.number_input("Moles of solute (mol)")
    kg = st.number_input("Mass of solvent (kg)")
    if st.button("Calculate"):
        st.write("Molality (m) =", moles / kg)

# --------------------------------------------------
# PERCENTAGE
# --------------------------------------------------
elif tool == "Percentage Solutions":
    st.subheader("Percentage Solutions")
    type_ = st.selectbox("Type", ["%(w/v)", "%(v/v)", "%(m/v)"])
    a = st.number_input("Solute amount")
    b = st.number_input("Solution amount")
    if st.button("Calculate"):
        st.write("Percentage =", (a / b) * 100, "%")

# --------------------------------------------------
# PROTEIN
# --------------------------------------------------
elif tool == "Protein":
    st.subheader("Protein Concentration")
    a280 = st.number_input("A280", min_value=0.0)
    if st.button("Calculate"):
        st.write("Protein (mg/mL) =", a280 * 1.5)

# --------------------------------------------------
# DNA / RNA
# --------------------------------------------------
elif tool == "DNA / RNA":
    st.subheader("DNA / RNA Concentration")
    kind = st.selectbox("Type", ["DNA", "RNA"])
    a260 = st.number_input("A260")
    dilution = st.number_input("Dilution factor", value=1.0)
    factor = 50 if kind == "DNA" else 40
    if st.button("Calculate"):
        st.write("Concentration (µg/mL) =", a260 * factor * dilution)

# --------------------------------------------------
# pH
# --------------------------------------------------
elif tool == "pH":
    st.subheader("pH Calculator")
    h = st.number_input("[H⁺] (M)", min_value=1e-12)
    if st.button("Calculate"):
        st.write("pH =", -math.log10(h))

# --------------------------------------------------
# OSMOTIC PRESSURE
# --------------------------------------------------
elif tool == "Osmotic Pressure":
    st.subheader("Osmotic Pressure")
    i = st.number_input("van’t Hoff factor")
    m = st.number_input("Molarity (M)")
    t = st.number_input("Temperature (K)")
    if st.button("Calculate"):
        st.write("π (atm) =", i * m * 0.0821 * t)

# --------------------------------------------------
# HARDY WEINBERG
# --------------------------------------------------
elif tool == "Hardy–Weinberg":
    st.subheader("Hardy–Weinberg Equation")
    p = st.slider("Allele frequency (p)", 0.0, 1.0, 0.5)
    q = 1 - p
    if st.button("Calculate"):
        st.write("p² =", p**2)
        st.write("2pq =", 2*p*q)
        st.write("q² =", q**2)

st.markdown('</div>', unsafe_allow_html=True)
