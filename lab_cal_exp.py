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
# CUSTOM CSS FOR STYLING
# --------------------------------------------------
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: "Segoe UI", sans-serif;
    background-color: #f4f6f8;
}
header {visibility: hidden;}
.lab-panel {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
    border-left: 6px solid #008080;
    margin-bottom: 20px;
}
h1, h2, h3 { color: #1f2d3d; }
.stButton > button {
    background-color: #1E90FF;  /* Blue buttons */
    color: white;
    border-radius: 10px;
    border: none;
    padding: 12px 24px;
    font-weight: bold;
    width: 100%;
}
.stButton > button:hover {
    background-color: #104E8B;
}
.back-button {
    background-color: #FF4C4C;  /* Red back button */
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    width: 100%;
}
input, .stNumberInput input {
    font-size: 16px;
    padding: 6px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("🧪 Biotechnology Laboratory Calculator")
st.caption("Accurate scientific calculations for biotechnology & life science laboratories")

# --------------------------------------------------
# SIDEBAR MENU
# --------------------------------------------------
tool = st.sidebar.radio(
    "Select Calculator 🔬",
    [
        "Mass",
        "Volume",
        "Temperature Converter",
        "Density",
        "Dilution (C₁V₁ = C₂V₂)",
        "Molarity (from moles)",
        "Molarity (from grams)",
        "Molarity by Dilution (M₁V₁ = M₂V₂)",
        "Normality",
        "Normality by Dilution (N₁V₁ = N₂V₂)",
        "Molarity → Normality",
        "Molality",
        "Percentage Solutions",
        "Moles Calculation",
        "Protein",
        "DNA / RNA Concentration",
        "DNA Purity",
        "pH",
        "Osmotic Pressure",
        "Hardy–Weinberg"
    ]
)

st.markdown('<div class="lab-panel">', unsafe_allow_html=True)

# --------------------------------------------------
# BACK BUTTON
# --------------------------------------------------
if st.button("🔙 Back to Main Menu", key="back"):
    st.experimental_rerun()
# -------------------------------
# MASS
# -------------------------------
if tool == "🏋️ Mass":
    st.subheader("⚖️ Mass Conversion")
    units = {"kg":1000, "g":1, "mg":0.001, "oz":28.35}
    value = st.number_input("Value", min_value=0.0)
    from_u = st.selectbox("From unit", units.keys())
    to_u = st.selectbox("To unit", units.keys())
    if st.button("Calculate"):
        st.success(f"✅ Result: {(value * units[from_u]) / units[to_u]} {to_u}")

# -------------------------------
# VOLUME
# -------------------------------
elif tool == "💧 Volume":
    st.subheader("💧 Volume Conversion")
    units = {"L":1, "mL":0.001, "µL":0.000001, "m³":1000}
    value = st.number_input("Value", min_value=0.0)
    from_u = st.selectbox("From unit", units.keys())
    to_u = st.selectbox("To unit", units.keys())
    if st.button("Calculate"):
        st.success(f"✅ Result: {(value * units[from_u]) / units[to_u]} {to_u}")

# -------------------------------
# TEMPERATURE
# -------------------------------
elif tool == "🌡️ Temperature Converter":
    st.subheader("🌡️ Temperature Converter")
    conversion = st.selectbox(
        "Select Conversion",
        [
            "Celsius → Kelvin",
            "Kelvin → Celsius",
            "Fahrenheit → Celsius",
            "Celsius → Fahrenheit",
            "Kelvin → Fahrenheit",
            "Fahrenheit → Kelvin"
        ]
    )
    temp = st.number_input("Enter Temperature Value")
    if st.button("Convert"):
        if conversion == "Celsius → Kelvin":
            result = temp + 273.15
        elif conversion == "Kelvin → Celsius":
            result = temp - 273.15
        elif conversion == "Fahrenheit → Celsius":
            result = (temp - 32) * 5/9
        elif conversion == "Celsius → Fahrenheit":
            result = (temp * 9/5) + 32
        elif conversion == "Kelvin → Fahrenheit":
            result = (temp - 273.15) * 9/5 + 32
        elif conversion == "Fahrenheit → Kelvin":
            result = (temp - 32) * 5/9 + 273.15
        st.success(f"✅ Result: {result:.2f}")

# -------------------------------
# DENSITY
# -------------------------------
elif tool == "⚖️ Density":
    st.subheader("⚖️ Density Calculator")
    mass = st.number_input("Mass (g)")
    volume = st.number_input("Volume (mL)")
    if st.button("Calculate"):
        st.success(f"✅ Density = {mass / volume} g/mL")

# -------------------------------
# DILUTION C1V1
# -------------------------------
elif tool == "🔬 Dilution (C₁V₁ = C₂V₂)":
    st.subheader("💧 Dilution Calculator (C₁ × V₁ = C₂ × V₂)")
    col1, col2 = st.columns(2)
    with col1:
        C1 = st.number_input("C₁ (Initial concentration)", value=0.0)
        V1 = st.number_input("V₁ (Initial volume)", value=0.0)
    with col2:
        C2 = st.number_input("C₂ (Final concentration)", value=0.0)
        V2 = st.number_input("V₂ (Final volume)", value=0.0)
    st.info("👉 Set ONE value as 0 to calculate it")
    if st.button("Calculate"):
        if C1 == 0 and V1 > 0:
            st.success(f"✅ C₁ = {(C2 * V2) / V1}")
        elif V1 == 0 and C1 > 0:
            st.success(f"✅ V₁ = {(C2 * V2) / C1}")
        elif C2 == 0 and V2 > 0:
            st.success(f"✅ C₂ = {(C1 * V1) / V2}")
        elif V2 == 0 and C2 > 0:
            st.success(f"✅ V₂ = {(C1 * V1) / C2}")
        else:
            st.warning("⚠️ Please set ONLY ONE value to 0")

# -------------------------------
# MOLARITY (from moles)
# -------------------------------
elif tool == "📏 Molarity (from moles)":
    st.subheader("📏 Molarity (M = n / V)")
    moles = st.number_input("Moles of solute (mol)")
    volume = st.number_input("Volume of solution (L)")
    if st.button("Calculate"):
        st.success(f"✅ Molarity (M) = {moles / volume}")

# -------------------------------
# MOLARITY (from grams)
# -------------------------------
elif tool == "📏 Molarity (from grams)":
    st.subheader("📏 Molarity from grams")
    grams = st.number_input("Mass of solute (g)")
    molar_mass = st.number_input("Molar mass (g/mol)")
    volume = st.number_input("Volume of solution (L)")
    if st.button("Calculate"):
        moles = grams / molar_mass
        st.success(f"✅ Molarity (M) = {moles / volume}")

# -------------------------------
# MOLARITY BY DILUTION
# -------------------------------
elif tool == "💦 Molarity by Dilution (M₁V₁ = M₂V₂)":
    st.subheader("💦 Molarity by Dilution")
    M1 = st.number_input("M₁", value=0.0)
    V1 = st.number_input("V₁", value=0.0)
    M2 = st.number_input("M₂", value=0.0)
    V2 = st.number_input("V₂", value=0.0)
    if st.button("Calculate"):
        if M1 == 0: st.success(f"✅ M₁ = {(M2*V2)/V1}")
        elif V1 == 0: st.success(f"✅ V₁ = {(M2*V2)/M1}")
        elif M2 == 0: st.success(f"✅ M₂ = {(M1*V1)/V2}")
        elif V2 == 0: st.success(f"✅ V₂ = {(M1*V1)/M2}")

# -------------------------------
# NORMALITY
# -------------------------------
elif tool == "⚡ Normality":
    st.subheader("⚡ Normality (N)")
    gram_eq = st.number_input("Gram equivalents")
    volume = st.number_input("Volume (L)")
    if st.button("Calculate"):
        st.success(f"✅ Normality (N) = {gram_eq / volume}")

# -------------------------------
# NORMALITY BY DILUTION
# -------------------------------
elif tool == "⚡ Normality by Dilution (N₁V₁ = N₂V₂)":
    st.subheader("⚡ Normality by Dilution")
    N1 = st.number_input("N₁", value=0.0)
    V1 = st.number_input("V₁", value=0.0)
    N2 = st.number_input("N₂", value=0.0)
    V2 = st.number_input("V₂", value=0.0)
    if st.button("Calculate"):
        if N1 == 0: st.success(f"✅ N₁ = {(N2*V2)/V1}")
        elif V1 == 0: st.success(f"✅ V₁ = {(N2*V2)/N1}")
        elif N2 == 0: st.success(f"✅ N₂ = {(N1*V1)/V2}")
        elif V2 == 0: st.success(f"✅ V₂ = {(N1*V1)/N2}")

# -------------------------------
# MOLARITY → NORMALITY
# -------------------------------
elif tool == "📐 Molarity → Normality":
    st.subheader("📐 Molarity to Normality")
    M = st.number_input("Molarity (M)")
    n_factor = st.number_input("n-factor / valency")
    if st.button("Calculate"):
        st.success(f"✅ Normality (N) = {M * n_factor}")

# -------------------------------
# MOLALITY
# -------------------------------
elif tool == "📊 Molality":
    st.subheader("📊 Molality")
    moles = st.number_input("Moles of solute (mol)")
    mass_solvent = st.number_input("Mass of solvent (kg)")
    if st.button("Calculate"):
        st.success(f"✅ Molality (m) = {moles / mass_solvent} m")

# -------------------------------
# PERCENTAGE SOLUTIONS
# -------------------------------
elif tool == "🧪 Percentage Solutions":
    st.subheader("🧪 Percentage Solutions")
    type_ = st.selectbox("Type", ["%(w/v)", "%(v/v)", "%(m/v)"])
    a = st.number_input("Solute")
    b = st.number_input("Solution")
    if st.button("Calculate"):
        st.success(f"✅ Percentage = {(a/b)*100:.2f} %")

# -------------------------------
# MOLES CALCULATION
# -------------------------------
elif tool == "🔹 Moles Calculation":
    st.subheader("🔹 Moles Calculation")
    mass = st.number_input("Mass (g)")
    molar_mass = st.number_input("Molar mass (g/mol)")
    if st.button("Calculate"):
        st.success(f"✅ Moles = {mass / molar_mass}")

# -------------------------------
# PROTEIN
# -------------------------------
elif tool == "🧫 Protein":
    st.subheader("🧫 Protein Concentration")
    a280 = st.number_input("A280")
    if st.button("Calculate"):
        st.success(f"✅ Protein (mg/mL) = {a280 * 1.5}")

# -------------------------------
# DNA/RNA Concentration
# -------------------------------
elif tool == "🧬 DNA / RNA Concentration":
    st.subheader("🧬 DNA / RNA Concentration")
    kind = st.selectbox("Type", ["DNA", "RNA"])
    a260 = st.number_input("A260")
    dilution = st.number_input("Dilution factor", value=1.0)
    if st.button("Calculate"):
        factor = 50 if kind=="DNA" else 40
        st.success(f"✅ {kind} concentration (µg/mL) = {a260*factor*dilution}")

# -------------------------------
# DNA PURITY
# -------------------------------
elif tool == "🧬 DNA Purity":
    st.subheader("🧬 DNA Purity (A260/A280)")
    a260 = st.number_input("A260")
    a280 = st.number_input("A280")
    if st.button("Calculate"):
        ratio = a260 / a280
        st.success(f"✅ A260/A280 = {ratio:.2f}")
        if 1.8 <= ratio <= 2.0:
            st.info("🟢 Pure DNA")
        else:
            st.warning("🔴 Impure DNA")

# -------------------------------
# pH
# -------------------------------
elif tool == "🧪 pH":
    st.subheader("🧪 pH Calculator")
    h = st.number_input("[H⁺] (M)", min_value=1e-12)
    if st.button("Calculate"):
        st.success(f"✅ pH = {-math.log10(h):.2f}")

# -------------------------------
# OSMOTIC PRESSURE
# -------------------------------
elif tool == "💧 Osmotic Pressure":
    st.subheader("💧 Osmotic Pressure")
    i = st.number_input("van’t Hoff factor (i)")
    M = st.number_input("Molarity (M)")
    T = st.number_input("Temperature (K)")
    if st.button("Calculate"):
        st.success(f"✅ π (atm) = {i*M*0.0821*T:.3f}")

# -------------------------------
# HARDY-WEINBERG
# -------------------------------
elif tool == "🔬 Hardy–Weinberg":
    st.subheader("🔬 Hardy–Weinberg Equation")
    p = st.slider("Allele frequency (p)", 0.0, 1.0, 0.5)
    q = 1-p
    if st.button("Calculate"):
        st.success(f"✅ p² = {p**2:.3f}, 2pq = {2*p*q:.3f}, q² = {q**2:.3f}")

st.markdown('</div>', unsafe_allow_html=True)


