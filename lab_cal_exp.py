
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
        "Molarity",
        "Normality",
        "Molality",
        "Percentage Solution",
        "Dilution",
        "Temperature",
        "Density"
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

