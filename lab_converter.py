import streamlit as st
import math

st.set_page_config(
    page_title="Complete Lab Science Calculator",
    page_icon="🧪",
    layout="centered"
)

st.title("🧪 Complete Laboratory Science Calculator")
st.caption("Chemistry • Biotechnology • Molecular Biology • Genetics")

category = st.selectbox(
    "Choose Category",
    [
        "Basic Unit Conversions",
        "Solution Chemistry",
        "Physical Chemistry",
        "Biomolecular Calculations",
        "Genetics"
    ]
)

# ======================================================
# BASIC UNIT CONVERSIONS
# ======================================================
if category == "Basic Unit Conversions":

    tool = st.selectbox(
        "Select Tool",
        ["Mass Converter", "Volume Converter", "Temperature Converter"]
    )

    if tool == "Mass Converter":
        value = st.number_input("Mass value", min_value=0.0)
        f = st.selectbox("From", ["kg", "g", "mg", "oz"])
        t = st.selectbox("To", ["kg", "g", "mg", "oz"])
        factor = {"kg":1000, "g":1, "mg":0.001, "oz":28.35}
        if st.button("Convert"):
            st.success(f"{value} {f} = {(value*factor[f]/factor[t]):.4f} {t}")

    elif tool == "Volume Converter":
        value = st.number_input("Volume value", min_value=0.0)
        f = st.selectbox("From", ["L", "mL", "µL", "m³"])
        t = st.selectbox("To", ["L", "mL", "µL", "m³"])
        factor = {"L":1, "mL":0.001, "µL":0.000001, "m³":1000}
        if st.button("Convert"):
            st.success(f"{value} {f} = {(value*factor[f]/factor[t]):.6f} {t}")

    elif tool == "Temperature Converter":
        option = st.selectbox(
            "Conversion",
            [
                "Celsius → Kelvin",
                "Kelvin → Celsius",
                "Fahrenheit → Celsius",
                "Celsius → Fahrenheit",
                "Kelvin → Fahrenheit",
                "Fahrenheit → Kelvin"
            ]
        )
        temp = st.number_input("Temperature")

        if st.button("Convert"):
            if option == "Celsius → Kelvin":
                st.success(temp + 273.15)
            elif option == "Kelvin → Celsius":
                st.success(temp - 273.15)
            elif option == "Fahrenheit → Celsius":
                st.success((temp - 32) * 5/9)
            elif option == "Celsius → Fahrenheit":
                st.success(temp * 9/5 + 32)
            elif option == "Kelvin → Fahrenheit":
                st.success((temp - 273.15) * 9/5 + 32)
            elif option == "Fahrenheit → Kelvin":
                st.success((temp - 32) * 5/9 + 273.15)

