import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF

# Základní nastavení
st.title("Body na kružnici")
st.sidebar.header("Vstupní parametry")

# Vstupy od uživatele
x_center = st.sidebar.number_input("X souřadnice středu", value=0.0)
y_center = st.sidebar.number_input("Y souřadnice středu", value=0.0)
radius = st.sidebar.number_input("Poloměr kružnice (m)", min_value=0.1, value=1.0)
num_points = st.sidebar.slider("Počet bodů", min_value=3, max_value=500, value=10)
color = st.sidebar.color_picker("Barva bodů", "#FF0000")

# Výpočet bodů
angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
x_points = x_center + radius * np.cos(angles)
y_points = y_center + radius * np.sin(angles)

# Vykreslení grafu
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.plot(x_points, y_points, 'o', color=color)
circle = plt.Circle((x_center, y_center), radius, fill=False, linestyle='--')
ax.add_artist(circle)
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.grid(True)
st.pyplot(fig)

# Informace o aplikaci
if st.checkbox("Zobrazit informace o aplikaci"):
    st.markdown("""
    ### O aplikaci
    - Autor: Aneta Kolářová
    - Kontakt: 277999@vutbr.cz
    - Technologie: Python, Streamlit, Matplotlib, FPDF
    - Tato aplikace byla vytvořena pomocí umělé inteligence Microsoft Copilot          
    """)

# Export do PDF
if st.button("Exportovat do PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Body na kruznici – Vystup", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Stred: ({x_center}, {y_center})", ln=True)
    pdf.cell(200, 10, txt=f"Polomer: {radius} m", ln=True)
    pdf.cell(200, 10, txt=f"Pocet bodu: {num_points}", ln=True)
    pdf.cell(200, 10, txt=f"Barva bodu: {color}", ln=True)
    pdf.output("vystup_kruznice.pdf")
    st.success("PDF bylo vytvořeno jako 'vystup_kruznice.pdf'.")

