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
html, body, [class*="css"] {
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
st.caption("Accurate scientific calculations for biotechnology & life science laboratories")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
tool = st.sidebar.radio(
    "Calculators",
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
# SIMPLE C1V1 DILUTION
# --------------------------------------------------
if tool == "C₁V₁ Dilution (Simple)":
    st.subheader("C₁V₁ Dilution Calculator")
    st.caption("Formula: C₁ × V₁ = C₂ × V₂")

    col1, col2 = st.columns(2)
    with col1:
        C1 = st.number_input("C₁ (Initial concentration)", value=0.0)
        V1 = st.number_input("V₁ (Initial volume)", value=0.0)
    with col2:
        C2 = st.number_input("C₂ (Final concentration)", value=0.0)
        V2 = st.number_input("V₂ (Final volume)", value=0.0)

    st.info("👉 Set ONE value as 0 to calculate it")

    if st.button("Calculate C₁V₁"):
        if C1 == 0 and V1 > 0:
            st.success(f"C₁ = {(C2 * V2) / V1}")
        elif V1 == 0 and C1 > 0:
            st.success(f"V₁ = {(C2 * V2) / C1}")
        elif C2 == 0 and V2 > 0:
            st.success(f"C₂ = {(C1 * V1) / V2}")
        elif V2 == 0 and C2 > 0:
            st.success(f"V₂ = {(C1 * V1) / C2}")
        else:
            st.warning("⚠️ Please set ONLY ONE value to 0")


#--------------------------------------------------
# Normality
#-------------------------------------------------
elif tool == "Normality (N)":
    st.subheader("Normality (N)")
    st.caption("Formula: Normality = Gram equivalents / Volume (L)")

    gram_eq = st.number_input("Gram equivalents")
    volume = st.number_input("Volume of solution (L)")

    if st.button("Calculate"):
        if volume == 0:
            st.warning("Volume cannot be zero")
        else:
            N = gram_eq / volume
            st.success(f"Normality (N) = {N}")
#-----------------------------------------------------
# Molality
#----------------------------------------------------
elif tool == "Molality":
    st.subheader("Molality (m)")
    st.caption("Formula: Molality (m) = Moles of solute / Mass of solvent (kg)")

    moles = st.number_input("Moles of solute (mol)")
    mass_solvent = st.number_input("Mass of solvent (kg)")

    if st.button("Calculate"):
        if mass_solvent == 0:
            st.warning("Mass of solvent cannot be zero")
        else:
            molality = moles / mass_solvent
            st.success(f"Molality (m) = {molality} m")

#------------------------------------------------------

# percantage solution
#---------------------------------------------------------

elif tool == "Percentage Solution":
    st.header("Percentage Solution")

    type_ = st.selectbox("Type", ["%(w/v)", "%(v/v)", "%(m/v)"])
    a = st.number_input("Numerator value")
    b = st.number_input("Denominator value")

    if st.button("Calculate"):
        percent = (a / b) * 100

        lab_result(
            "Percentage Result",
            {"Numerator": a, "Denominator": b},
            "(value / total) × 100",
            f"{percent:.2f} %"
        )


# --------------------------------------------------
# MASS
# --------------------------------------------------
if tool == "Mass":
    st.subheader("Mass Conversion")
    units = {"kg":1000, "g":1, "mg":0.001}
    value = st.number_input("Value", min_value=0.0)
    from_u = st.selectbox("From unit", units.keys())
    to_u = st.selectbox("To unit", units.keys())
    if st.button("Calculate"):
        st.write("Result =", (value * units[from_u]) / units[to_u], to_u)


#-----------------------------------------------------
# DNA concentration 
#----------------------------------------------------
elif tool == "DNA Concentration":
    st.header("DNA Concentration")

    A260 = st.number_input("A260")
    dilution = st.number_input("Dilution factor", value=1.0)

    if st.button("Calculate"):
        dna = A260 * 50 * dilution

        lab_result(
            "DNA Result",
            {"A260": A260, "Dilution": dilution},
            "DNA = A260 × 50 × dilution",
            f"{dna:.2f} µg/mL"
        )

#--------------------------------------------------
# RNA concentration
#--------------------------------------------------
elif tool == "RNA Concentration":
    st.header("RNA Concentration")

    A260 = st.number_input("A260")
    dilution = st.number_input("Dilution factor", value=1.0)

    if st.button("Calculate"):
        rna = A260 * 40 * dilution

        lab_result(
            "RNA Result",
            {"A260": A260, "Dilution": dilution},
            "RNA = A260 × 40 × dilution",
            f"{rna:.2f} µg/mL"
        )

# -------------------------------------------------
# Osmotic pressur 
#--------------------------------------------------
elif tool == "Osmotic Pressure":
    st.header("Osmotic Pressure")

    i = st.number_input("van’t Hoff factor (i)")
    M = st.number_input("Molarity (M)")
    T = st.number_input("Temperature (K)")

    if st.button("Calculate"):
        pi = i * M * 0.0821 * T

        lab_result(
            "Osmotic Pressure Result",
            {"i": i, "M": M, "T": T},
            "π = i × M × R × T",
            f"{pi:.3f} atm"
        )

# =====================================================
# HARDY WEINBERG
# =====================================================
elif tool == "Hardy–Weinberg Equation":
    st.header("Hardy–Weinberg Equation")

    p = st.slider("Allele frequency (p)", 0.0, 1.0, 0.5)
    q = 1 - p

    if st.button("Calculate"):
        lab_result(
            "Hardy–Weinberg Result",
            {"p": p, "q": q},
            "p² + 2pq + q² = 1",
            f"p²={p*2:.3f}, 2pq={2*p*q:.3f}, q²={q*2:.3f}"
        )







# --------------------------------------------------
# VOLUME
# --------------------------------------------------
elif tool == "Volume":
    st.subheader("Volume Conversion")
    units = {"L":1, "mL":0.001, "µL":0.000001}
    value = st.number_input("Value", min_value=0.0)
    from_u = st.selectbox("From unit", units.keys())
    to_u = st.selectbox("To unit", units.keys())
    if st.button("Calculate"):
        st.write("Result =", (value * units[from_u]) / units[to_u], to_u)

# --------------------------------------------------
# TEMPERATURE
# --------------------------------------------------
elif tool == "Temperature Converter":
    st.header("Temperature Converter")

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
            formula = "K = C + 273.15"
            output = f"{result:.2f} K"

        elif conversion == "Kelvin → Celsius":
            result = temp - 273.15
            formula = "C = K − 273.15"
            output = f"{result:.2f} °C"

        elif conversion == "Fahrenheit → Celsius":
            result = (temp - 32) * 5/9
            formula = "C = (F − 32) × 5/9"
            output = f"{result:.2f} °C"

        elif conversion == "Celsius → Fahrenheit":
            result = (temp * 9/5) + 32
            formula = "F = (C × 9/5) + 32"
            output = f"{result:.2f} °F"

        elif conversion == "Kelvin → Fahrenheit":
            result = (temp - 273.15) * 9/5 + 32
            formula = "F = (K − 273.15) × 9/5 + 32"
            output = f"{result:.2f} °F"

        elif conversion == "Fahrenheit → Kelvin":
            result = (temp - 32) * 5/9 + 273.15
            formula = "K = (F − 32) × 5/9 + 273.15"
            output = f"{result:.2f} K"

        lab_result(
            "Temperature Conversion Result",
            {"Input Temperature": temp, "Conversion": conversion},
            formula,
            output
        )
# --------------------------------------------------
# DENSITY
# --------------------------------------------------
elif tool == "Density":
    st.subheader("Density Calculator")
    mass = st.number_input("Mass (g)")
    volume = st.number_input("Volume (mL)")
    if st.button("Calculate"):
        st.write("Density (g/mL) =", mass / volume)

# --------------------------------------------------
# MOLARITY FROM MOLES
# --------------------------------------------------
elif tool == "Molarity (from moles)":
    st.subheader("Molarity (M = n / V)")
    moles = st.number_input("Moles (mol)")
    volume = st.number_input("Volume (L)")
    if st.button("Calculate"):
        st.write("Molarity (M) =", moles / volume)

# --------------------------------------------------
# MOLARITY FROM GRAMS
# --------------------------------------------------
elif tool == "Molarity (from grams)":
    st.subheader("Molarity from grams")
    grams = st.number_input("Mass of solute (g)")
    molar_mass = st.number_input("Molar mass (g/mol)")
    volume = st.number_input("Volume of solution (L)")
    if st.button("Calculate"):
        moles = grams / molar_mass
        st.write("Molarity (M) =", moles / volume)

# --------------------------------------------------
# MOLARITY BY DILUTION
# --------------------------------------------------
elif tool == "Molarity by Dilution (M₁V₁ = M₂V₂)":
    st.subheader("Molarity by Dilution")
    M1 = st.number_input("M₁", value=0.0)
    V1 = st.number_input("V₁", value=0.0)
    M2 = st.number_input("M₂", value=0.0)
    V2 = st.number_input("V₂", value=0.0)
    if st.button("Calculate"):
        if M1 == 0: st.write("M₁ =", (M2*V2)/V1)
        elif V1 == 0: st.write("V₁ =", (M2*V2)/M1)
        elif M2 == 0: st.write("M₂ =", (M1*V1)/V2)
        elif V2 == 0: st.write("V₂ =", (M1*V1)/M2)

# --------------------------------------------------
# NORMALITY BY DILUTION
# --------------------------------------------------
elif tool == "Normality by Dilution (N₁V₁ = N₂V₂)":
    st.subheader("Normality by Dilution")
    N1 = st.number_input("N₁", value=0.0)
    V1 = st.number_input("V₁", value=0.0)
    N2 = st.number_input("N₂", value=0.0)
    V2 = st.number_input("V₂", value=0.0)
    if st.button("Calculate"):
        if N1 == 0: st.write("N₁ =", (N2*V2)/V1)
        elif V1 == 0: st.write("V₁ =", (N2*V2)/N1)
        elif N2 == 0: st.write("N₂ =", (N1*V1)/V2)
        elif V2 == 0: st.write("V₂ =", (N1*V1)/N2)

# --------------------------------------------------
# MOLARITY → NORMALITY
# --------------------------------------------------
elif tool == "Molarity → Normality":
    st.subheader("Molarity to Normality")
    M = st.number_input("Molarity (M)")
    n_factor = st.number_input("n-factor / valency")
    if st.button("Calculate"):
        st.write("Normality (N) =", M * n_factor)

# --------------------------------------------------
# MOLES CALCULATION
# --------------------------------------------------
elif tool == "Moles Calculation":
    st.subheader("Calculation of Moles")
    mass = st.number_input("Mass (g)")
    molar_mass = st.number_input("Molar mass (g/mol)")
    if st.button("Calculate"):
        st.write("Moles (mol) =", mass / molar_mass)

# --------------------------------------------------
# DNA PURITY
# --------------------------------------------------
elif tool == "DNA Purity":
    st.subheader("DNA Purity (A260/A280)")
    a260 = st.number_input("A260")
    a280 = st.number_input("A280")
    if st.button("Calculate"):
        ratio = a260 / a280
        st.write("A260/A280 =", ratio)
        if 1.8 <= ratio <= 2.0:
            st.success("Pure DNA")
        else:
            st.warning("Impure sample")

st.markdown('</div>', unsafe_allow_html=True)
