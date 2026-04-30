import streamlit as st

# Configuración de pantalla
st.set_page_config(page_title="SISTEMA CENTRAL | EMILIO", layout="wide")

# ESTILO GÓTICO AVANZADO (CSS)
st.markdown("""
    <style>
    /* Fondo Negro Absoluto */
    .stApp {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Courier New', Courier, monospace;
    }

    /* Ocultar elementos innecesarios de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Contenedor de Proyectos */
    .project-card {
        border: 1px solid #333333;
        padding: 20px;
        transition: 0.5s;
        margin-bottom: 20px;
    }
    
    .project-card:hover {
        border: 1px solid #ffffff;
        background-color: #111111;
    }

    /* Botones de Ejecución */
    .stButton>button {
        width: 100%;
        background-color: #000000;
        color: #ffffff;
        border: 1px solid #ffffff;
        border-radius: 0px;
        letter-spacing: 3px;
        font-weight: bold;
        height: 45px;
    }

    .stButton>button:hover {
        background-color: #ffffff;
        color: #000000;
    }

    /* Títulos */
    h1, h2 {
        letter-spacing: 10px;
        text-align: center;
        text-transform: uppercase;
        border-bottom: 2px solid #ffffff;
        padding-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# ENCABEZADO DEL SISTEMA
st.markdown("<h1>SISTEMA CENTRAL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; letter-spacing: 5px;'>LABORATORIO DE INGENIERÍA FÍSICA // EMILIO</p>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# CUADRÍCULA DE PROYECTOS (Aquí irás sumando hasta 20)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class='project-card'>
            <h3>01. BALÍSTICA</h3>
            <p>Simulación de proyectiles con arrastre aerodinámico en entornos variables.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("ACCEDER _ 01"):
        st.switch_page("pages/1_balistica.py")

with col2:
    st.markdown("""
        <div class='project-card'>
            <h3>02. FINANZAS</h3>
            <p>Modelado estocástico de activos mediante Movimiento Browniano Geométrico.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("ACCEDER _ 02"):
        st.switch_page("pages/2_finanzas.py")

with col3:
    st.markdown("""
        <div class='project-card' style='opacity: 0.3;'>
            <h3>03. ???</h3>
            <p>Módulo de sistema encriptado. Pendiente de desarrollo...</p>
        </div>
    """, unsafe_allow_html=True)
    st.button("BLOQUEADO", disabled=True)

# PIE DE PÁGINA TÉCNICO
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
st.code("LOG_DATA: User_Emilio_Access_Granted... Loading_Ecosystem_V.2.0", language=None)