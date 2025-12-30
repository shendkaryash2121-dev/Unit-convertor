import streamlit as st
import math


# =====================================================
# PAGE CONFIG (MOBILE SAFE)
# =====================================================
st.set_page_config(
    page_title="Biotech Lab Calculator",
    page_icon="🧪",
    layout="centered"
)

# =====================================================
# SESSION STATE (FOR BACK BUTTON)
# =====================================================
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_home():
    st.session_state.page = "home"

def go_calc(name):
    st.session_state.page = name

# =====================================================
# SAFE MOBILE CSS
# =====================================================
st.markdown("""
<style>
.stButton > button {
    width: 100%;
    background-color: #1976D2;
    color: white;
    font-size: 16px;
    border-radius: 12px;
    padding: 12px;
}
.stSelectbox, .stNumberInput {
    font-size: 16px;
}
.card {
    background-color: white;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================
st.title("🧪 Biotechnology Lab Calculator")
st.caption("Mobile-friendly scientific calculator for laboratories")
# --------------------------------------------------
# SIDEBAR MENU
# --------------------------------------------------
tool = st.sidebar.radio(
    "Select Calculator 🔬",
    [
        "Mass Conversion ⚖️",
        "Volume Conversion 💧",
        "Temperature Converter 🌡",
        "Density Calculator 🧱",
        "Dilution (C₁V₁ = C₂V₂) 💧",
        "Molarity (from moles) 🧪",
        "Molarity (from grams) 🧪",
        "Molarity by Dilution (M₁V₁ = M₂V₂) 🔄",
        "Normality (N) ⚗️",
        "Normality by Dilution (N₁V₁ = N₂V₂) 🔄",
        "Molarity → Normality 🔬",
        "Molality (m) 🧪",
        "Percentage Solutions % 📊",
        "Moles Calculation 🧪",
        "Protein Concentration 🧬",
        "DNA / RNA Concentration 🧬",
        "DNA Purity 🧬",
        "pH Calculator 🧪",
        "Osmotic Pressure 🌡",
        "Hardy–Weinberg Equation ⚖️"
    ]
)

st.markdown('<div class="lab-panel">', unsafe_allow_html=True)

# --------------------------------------------------
# BACK BUTTON
# --------------------------------------------------
if st.button("🔙 Back"):
    st.rerun()

# ----------------- Mass ---------------------------
if tool == "Mass Conversion ⚖️":
    st.subheader("⚖️ Mass Conversion")
    units = {"kg":1000, "g":1, "mg":0.001, "oz":28.35}
    value = st.number_input("Value", min_value=0.0)
    from_u = st.selectbox("From unit", units.keys())
    to_u = st.selectbox("To unit", units.keys())
    if st.button("Calculate Mass"):
        st.success(f"Result: {(value * units[from_u]) / units[to_u]} {to_u}")

# ----------------- Volume -------------------------
elif tool == "Volume Conversion 💧":
    st.subheader("💧 Volume Conversion")
    units = {"L":1, "mL":0.001, "µL":0.000001, "m³":1000}
    value = st.number_input("Value", min_value=0.0)
    from_u = st.selectbox("From unit", units.keys())
    to_u = st.selectbox("To unit", units.keys())
    if st.button("Calculate Volume"):
        st.success(f"Result: {(value * units[from_u]) / units[to_u]} {to_u}")

# ----------------- Temperature --------------------
elif tool == "Temperature Converter 🌡":
    st.subheader("🌡 Temperature Converter")
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
    if st.button("Convert Temperature"):
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
        st.success(f"Result: {result:.2f}")

# ----------------- Density ------------------------
elif tool == "Density Calculator 🧱":
    st.subheader("🧱 Density Calculator")
    mass = st.number_input("Mass (g)")
    volume = st.number_input("Volume (mL)")
    if st.button("Calculate Density"):
        st.success(f"Density: {mass / volume} g/mL")

# ----------------- Dilution -----------------------
elif tool == "Dilution (C₁V₁ = C₂V₂) 💧":
    st.subheader("💧 Dilution Calculator (C₁V₁ = C₂V₂)")
    C1 = st.number_input("C₁ (Initial concentration)", value=0.0)
    V1 = st.number_input("V₁ (Initial volume)", value=0.0)
    C2 = st.number_input("C₂ (Final concentration)", value=0.0)
    V2 = st.number_input("V₂ (Final volume)", value=0.0)
    if st.button("Calculate Dilution"):
        if C1 == 0 and V1 > 0:
            st.success(f"C₁ = {(C2 * V2)/V1}")
        elif V1 == 0 and C1 > 0:
            st.success(f"V₁ = {(C2 * V2)/C1}")
        elif C2 == 0 and V2 > 0:
            st.success(f"C₂ = {(C1 * V1)/V2}")
        elif V2 == 0 and C2 > 0:
            st.success(f"V₂ = {(C1 * V1)/C2}")
        else:
            st.warning("Set ONE value to 0 to calculate it")

# ----------------- Molarity -----------------------
elif tool == "Molarity (from moles) 🧪":
    st.subheader("🧪 Molarity (M = n/V)")
    moles = st.number_input("Moles (mol)")
    volume = st.number_input("Volume (L)")
    if st.button("Calculate Molarity"):
        st.success(f"Molarity: {moles / volume} M")

elif tool == "Molarity (from grams) 🧪":
    st.subheader("🧪 Molarity from grams")
    grams = st.number_input("Mass of solute (g)")
    molar_mass = st.number_input("Molar mass (g/mol)")
    volume = st.number_input("Volume (L)")
    if st.button("Calculate Molarity"):
        moles = grams / molar_mass
        st.success(f"Molarity: {moles / volume} M")

elif tool == "Molarity by Dilution (M₁V₁ = M₂V₂) 🔄":
    st.subheader("🔄 Molarity by Dilution")
    M1 = st.number_input("M₁", value=0.0)
    V1 = st.number_input("V₁", value=0.0)
    M2 = st.number_input("M₂", value=0.0)
    V2 = st.number_input("V₂", value=0.0)
    if st.button("Calculate"):
        if M1 == 0: st.success(f"M₁ = {(M2*V2)/V1}")
        elif V1 == 0: st.success(f"V₁ = {(M2*V2)/M1}")
        elif M2 == 0: st.success(f"M₂ = {(M1*V1)/V2}")
        elif V2 == 0: st.success(f"V₂ = {(M1*V1)/M2}")

# ----------------- Normality ----------------------
elif tool == "Normality (N) ⚗️":
    st.subheader("⚗️ Normality Calculator")
    gram_eq = st.number_input("Gram equivalents")
    volume = st.number_input("Volume (L)")
    if st.button("Calculate Normality"):
        if volume == 0:
            st.warning("Volume cannot be zero")
        else:
            N = gram_eq / volume
            st.success(f"Normality (N) = {N}")

elif tool == "Normality by Dilution (N₁V₁ = N₂V₂) 🔄":
    st.subheader("🔄 Normality by Dilution")
    N1 = st.number_input("N₁", value=0.0)
    V1 = st.number_input("V₁", value=0.0)
    N2 = st.number_input("N₂", value=0.0)
    V2 = st.number_input("V₂", value=0.0)
    if st.button("Calculate"):
        if N1 == 0: st.success(f"N₁ = {(N2*V2)/V1}")
        elif V1 == 0: st.success(f"V₁ = {(N2*V2)/N1}")
        elif N2 == 0: st.success(f"N₂ = {(N1*V1)/V2}")
        elif V2 == 0: st.success(f"V₂ = {(N1*V1)/N2}")

# ----------------- Molarity to Normality ----------
elif tool == "Molarity → Normality 🔬":
    st.subheader("🔬 Molarity to Normality")
    M = st.number_input("Molarity (M)")
    n_factor = st.number_input("n-factor / valency")
    if st.button("Calculate Normality"):
        st.success(f"Normality (N) = {M * n_factor}")

# ----------------- Molality -----------------------
elif tool == "Molality (m) 🧪":
    st.subheader("🧪 Molality Calculator")
    moles = st.number_input("Moles of solute (mol)")
    mass_solvent = st.number_input("Mass of solvent (kg)")
    if st.button("Calculate Molality"):
        if mass_solvent == 0:
            st.warning("Mass of solvent cannot be zero")
        else:
            molality = moles / mass_solvent
            st.success(f"Molality (m) = {molality} m")

# ----------------- Percentage ---------------------
elif tool == "Percentage Solutions % 📊":
    st.subheader("📊 Percentage Solutions")
    type_ = st.selectbox("Type", ["%(w/v)", "%(v/v)", "%(m/v)"])
    a = st.number_input("Numerator value")
    b = st.number_input("Denominator value")
    if st.button("Calculate Percentage"):
        st.success(f"Percentage: {(a/b)*100:.2f} %")

# ----------------- Moles Calculation --------------
elif tool == "Moles Calculation 🧪":
    st.subheader("🧪 Moles Calculation")
    mass = st.number_input("Mass (g)")
    molar_mass = st.number_input("Molar mass (g/mol)")
    if st.button("Calculate Moles"):
        st.success(f"Moles (mol) = {mass/molar_mass}")

# ----------------- Protein ------------------------
elif tool == "Protein Concentration 🧬":
    st.subheader("🧬 Protein Concentration")
    A280 = st.number_input("A280")
    if st.button("Calculate Protein"):
        st.success(f"Protein (mg/mL) = {A280 * 1.5}")

# ----------------- DNA / RNA ----------------------
elif tool == "DNA / RNA Concentration 🧬":
    st.subheader("🧬 DNA / RNA Concentration")
    type_ = st.selectbox("Type", ["DNA", "RNA"])
    A260 = st.number_input("A260")
    dilution = st.number_input("Dilution Factor", value=1.0)
    factor = 50 if type_ == "DNA" else 40
    if st.button("Calculate Concentration"):
        st.success(f"Concentration: {A260 * factor * dilution} µg/mL")

# ----------------- DNA Purity ---------------------
elif tool == "DNA Purity 🧬":
    st.subheader("🧬 DNA Purity (A260/A280)")
    a260 = st.number_input("A260")
    a280 = st.number_input("A280")
    if st.button("Calculate Purity"):
        ratio = a260 / a280
        st.success(f"A260/A280 = {ratio:.2f}")
        if 1.8 <= ratio <= 2.0:
            st.success("✅ Pure DNA")
        else:
            st.warning("⚠️ Impure sample")

# ----------------- pH --------------------------------
elif tool == "pH Calculator 🧪":
    st.subheader("🧪 pH Calculator")
    H = st.number_input("[H⁺] (M)", min_value=1e-12)
    if st.button("Calculate pH"):
        st.success(f"pH = {-math.log10(H):.2f}")

# ----------------- Osmotic Pressure -----------------
elif tool == "Osmotic Pressure 🌡":
    st.subheader("🌡 Osmotic Pressure")
    i = st.number_input("van’t Hoff factor (i)")
    M = st.number_input("Molarity (M)")
    T = st.number_input("Temperature (K)")
    if st.button("Calculate π"):
        pi = i * M * 0.0821 * T
        st.success(f"π = {pi:.3f} atm")

# ----------------- Hardy–Weinberg -------------------
elif tool == "Hardy–Weinberg Equation ⚖️":
    st.subheader("⚖️ Hardy–Weinberg Equation")
    p = st.slider("Allele frequency (p)", 0.0, 1.0, 0.5)
    q = 1 - p
    if st.button("Calculate HW"):
        st.success(f"p² = {p**2:.3f}, 2pq = {2*p*q:.3f}, q² = {q**2:.3f}")

st.markdown('</div>', unsafe_allow_html=True)


