import streamlit as st
from motor import analizar_muro
from graficos import dibujar_muro
from fpdf import FPDF

st.set_page_config(page_title="Muro Mampostería", layout="wide")
st.title("🧱 Diseño de Muro de Mampostería (2.0 tonf/m³)")

# Entradas en la barra lateral
with st.sidebar:
    st.header("📐 Dimensiones")
    gamma_m = st.number_input("Peso muro (tonf/m³)", value=1.8)
    H = st.number_input("Altura H (m)", value=2.8)
    B = st.number_input("Base B (m)", value=1.7)
    t = st.number_input("Corona t (m)", value=0.4)
    hz = st.number_input("Profundidad(m)", value=0.5)
    st.header("🌱 Suelo")
    gamma_s = st.number_input("Peso suelo (tonf/m³)", value=1.8)
    phi = st.number_input("Ángulo φ (°)", value=30.0)
    q_adm = st.number_input("Capacidad admisible (tonf/m²)", value=15.0)

if st.button("🚀 REALIZAR ANÁLISIS"):
    # Ejecutar cálculos
    res = analizar_muro(H, B, t, gamma_m, gamma_s, phi, hz)
    
    # 1. Mostrar Resultados en pantalla
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("FS Volcamiento >=2", f"{res['FS_vol']:.2f}")
    c2.metric("FS Deslizamiento >=1.5", f"{res['FS_des']:.2f}")
    c3.metric("FS Deslizamiento_pasivo",f"{res['FS_despasivo']:.2f}")
    c4.metric("Presión Máxima",f"{res['q_max']:.2f} ton/m²")


    # 2. Gráfico descriptivo
    st.write("### Esquema de Fuerzas")
    fig = dibujar_muro(H, B, t, res['Pa'], res['W_total'])
    st.pyplot(fig)

    # 3. Generación de PDF (Sin errores de librerías)
    '''st.divider()
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 10, "REPORTE TÉCNICO DE INGENIERÍA", ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Helvetica", "", 12)
        pdf.cell(0, 10, f"Proyecto: Muro de Gravedad (Mampostería)", ln=True)
        pdf.cell(0, 10, f"Geometría: H={H}m, B={B}m, t={t}m", ln=True)
        pdf.ln(5)
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 10, "RESULTADOS:", ln=True)
        pdf.set_font("Helvetica", "", 12)
        pdf.cell(0, 10, f"- FS Volcamiento: {res['FS_vol']:.2f}", ln=True)
        pdf.cell(0, 10, f"- FS Deslizamiento: {res['FS_des']:.2f}", ln=True)
        pdf.cell(0, 10, f"- Presión Máxima: {res['q_max']:.2f} tonf/m2", ln=True)
        
        # Generar salida binaria
        pdf_output = pdf.output() 
        
        st.download_button(
            label="📥 DESCARGAR MEMORIA DE CÁLCULO (PDF)",
            data=bytes(pdf_output),
            file_name=f"Memoria_Muro_{H}m.pdf",
            mime="application/pdf"
        )
        st.success("¡Análisis completado! El reporte está listo para descargar.")
    except Exception as e:
        st.error(f"Error al preparar el PDF: {e}")'''
