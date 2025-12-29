import streamlit as st
import math

st.set_page_config(
    page_title="Lab Unit Calculator",
    page_icon="🧪",
    layout="centered"
)

st.title("🧪 Laboratory Unit Calculator")
st.caption("All-in-one Chemistry & Biology Calculator")

menu = st.selectbox(
    "Select Calculator",
    [
        "Mass Converter",
        "Volume Converter",
        "Concentration (C1V1 = C2V2)",
        "Molarity (grams needed)",
        "Molarity by Dilution",
        "Normality",
        "Normality by Dilution",
        "Percentage Solutions",
        "Temperature Converter",
        "Protein Concentration",
        "DNA Concentration",
        "RNA Concentration",
        "DNA Purity",
        "pH Calculator",
        "Density",
        "Osmotic Pressure",
        "Hardy–Weinberg Equation"
    ]
)

# ---------------- MASS ----------------
if menu == "Mass Converter":
    st.subheader("⚖️ Mass Converter")
    value = st.number_input("Value", 0.0)
    from_u = st.selectbox("From", ["kg","g","mg","oz"])
    to_u = st.selectbox("To", ["kg","g","mg","oz"])

    factors = {"kg":1000,"g":1,"mg":0.001,"oz":28.35}
    if st.button("Convert"):
        result = value * factors[from_u] / factors[to_u]
        st.success(f"{value} {from_u} = {result} {to_u}")

# ---------------- VOLUME ----------------
elif menu == "Volume Converter":
    st.subheader("🧴 Volume Converter")
    value = st.number_input("Value", 0.0)
    from_u = st.selectbox("From", ["L","mL","µL","m³"])
    to_u = st.selectbox("To", ["L","mL","µL","m³"])

    factors = {"L":1,"mL":0.001,"µL":1e-6,"m³":1000}
    if st.button("Convert"):
        result = value * factors[from_u] / factors[to_u]
        st.success(f"{value} {from_u} = {result} {to_u}")

# ---------------- CONCENTRATION ----------------
elif menu == "Concentration (C1V1 = C2V2)":
    st.subheader("🧪 Concentration Calculator")

    C1 = st.text_input("C1")
    V1 = st.text_input("V1")
    C2 = st.text_input("C2")
    V2 = st.text_input("V2")

    if st.button("Calculate"):
        vals = [C1,V1,C2,V2]
        if vals.count("") != 1:
            st.error("Leave only ONE value blank")
        else:
            C1 = float(C1) if C1 else None
            V1 = float(V1) if V1 else None
            C2 = float(C2) if C2 else None
            V2 = float(V2) if V2 else None

            if C1 is None: st.success(f"C1 = {(C2*V2)/V1}")
            if V1 is None: st.success(f"V1 = {(C2*V2)/C1}")
            if C2 is None: st.success(f"C2 = {(C1*V1)/V2}")
            if V2 is None: st.success(f"V2 = {(C1*V1)/C2}")

# ---------------- MOLARITY ----------------
elif menu == "Molarity (grams needed)":
    st.subheader("📘 Molarity Calculator")
    M = st.number_input("Molarity (M)")
    MW = st.number_input("Molecular Weight (g/mol)")
    V = st.number_input("Volume (L)")
    if st.button("Calculate"):
        st.success(f"Grams required = {M*MW*V}")

# ---------------- NORMALITY ----------------
elif menu == "Normality":
    st.subheader("📗 Normality")
    M = st.number_input("Molarity")
    n = st.number_input("n-factor")
    if st.button("Calculate"):
        st.success(f"Normality = {M*n}")

# ---------------- TEMP ----------------
elif menu == "Temperature Converter":
    st.subheader("🌡️ Temperature Converter")
    c = st.number_input("Celsius")
    if st.button("Convert to Kelvin"):
        st.success(f"{c+273.15} K")

# ---------------- PROTEIN ----------------
elif menu == "Protein Concentration":
    A280 = st.number_input("A280")
    if st.button("Calculate"):
        st.success(f"{A280*1.5} mg/mL")

# ---------------- DNA ----------------
elif menu == "DNA Concentration":
    A260 = st.number_input("A260")
    d = st.number_input("Dilution Factor")
    if st.button("Calculate"):
        st.success(f"{A260*50*d} µg/mL")

# ---------------- RNA ----------------
elif menu == "RNA Concentration":
    A260 = st.number_input("A260")
    d = st.number_input("Dilution Factor")
    if st.button("Calculate"):
        st.success(f"{A260*40*d} µg/mL")

# ---------------- PH ----------------
elif menu == "pH Calculator":
    h = st.number_input("[H+]")
    if st.button("Calculate"):
        st.success(f"pH = {-math.log10(h)}")

# ---------------- DENSITY ----------------
elif menu == "Density":
    m = st.number_input("Mass")
    v = st.number_input("Volume")
    if st.button("Calculate"):
        st.success(f"Density = {m/v}")

# ---------------- OSMOTIC ----------------
elif menu == "Osmotic Pressure":
    i = st.number_input("van’t Hoff factor")
    M = st.number_input("Molarity")
    T = st.number_input("Temperature (K)")
    if st.button("Calculate"):
        st.success(f"π = {i*M*0.0821*T} atm")

# ---------------- HARDY ----------------
elif menu == "Hardy–Weinberg Equation":
    p = st.number_input("p value")
    q = 1 - p
    st.success(f"p²={p**2}, 2pq={2*p*q}, q²={q**2}")