# ======================================================
# SOLUTION CHEMISTRY
# ======================================================
elif category == "Solution Chemistry":

    tool = st.selectbox(
        "Select Tool",
        [
            "Concentration (C1V1 = C2V2)",
            "Molarity (grams required)",
            "Molarity by Dilution",
            "Normality by Dilution",
            "Molarity → Normality",
            "Percentage Solutions",
            "Molality"
        ]
    )

    if tool == "Concentration (C1V1 = C2V2)":
        C1 = st.text_input("C1")
        V1 = st.text_input("V1")
        C2 = st.text_input("C2")
        V2 = st.text_input("V2")

        if st.button("Calculate"):
            vals = [C1, V1, C2, V2]
            if vals.count("") != 1:
                st.error("Leave exactly ONE value empty")
            else:
                C1 = float(C1) if C1 else None
                V1 = float(V1) if V1 else None
                C2 = float(C2) if C2 else None
                V2 = float(V2) if V2 else None

                if C1 is None:
                    st.success((C2 * V2) / V1)
                elif V1 is None:
                    st.success((C2 * V2) / C1)
                elif C2 is None:
                    st.success((C1 * V1) / V2)
                else:
                    st.success((C1 * V1) / C2)

    elif tool == "Molarity (grams required)":
        M = st.number_input("Molarity (M)")
        MW = st.number_input("Molecular weight (g/mol)")
        V = st.number_input("Volume (L)")
        if st.button("Calculate"):
            st.success(f"{M*MW*V:.4f} g")

    elif tool == "Molarity by Dilution":
        M1 = st.text_input("M1")
        V1 = st.text_input("V1")
        M2 = st.text_input("M2")
        V2 = st.text_input("V2")
        if st.button("Calculate"):
            vals = [M1, V1, M2, V2]
            if vals.count("") != 1:
                st.error("Leave exactly ONE blank")
            else:
                M1 = float(M1) if M1 else None
                V1 = float(V1) if V1 else None
                M2 = float(M2) if M2 else None
                V2 = float(V2) if V2 else None

                if M1 is None:
                    st.success((M2*V2)/V1)
                elif V1 is None:
                    st.success((M2*V2)/M1)
                elif M2 is None:
                    st.success((M1*V1)/V2)
                else:
                    st.success((M1*V1)/M2)

    elif tool == "Normality by Dilution":
        N1 = st.text_input("N1")
        V1 = st.text_input("V1")
        N2 = st.text_input("N2")
        V2 = st.text_input("V2")
        if st.button("Calculate"):
            vals = [N1, V1, N2, V2]
            if vals.count("") != 1:
                st.error("Leave exactly ONE blank")
            else:
                N1 = float(N1) if N1 else None
                V1 = float(V1) if V1 else None
                N2 = float(N2) if N2 else None
                V2 = float(V2) if V2 else None

                if N1 is None:
                    st.success((N2*V2)/V1)
                elif V1 is None:
                    st.success((N2*V2)/N1)
                elif N2 is None:
                    st.success((N1*V1)/V2)
                else:
                    st.success((N1*V1)/N2)

    elif tool == "Molarity → Normality":
        M = st.number_input("Molarity (M)")
        n = st.number_input("n-factor")
        if st.button("Convert"):
            st.success(M * n)

    elif tool == "Percentage Solutions":
        option = st.selectbox("% Type", ["w/v", "v/v", "m/v"])
        if option == "w/v":
            g = st.number_input("Grams")
            v = st.number_input("Volume (mL)")
            st.success((g/v)*100 if v else 0)
        elif option == "v/v":
            vs = st.number_input("Volume solute (mL)")
            vt = st.number_input("Volume solution (mL)")
            st.success((vs/vt)*100 if vt else 0)
        elif option == "m/v":
            m = st.number_input("Mass (g)")
            v = st.number_input("Volume (mL)")
            st.success((m/v)*100 if v else 0)

    elif tool == "Molality":
        moles = st.number_input("Moles of solute")
        kg = st.number_input("Mass of solvent (kg)")
        if st.button("Calculate"):
            st.success(moles / kg)

# ======================================================
# PHYSICAL CHEMISTRY
# ======================================================
elif category == "Physical Chemistry":

    tool = st.selectbox(
        "Select Tool",
        ["pH Calculator", "Density", "Osmotic Pressure"]
    )

    if tool == "pH Calculator":
        h = st.number_input("[H+] (M)")
        if st.button("Calculate"):
            st.success(-math.log10(h))

    elif tool == "Density":
        m = st.number_input("Mass")
        v = st.number_input("Volume")
        if st.button("Calculate"):
            st.success(m/v)

    elif tool == "Osmotic Pressure":
        i = st.number_input("van't Hoff factor")
        M = st.number_input("Molarity")
        T = st.number_input("Temperature (K)")
        if st.button("Calculate"):
            st.success(i * M * 0.0821 * T)

# ======================================================
# BIOMOLECULAR
# ======================================================
elif category == "Biomolecular Calculations":

    tool = st.selectbox(
        "Select Tool",
        [
            "Protein Concentration",
            "DNA Concentration",
            "RNA Concentration",
            "DNA Purity"
        ]
    )

    if tool == "Protein Concentration":
        A280 = st.number_input("A280")
        if st.button("Calculate"):
            st.success(f"{A280*1.5:.3f} mg/mL")

    elif tool == "DNA Concentration":
        A260 = st.number_input("A260")
        d = st.number_input("Dilution factor")
        if st.button("Calculate"):
            st.success(f"{A260*50*d} µg/mL")

    elif tool == "RNA Concentration":
        A260 = st.number_input("A260")
        d = st.number_input("Dilution factor")
        if st.button("Calculate"):
            st.success(f"{A260*40*d} µg/mL")

    elif tool == "DNA Purity":
        A260 = st.number_input("A260")
        A280 = st.number_input("A280")
        if st.button("Calculate"):
            st.success(A260/A280)

# ======================================================
# GENETICS
# ======================================================
elif category == "Genetics":
    st.subheader("Hardy–Weinberg Equation")
    p = st.number_input("Allele frequency (p)", min_value=0.0, max_value=1.0)
    q = 1 - p
    st.success({
        "p²": p**2,
        "2pq": 2*p*q,
        "q²": q**2,
        "Total": p**2 + 2*p*q + q**2
    })
