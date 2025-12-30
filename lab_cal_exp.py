import streamlit as st

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

# =====================================================
# HOME PAGE
# =====================================================
if st.session_state.page == "home":

    st.markdown("### 🔬 Select Calculator")

    calculators = [
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

    choice = st.selectbox("Choose tool", calculators)

    if st.button("➡️ Open Calculator"):
        go_calc(choice)

# =====================================================
# BACK BUTTON (FOR ALL CALCULATORS)
# =====================================================
if st.session_state.page != "home":
    if st.button("⬅️ Back to Home"):
        go_home()
    st.markdown("---")

# =====================================================
# MASS
# =====================================================
if st.session_state.page == "Mass":
    st.subheader("⚖️ Mass Conversion")
    value = st.number_input("Value", min_value=0.0)
    from_u = st.selectbox("From", ["kg", "g", "mg"])
    to_u = st.selectbox("To", ["kg", "g", "mg"])

    factors = {"kg": 1000, "g": 1, "mg": 0.001}

    if st.button("Calculate"):
        result = (value * factors[from_u]) / factors[to_u]
        st.success(f"Result = {result:.4f} {to_u}")





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


# --------------------------------------------------
# MOLARITY FROM MOLES
# --------------------------------------------------
elif tool == "Molarity (from moles)":
    st.subheader("Molarity (M = n / V)")
    moles = st.number_input("Moles (mol)")
    volume = st.number_input("Volume (L)")
    if st.button("Calculate"):
        st.write("Molarity (M) =", moles / volume)



# =====================================================
# VOLUME
# =====================================================
elif st.session_state.page == "Volume":
    st.subheader("🧪 Volume Conversion")
    value = st.number_input("Value", min_value=0.0)
    from_u = st.selectbox("From", ["L", "mL", "µL"])
    to_u = st.selectbox("To", ["L", "mL", "µL"])

    factors = {"L": 1, "mL": 0.001, "µL": 0.000001}

    if st.button("Calculate"):
        result = (value * factors[from_u]) / factors[to_u]
        st.success(f"Result = {result:.6f} {to_u}")

# =====================================================
# MOLARITY
# =====================================================
elif st.session_state.page == "Molarity":
    st.subheader("⚗️ Molarity")
    moles = st.number_input("Moles (mol)")
    volume = st.number_input("Volume (L)")

    if st.button("Calculate"):
        if volume == 0:
            st.error("Volume cannot be zero")
        else:
            st.success(f"Molarity (M) = {moles/volume:.4f}")

# =====================================================
# NORMALITY
# =====================================================
elif st.session_state.page == "Normality":
    st.subheader("🧬 Normality")
    gram_eq = st.number_input("Gram equivalents")
    volume = st.number_input("Volume (L)")

    if st.button("Calculate"):
        if volume == 0:
            st.error("Volume cannot be zero")
        else:
            st.success(f"Normality (N) = {gram_eq/volume:.4f}")

# =====================================================
# MOLALITY
# =====================================================
elif st.session_state.page == "Molality":
    st.subheader("🧫 Molality")
    moles = st.number_input("Moles of solute (mol)")
    mass = st.number_input("Mass of solvent (kg)")

    if st.button("Calculate"):
        if mass == 0:
            st.error("Mass cannot be zero")
        else:
            st.success(f"Molality (m) = {moles/mass:.4f}")

# =====================================================
# PERCENTAGE SOLUTION
# =====================================================
elif st.session_state.page == "Percentage Solution":
    st.subheader("📊 Percentage Solution")
    numerator = st.number_input("Numerator")
    denominator = st.number_input("Denominator")

    if st.button("Calculate"):
        if denominator == 0:
            st.error("Denominator cannot be zero")
        else:
            st.success(f"Percentage = {(numerator/denominator)*100:.2f}%")

# =====================================================
# DILUTION
# =====================================================
elif st.session_state.page == "Dilution":
    st.subheader("🧪 Dilution (C₁V₁ = C₂V₂)")
    C1 = st.number_input("C₁", value=0.0)
    V1 = st.number_input("V₁", value=0.0)
    C2 = st.number_input("C₂", value=0.0)
    V2 = st.number_input("V₂", value=0.0)

    if st.button("Calculate"):
        if C1 == 0 and V1 > 0:
            st.success(f"C₁ = {(C2*V2)/V1:.4f}")
        elif V1 == 0 and C1 > 0:
            st.success(f"V₁ = {(C2*V2)/C1:.4f}")
        elif C2 == 0 and V2 > 0:
            st.success(f"C₂ = {(C1*V1)/V2:.4f}")
        elif V2 == 0 and C2 > 0:
            st.success(f"V₂ = {(C1*V1)/C2:.4f}")
        else:
            st.warning("Set only ONE value to zero")

# =====================================================
# TEMPERATURE
# =====================================================
elif st.session_state.page == "Temperature":
    st.subheader("🌡️ Temperature Converter")
    temp = st.number_input("Temperature")
    mode = st.selectbox("Conversion", ["C → K", "K → C", "C → F", "F → C"])

    if st.button("Convert"):
        if mode == "C → K":
            st.success(f"{temp + 273.15:.2f} K")
        elif mode == "K → C":
            st.success(f"{temp - 273.15:.2f} °C")
        elif mode == "C → F":
            st.success(f"{(temp*9/5)+32:.2f} °F")
        elif mode == "F → C":
            st.success(f"{(temp-32)*5/9:.2f} °C")

# =====================================================
# DENSITY
# =====================================================
elif st.session_state.page == "Density":
    st.subheader("🧱 Density")
    mass = st.number_input("Mass (g)")
    volume = st.number_input("Volume (mL)")

    if st.button("Calculate"):
        if volume == 0:
            st.error("Volume cannot be zero")
        else:
            st.success(f"Density = {mass/volume:.4f} g/mL")

