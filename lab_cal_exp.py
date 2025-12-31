import streamlit as st
import math

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="Biotechnology Lab Calculator",
    page_icon="🧪",
    layout="centered"
)

# ======================================================
# CUSTOM DARK THEME CSS (UNCHANGED)
# ======================================================
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
    background-color: #0e1117;
    color: #e6e6e6;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 900px;
}
h1, h2, h3 {
    color: #ffffff;
    font-weight: 700;
}
h1 {
    text-align: center;
    margin-bottom: 0.2rem;
}
.subtitle {
    text-align: center;
    color: #9aa4b2;
    font-size: 0.95rem;
    margin-bottom: 2rem;
}
.card {
    background: #161b22;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 0 0 1px rgba(255,255,255,0.05);
}
input, select, textarea {
    background-color: #0e1117 !important;
    color: #ffffff !important;
    border-radius: 8px !important;
    border: 1px solid #30363d !important;
}
.stButton > button {
    background: linear-gradient(135deg, #1f6feb, #388bfd);
    color: white;
    border-radius: 10px;
    padding: 0.6rem 1.2rem;
    border: none;
    font-size: 0.95rem;
    font-weight: 600;
}
.footer {
    text-align: center;
    color: #6e7681;
    font-size: 0.8rem;
    margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# TITLE
# ======================================================
st.title("🧪 Biotechnology Laboratory Calculator")
st.markdown('<p class="subtitle">Chemical & Biological Calculation Toolkit</p>', unsafe_allow_html=True)

# ======================================================
# TOOL SELECTION
# ======================================================
tool = st.selectbox(
    "Select Calculation Tool",
    [
        "Mass",
        "Volume",
        "Temperature",
        "Density",
        "Dilution (C₁V₁ = C₂V₂)",
        "Molarity (from moles)",
        "Molarity (from grams)",
        "Molarity by dilution",
        "Molality",
        "Normality",
        "Normality by dilution",
        "Molarity → Normality",
        "Moles calculation",
        "Percentage solution",
        "DNA concentration",
        "RNA concentration",
        "DNA purity (260/280)",
        "Osmotic pressure",
        "Hardy–Weinberg equation"
    ]
)

st.markdown('<div class="card">', unsafe_allow_html=True)

# ======================================================
# CALCULATORS
# ======================================================

if tool == "Mass":
    m = st.number_input("Mass", min_value=0.0)
    unit = st.selectbox("Unit", ["kg", "g", "mg"])
    if unit == "kg":
        st.success(f"{m*1000:.2f} g")
    elif unit == "g":
        st.success(f"{m/1000:.4f} kg | {m*1000:.2f} mg")
    else:
        st.success(f"{m/1000:.4f} g")

elif tool == "Volume":
    v = st.number_input("Volume", min_value=0.0)
    unit = st.selectbox("Unit", ["L", "mL"])
    st.success(f"{v*1000:.2f} mL" if unit == "L" else f"{v/1000:.4f} L")

elif tool == "Temperature":
    t = st.number_input("Temperature")
    unit = st.selectbox("Convert from", ["Celsius", "Fahrenheit", "Kelvin"])
    if unit == "Celsius":
        st.success(f"{(t*9/5)+32:.2f} °F | {t+273.15:.2f} K")
    elif unit == "Fahrenheit":
        st.success(f"{(t-32)*5/9:.2f} °C")
    else:
        st.success(f"{t-273.15:.2f} °C")

elif tool == "Density":
    m = st.number_input("Mass (g)")
    v = st.number_input("Volume (mL)")
    if v > 0:
        st.success(f"Density = {m/v:.3f} g/mL")

elif tool == "Dilution (C₁V₁ = C₂V₂)":
    c1 = st.number_input("C₁")
    v1 = st.number_input("V₁")
    c2 = st.number_input("C₂")
    if c2 > 0:
        st.success(f"V₂ = {(c1*v1)/c2:.2f}")

elif tool == "Molarity (from moles)":
    n = st.number_input("Moles")
    v = st.number_input("Volume (L)")
    if v > 0:
        st.success(f"M = {n/v:.4f}")

elif tool == "Molarity (from grams)":
    g = st.number_input("Grams of solute")
    mw = st.number_input("Molecular weight")
    v = st.number_input("Volume (L)")
    if mw > 0 and v > 0:
        st.success(f"M = {(g/mw)/v:.4f}")

elif tool == "Molarity by dilution":
    m1 = st.number_input("M₁")
    v1 = st.number_input("V₁")
    v2 = st.number_input("V₂")
    if v2 > 0:
        st.success(f"M₂ = {(m1*v1)/v2:.4f}")

# ================= NEW =================
elif tool == "Molality":
    moles = st.number_input("Moles of solute")
    solvent = st.number_input("Mass of solvent (kg)")
    if solvent > 0:
        st.success(f"Molality (m) = {moles/solvent:.4f}")

elif tool == "Percentage solution":
    ptype = st.selectbox("Select type", ["%(w/v)", "%(v/v)", "%(m/v)"])

    if ptype == "%(w/v)":
        g = st.number_input("Grams of solute")
        v = st.number_input("Volume of solution (mL)")
        if v > 0:
            st.success(f"% (w/v) = {(g/v)*100:.2f}%")

    elif ptype == "%(v/v)":
        vs = st.number_input("Volume of solute (mL)")
        v = st.number_input("Volume of solution (mL)")
        if v > 0:
            st.success(f"% (v/v) = {(vs/v)*100:.2f}%")

    else:
        g = st.number_input("Mass of solute (g)")
        v = st.number_input("Volume of solution (mL)")
        if v > 0:
            st.success(f"% (m/v) = {(g/v)*100:.2f}%")

elif tool == "Normality":
    m = st.number_input("Molarity")
    n = st.number_input("n-factor")
    st.success(f"N = {m*n:.4f}")

elif tool == "Normality by dilution":
    n1 = st.number_input("N₁")
    v1 = st.number_input("V₁")
    v2 = st.number_input("V₂")
    if v2 > 0:
        st.success(f"N₂ = {(n1*v1)/v2:.4f}")

elif tool == "Molarity → Normality":
    m = st.number_input("Molarity")
    n = st.number_input("n-factor")
    st.success(f"Normality = {m*n:.4f}")

elif tool == "Moles calculation":
    g = st.number_input("Grams")
    mw = st.number_input("Molecular weight")
    if mw > 0:
        st.success(f"Moles = {g/mw:.4f}")

elif tool == "DNA concentration":
    a260 = st.number_input("A260")
    st.success(f"DNA = {a260*50:.2f} µg/mL")

elif tool == "RNA concentration":
    a260 = st.number_input("A260")
    st.success(f"RNA = {a260*40:.2f} µg/mL")

elif tool == "DNA purity (260/280)":
    a260 = st.number_input("A260")
    a280 = st.number_input("A280")
    if a280 > 0:
        st.success(f"Purity ratio = {a260/a280:.2f}")

elif tool == "Osmotic pressure":
    m = st.number_input("Molarity")
    t = st.number_input("Temperature (K)")
    st.success(f"π = {m*0.0821*t:.2f} atm")

elif tool == "Hardy–Weinberg equation":
    p = st.number_input("p", max_value=1.0)
    q = 1 - p
    st.success(f"p²={p*p:.3f} | 2pq={2*p*q:.3f} | q²={q*q:.3f}")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="footer">© Biotechnology Laboratory Calculator</div>', unsafe_allow_html=True)
