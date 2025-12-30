import streamlit as st
import math
from datetime import datetime

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Biotechnology Laboratory Unit Converter",
    layout="wide"
)

st.title("Biotechnology Laboratory Unit Converter")
st.caption("Accurate scientific calculations for laboratory use")

# =====================================================
# COMMON OUTPUT FORMAT (LAB REPORT STYLE)
# =====================================================
def lab_result(title, inputs, formula, result):
    st.markdown("---")
    st.subheader(title)

    st.markdown("**Inputs:**")
    for k, v in inputs.items():
        st.write(f"- {k}: {v}")

    st.markdown("**Formula Used:**")
    st.code(formula)

    st.markdown("**Result:**")
    st.success(result)

    st.caption(f"Calculated on: {datetime.now().strftime('%d %b %Y, %H:%M')}")
    st.markdown("---")

# =====================================================
# SIDEBAR MENU
# =====================================================
tool = st.sidebar.selectbox(
    "Select Calculator",
    [
        "Mass Converter",
        "Volume Converter",
        "Dilution (C1V1 = C2V2)",
        "Molarity (from grams)",
        "Molarity to Normality",
        "Percentage Solution",
        "Molality",
        "Temperature Converter",
        "Protein Concentration",
        "DNA Concentration",
        "RNA Concentration",
        "pH Calculator",
        "Osmotic Pressure",
        "Hardy–Weinberg Equation"
    ]
)

# =====================================================
# MASS CONVERTER
# =====================================================
if tool == "Mass Converter":
    st.header("Mass Converter")

    units = {"kg":1000, "g":1, "mg":0.001, "oz":28.35}

    value = st.number_input("Enter value", min_value=0.0)
    from_u = st.selectbox("From unit", units.keys())
    to_u = st.selectbox("To unit", units.keys())

    if st.button("Calculate"):
        grams = value * units[from_u]
        result = grams / units[to_u]

        lab_result(
            "Mass Conversion Result",
            {
                "Input Value": f"{value} {from_u}",
                "Target Unit": to_u
            },
            "value × conversion_factor",
            f"{result:.6f} {to_u}"
        )

# =====================================================
# VOLUME CONVERTER
# =====================================================
elif tool == "Volume Converter":
    st.header("Volume Converter")

    units = {"L":1, "mL":0.001, "µL":0.000001, "m³":1000}

    value = st.number_input("Enter value", min_value=0.0)
    from_u = st.selectbox("From unit", units.keys())
    to_u = st.selectbox("To unit", units.keys())

    if st.button("Calculate"):
        liters = value * units[from_u]
        result = liters / units[to_u]

        lab_result(
            "Volume Conversion Result",
            {
                "Input Volume": f"{value} {from_u}",
                "Target Unit": to_u
            },
            "volume × conversion_factor",
            f"{result:.6f} {to_u}"
        )

# =====================================================
# DILUTION
# =====================================================
elif tool == "Dilution (C1V1 = C2V2)":
    st.header("Dilution Calculator")

    C1 = st.number_input("C1", value=0.0)
    V1 = st.number_input("V1", value=0.0)
    C2 = st.number_input("C2", value=0.0)
    V2 = st.number_input("V2", value=0.0)

    if st.button("Calculate"):
        if C1 == 0:
            result = (C2 * V2) / V1
            missing = "C1"
        elif V1 == 0:
            result = (C2 * V2) / C1
            missing = "V1"
        elif C2 == 0:
            result = (C1 * V1) / V2
            missing = "C2"
        elif V2 == 0:
            result = (C1 * V1) / C2
            missing = "V2"
        else:
            st.warning("Leave one value as 0 to calculate it")
            st.stop()

        lab_result(
            "Dilution Result",
            {"Calculated Parameter": missing},
            "C1 × V1 = C2 × V2",
            f"{missing} = {result}"
        )

# =====================================================
# MOLARITY FROM GRAMS
# =====================================================
elif tool == "Molarity (from grams)":
    st.header("Molarity Calculation")

    M = st.number_input("Molarity (M)")
    MW = st.number_input("Molecular Weight (g/mol)")
    V = st.number_input("Volume (L)")

    if st.button("Calculate"):
        grams = M * MW * V

        lab_result(
            "Molarity Result",
            {"M": M, "MW": MW, "Volume": V},
            "grams = M × MW × Volume",
            f"{grams:.4f} g"
        )

# =====================================================
# MOLARITY TO NORMALITY
# =====================================================
elif tool == "Molarity to Normality":
    st.header("Molarity to Normality")

    M = st.number_input("Molarity (M)")
    n = st.number_input("n (equivalence factor)")

    if st.button("Calculate"):
        N = M * n

        lab_result(
            "Normality Result",
            {"Molarity": M, "n-factor": n},
            "Normality = M × n",
            f"{N:.4f} N"
        )

# =====================================================
# PERCENTAGE
# =====================================================
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

# =====================================================
# MOLALITY
# =====================================================
elif tool == "Molality":
    st.header("Molality")

    moles = st.number_input("Moles of solute")
    kg = st.number_input("Mass of solvent (kg)")

    if st.button("Calculate"):
        molality = moles / kg

        lab_result(
            "Molality Result",
            {"Moles": moles, "Solvent mass": kg},
            "molality = moles / kg",
            f"{molality:.4f} m"
        )

# =====================================================
# TEMPERATURE
# =====================================================
elif tool == "Temperature Converter":
    st.header("Temperature Converter")

    c = st.number_input("Temperature (°C)")

    if st.button("Convert"):
        k = c + 273.15
        f = (c * 9/5) + 32

        lab_result(
            "Temperature Conversion",
            {"Celsius": c},
            "K = C + 273.15 ; F = (C×9/5)+32",
            f"{k:.2f} K , {f:.2f} °F"
        )

# =====================================================
# PROTEIN
# =====================================================
elif tool == "Protein Concentration":
    st.header("Protein Concentration")

    A280 = st.number_input("A280")

    if st.button("Calculate"):
        protein = A280 * 1.5

        lab_result(
            "Protein Result",
            {"A280": A280},
            "Protein (mg/mL) = A280 × 1.5",
            f"{protein:.3f} mg/mL"
        )

# =====================================================
# DNA
# =====================================================
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

# =====================================================
# RNA
# =====================================================
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

# =====================================================
# PH
# =====================================================
elif tool == "pH Calculator":
    st.header("pH Calculator")

    h = st.number_input("[H+]", min_value=1e-12)

    if st.button("Calculate"):
        ph = -math.log10(h)

        lab_result(
            "pH Result",
            {"[H+]": h},
            "pH = −log₁₀[H⁺]",
            f"{ph:.3f}"
        )

# =====================================================
# OSMOTIC
# =====================================================
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
            f"p²={p**2:.3f}, 2pq={2*p*q:.3f}, q²={q**2:.3f}"
        )
