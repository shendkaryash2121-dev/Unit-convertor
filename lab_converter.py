import streamlit as st

st.set_page_config(page_title="Lab Calculator", page_icon="🧪")

st.title("🧪 Laboratory Calculator")
st.write("Mass • Volume • Concentration • Molarity • Normality")

menu = st.selectbox(
    "Choose Calculator",
    [
        "Mass Converter",
        "Volume Converter",
        "Concentration (C1V1 = C2V2)",
        "Molarity by Dilution",
        "Molarity (Grams)",
        "Normality",
        "Normality by Dilution"
    ]
)

# ---------------- MASS ----------------
if menu == "Mass Converter":
    value = st.number_input("Mass value", min_value=0.0)
    from_unit = st.selectbox("From", ["kg", "g", "mg", "oz"])
    to_unit = st.selectbox("To", ["kg", "g", "mg", "oz"])

    factor = {"kg":1000, "g":1, "mg":0.001, "oz":28.35}

    if st.button("Convert"):
        result = (value * factor[from_unit]) / factor[to_unit]
        st.success(f"{value} {from_unit} = {result} {to_unit}")

# ---------------- VOLUME ----------------
elif menu == "Volume Converter":
    value = st.number_input("Volume value", min_value=0.0)
    from_unit = st.selectbox("From", ["L", "mL", "µL", "m³"])
    to_unit = st.selectbox("To", ["L", "mL", "µL", "m³"])

    factor = {"L":1, "mL":0.001, "µL":0.000001, "m³":1000}

    if st.button("Convert"):
        result = (value * factor[from_unit]) / factor[to_unit]
        st.success(f"{value} {from_unit} = {result} {to_unit}")

# ---------------- CONCENTRATION ----------------
elif menu == "Concentration (C1V1 = C2V2)":
    C1 = st.text_input("C1 (leave blank if unknown)")
    V1 = st.text_input("V1")
    C2 = st.text_input("C2")
    V2 = st.text_input("V2")

    if st.button("Calculate"):
        vals = {
            "C1": float(C1) if C1 else None,
            "V1": float(V1) if V1 else None,
            "C2": float(C2) if C2 else None,
            "V2": float(V2) if V2 else None,
        }

        if list(vals.values()).count(None) != 1:
            st.error("Leave only ONE value blank")
        else:
            if vals["C1"] is None:
                st.success(f"C1 = {(vals['C2']*vals['V2'])/vals['V1']}")
            elif vals["V1"] is None:
                st.success(f"V1 = {(vals['C2']*vals['V2'])/vals['C1']}")
            elif vals["C2"] is None:
                st.success(f"C2 = {(vals['C1']*vals['V1'])/vals['V2']}")
            elif vals["V2"] is None:
                st.success(f"V2 = {(vals['C1']*vals['V1'])/vals['C2']}")

# ---------------- MOLARITY ----------------
elif menu == "Molarity (Grams)":
    M = st.number_input("Molarity (M)", min_value=0.0)
    MW = st.number_input("Molecular Weight (g/mol)", min_value=0.0)
    V = st.number_input("Volume (L)", min_value=0.0)

    if st.button("Calculate"):
        st.success(f"Required grams = {M * MW * V}")

# ---------------- MOLARITY DILUTION ----------------
elif menu == "Molarity by Dilution":
    M2 = st.number_input("Final Molarity (M2)")
    V1 = st.number_input("Stock Volume (V1)")
    V2 = st.number_input("Final Volume (V2)")

    if st.button("Calculate M1"):
        st.success(f"M1 = {(M2 * V2) / V1}")

# ---------------- NORMALITY ----------------
elif menu == "Normality":
    M = st.number_input("Molarity (M)")
    n = st.number_input("n-factor")

    if st.button("Calculate"):
        st.success(f"Normality = {M * n}")

# ---------------- NORMALITY DILUTION ----------------
elif menu == "Normality by Dilution":
    V1 = st.number_input("Initial Volume (V1)")
    N2 = st.number_input("Final Normality (N2)")
    V2 = st.number_input("Final Volume (V2)")

    if st.button("Calculate N1"):
        st.success(f"N1 = {(N2 * V2) / V1}")
