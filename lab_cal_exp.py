import streamlit as st
import math

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Biotechnology Lab Calculator",
    page_icon="🧪",
    layout="centered"
)

# ---------------- CSS (Mobile Friendly) ----------------
st.markdown("""
<style>
body {background-color: #f7fafc;}
h1,h2,h3 {color:#0f4c5c;}
.stButton>button {
    background-color:#0f766e;
    color:white;
    width:100%;
    padding:0.6em;
    border-radius:8px;
    font-size:16px;
}
.stSelectbox>div>div {font-size:16px;}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🧪 Biotechnology Laboratory Calculator")
st.caption("Professional mobile-friendly lab calculations")

# ---------------- TOOL MENU ----------------
tool = st.selectbox(
    "Select Calculator",
    [
        "🏋️ Mass",
        "💧 Volume",
        "🌡️ Temperature Converter",
        "⚖️ Density",
        "🔬 Dilution (C₁V₁ = C₂V₂)",
        "📏 Molarity (from moles)",
        "📏 Molarity (from grams)",
        "💦 Molarity by Dilution (M₁V₁ = M₂V₂)",
        "⚡ Normality",
        "⚡ Normality by Dilution (N₁V₁ = N₂V₂)",
        "📐 Molarity → Normality",
        "📊 Molality",
        "🧪 Percentage Solutions",
        "🔹 Moles Calculation",
        "🧫 Protein",
        "🧬 DNA / RNA Concentration",
        "🧬 DNA Purity",
        "🧪 pH",
        "💧 Osmotic Pressure",
        "🔬 Hardy–Weinberg"
    ]
)

st.divider()

# ---------------- MASS ----------------
if tool == "🏋️ Mass":
    units = {"kg":1000,"g":1,"mg":0.001}
    v = st.number_input("Value",0.0)
    f = st.selectbox("From",units)
    t = st.selectbox("To",units)
    if st.button("Calculate"):
        st.success((v*units[f])/units[t])

# ---------------- VOLUME ----------------
elif tool == "💧 Volume":
    units = {"L":1,"mL":0.001,"µL":0.000001}
    v = st.number_input("Value",0.0)
    f = st.selectbox("From",units)
    t = st.selectbox("To",units)
    if st.button("Calculate"):
        st.success((v*units[f])/units[t])

# ---------------- TEMPERATURE ----------------
elif tool == "🌡️ Temperature Converter":
    c = st.selectbox("Conversion",["C→K","K→C","C→F","F→C"])
    t = st.number_input("Temperature")
    if st.button("Convert"):
        if c=="C→K": st.success(t+273.15)
        elif c=="K→C": st.success(t-273.15)
        elif c=="C→F": st.success((t*9/5)+32)
        elif c=="F→C": st.success((t-32)*5/9)

# ---------------- DENSITY ----------------
elif tool == "⚖️ Density":
    m = st.number_input("Mass (g)")
    v = st.number_input("Volume (mL)")
    if st.button("Calculate"):
        st.success(m/v)

# ---------------- C1V1 ----------------
elif tool == "🔬 Dilution (C₁V₁ = C₂V₂)":
    C1=st.number_input("C₁",0.0)
    V1=st.number_input("V₁",0.0)
    C2=st.number_input("C₂",0.0)
    V2=st.number_input("V₂",0.0)
    if st.button("Calculate"):
        if C1==0: st.success((C2*V2)/V1)
        elif V1==0: st.success((C2*V2)/C1)
        elif C2==0: st.success((C1*V1)/V2)
        elif V2==0: st.success((C1*V1)/C2)

# ---------------- MOLARITY ----------------
elif tool == "📏 Molarity (from moles)":
    n=st.number_input("Moles")
    V=st.number_input("Volume (L)")
    if st.button("Calculate"):
        st.success(n/V)

elif tool == "📏 Molarity (from grams)":
    g=st.number_input("Grams")
    mm=st.number_input("Molar mass")
    V=st.number_input("Volume (L)")
    if st.button("Calculate"):
        st.success((g/mm)/V)

# ---------------- MOLARITY DILUTION ----------------
elif tool == "💦 Molarity by Dilution (M₁V₁ = M₂V₂)":
    M1=st.number_input("M₁",0.0)
    V1=st.number_input("V₁",0.0)
    M2=st.number_input("M₂",0.0)
    V2=st.number_input("V₂",0.0)
    if st.button("Calculate"):
        if M1==0: st.success((M2*V2)/V1)
        elif V1==0: st.success((M2*V2)/M1)
        elif M2==0: st.success((M1*V1)/V2)
        elif V2==0: st.success((M1*V1)/M2)

# ---------------- NORMALITY ----------------
elif tool == "⚡ Normality":
    ge=st.number_input("Gram equivalents")
    V=st.number_input("Volume (L)")
    if st.button("Calculate"):
        st.success(ge/V)

elif tool == "⚡ Normality by Dilution (N₁V₁ = N₂V₂)":
    N1=st.number_input("N₁",0.0)
    V1=st.number_input("V₁",0.0)
    N2=st.number_input("N₂",0.0)
    V2=st.number_input("V₂",0.0)
    if st.button("Calculate"):
        if N1==0: st.success((N2*V2)/V1)
        elif V1==0: st.success((N2*V2)/N1)
        elif N2==0: st.success((N1*V1)/V2)
        elif V2==0: st.success((N1*V1)/N2)

# ---------------- MOLALITY ----------------
elif tool == "📊 Molality":
    n=st.number_input("Moles")
    kg=st.number_input("Solvent mass (kg)")
    if st.button("Calculate"):
        st.success(n/kg)

# ---------------- % SOLUTION ----------------
elif tool == "🧪 Percentage Solutions":
    a=st.number_input("Solute")
    b=st.number_input("Solution")
    if st.button("Calculate"):
        st.success((a/b)*100)

# ---------------- MOLES ----------------
elif tool == "🔹 Moles Calculation":
    g=st.number_input("Mass (g)")
    mm=st.number_input("Molar mass")
    if st.button("Calculate"):
        st.success(g/mm)

# ---------------- PROTEIN ----------------
elif tool == "🧫 Protein":
    a=st.number_input("A280")
    if st.button("Calculate"):
        st.success(a*1.5)

# ---------------- DNA RNA ----------------
elif tool == "🧬 DNA / RNA Concentration":
    t=st.selectbox("Type",["DNA","RNA"])
    a=st.number_input("A260")
    d=st.number_input("Dilution",1.0)
    f=50 if t=="DNA" else 40
    if st.button("Calculate"):
        st.success(a*f*d)

# ---------------- DNA PURITY ----------------
elif tool == "🧬 DNA Purity":
    a260=st.number_input("A260")
    a280=st.number_input("A280")
    if st.button("Calculate"):
        r=a260/a280
        st.success(r)

# ---------------- pH ----------------
elif tool == "🧪 pH":
    h=st.number_input("[H+]")
    if st.button("Calculate"):
        st.success(-math.log10(h))

# ---------------- OSMOTIC ----------------
elif tool == "💧 Osmotic Pressure":
    i=st.number_input("i")
    M=st.number_input("M")
    T=st.number_input("T (K)")
    if st.button("Calculate"):
        st.success(i*M*0.0821*T)

# ---------------- HARDY ----------------
elif tool == "🔬 Hardy–Weinberg":
    p=st.slider("p",0.0,1.0,0.5)
    q=1-p
    if st.button("Calculate"):
        st.success({"p²":p*p,"2pq":2*p*q,"q²":q*q})
