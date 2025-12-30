import streamlit as st
import math

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="Complete Lab Science Calculator",
    page_icon="🧪",
    layout="centered"
)

# ======================================================
# NUDE / SCIENTIFIC THEME (CUSTOM CSS)
# ======================================================
st.markdown("""
<style>
html, body, [class*="css"]  {
    background-color: #f6f2ee;
    color: #3b3b3b;
    font-family: 'Segoe UI', sans-serif;
}

h1, h2, h3 {
    color: #3a2f2a;
}

.card {
    background-color: #ffffff;
    padding: 1.5rem;
    border-radius: 14px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.05);
    margin-bottom: 1.5rem;
}

.stButton>button {
    background-color: #c9a27c;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 0.5rem 1rem;
}

.stButton>button:hover {
    background-color: #b08a66;
}

.stSelectbox, .stNumberInput, .stTextInput {
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# HEADER
# ======================================================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.title("🧪 Complete Laboratory Science Calculator")
st.caption("Chemistry • Biotechnology • Molecular Biology • Genetics")
st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# CATEGORY SELECTION
# ======================================================
st.markdown("<div class='card'>", unsafe_allow_html=True)
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
st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# BASIC UNIT CONVERSIONS
# ======================================================
if category == "Basic Unit Conversions":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    tool = st.selectbox(
        "Select Tool",
        ["Mass Converter", "Volume Converter", "Temperature Converter"]
    )

    if tool == "Mass Converter":
        value = st.number_input("Mass value", min_value=0.0)
        f = st.selectbox("From unit", ["kg", "g", "mg", "oz"])
        t = st.selectbox("To unit", ["kg", "g", "mg", "oz"])
        factor = {"kg":1000, "g":1, "mg":0.001, "oz":28.35}
        if st.button("Convert"):
            st.success(f"{value} {f} = {(value*factor[f]/factor[t]):.4f} {t}")

    elif tool == "Volume Converter":
        value = st.number_input("Volume value", min_value=0.0)
        f = st.selectbox("From unit", ["L", "mL", "µL", "m³"])
        t = st.selectbox("To unit", ["L", "mL", "µL", "m³"])
        factor = {"L":1, "mL":0.001, "µL":0.000001, "m³":1000}
        if st.button("Convert"):
            st.success(f"{value} {f} = {(value*factor[f]/factor[t]):.6f} {t}")

    elif tool == "Temperature Converter":
        option = st.selectbox(
            "Conversion Type",
            [
                "Celsius → Kelvin",
                "Kelvin → Celsius",
                "Fahrenheit → Celsius",
                "Celsius → Fahrenheit",
                "Kelvin → Fahrenheit",
                "Fahrenheit → Kelvin"
            ]
        )
        temp = st.number_input("Temperature value")

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
    st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# SOLUTION CHEMISTRY
# ======================================================
elif category == "Solution Chemistry":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    tool = st.selectbox(
        "Select Tool",
        [
            "C1V1 = C2V2",
            "Molarity (grams required)",
            "Molarity by Dilution",
            "Normality by Dilution",
            "Molarity → Normality",
            "Percentage Solutions",
            "Molality"
        ]
    )

    if tool == "C1V1 = C2V2":
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

    elif tool == "Percentage Solutions":
        option = st.selectbox("% Type", ["w/v", "v/v", "m/v"])
        if option == "w/v":
            g = st.number_input("Grams of solute")
            v = st.number_input("Volume (mL)")
            if st.button("Calculate"):
                st.success((g/v)*100 if v else 0)

    st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# BIOMOLECULAR
# ======================================================
elif category == "Biomolecular Calculations":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
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
    st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# GENETICS
# ======================================================
elif category == "Genetics":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Hardy–Weinberg Equation")
    p = st.number_input("Allele frequency (p)", min_value=0.0, max_value=1.0)
    q = 1 - p
    st.success({
        "p²": p**2,
        "2pq": 2*p*q,
        "q²": q**2,
        "Total": p**2 + 2*p*q + q**2
    })
    st.markdown("</div>", unsafe_allow_html=True)
