import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# 1. Configuración de la página
st.set_page_config(page_title="Simulador Quant - Dark Edition", layout="wide")

# 2. AQUÍ PONES EL DISEÑO DE LAS MÉTRICAS (CSS)
st.markdown("""
    <style>
    /* Fondo de la app negro */
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    
    /* Cuadros de métricas estilo gótico: bordes blancos y cuadrados */
    [data-testid="stMetric"] {
        border: 1px solid #ffffff;
        padding: 20px;
        background-color: #000000;
        text-align: center;
    }

    /* Color de los títulos de las métricas */
    [data-testid="stMetricLabel"] {
        color: #ffffff !important;
        font-family: 'Courier New', monospace;
        letter-spacing: 2px;
    }

    /* Color de los números de las métricas */
    [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-family: 'Courier New', monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. El resto de tu código (Título, Sliders y lógica)
st.title("ⱴ MONTE CARLO ENGINE")
# ... (aquí sigue todo el código que ya teníamos)
# Sidebar - Parámetros de Ingeniería Financiera
with st.sidebar:
    st.header("Configuración del Modelo")
    S0 = st.number_input("Precio Inicial (USD)", value=100.0)
    mu = st.slider("Retorno Esperado (Drift %)", -20.0, 50.0, 10.0) / 100
    sigma = st.slider("Volatilidad Anual (Sigma %)", 1.0, 100.0, 25.0) / 100
    t_dias = st.number_input("Días a simular", value=252) # 252 días hábiles tiene un año
    n_sim = st.number_input("Número de Simulaciones", value=50, step=10)

# El motor del modelo: Movimiento Browniano Geométrico
# Formula: S(t) = S(0) * exp((mu - 0.5 * sigma^2) * t + sigma * W(t))
dt = 1/252
precios = np.zeros((t_dias, n_sim))
precios[0] = S0

for t in range(1, t_dias):
    # Generamos ruido blanco gaussiano (física pura)
    z = np.random.standard_normal(n_sim)
    precios[t] = precios[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)

# Visualización con Estilo Gótico Industrial
fig = go.Figure()

for i in range(n_sim):
    fig.add_trace(go.Scatter(
        y=precios[:, i], 
        mode='lines', 
        # Líneas blancas muy delgadas y semi-transparentes
        line=dict(width=0.5, color='rgba(255, 255, 255, 0.2)'), 
        showlegend=False,
        hoverinfo='none' # Para que no estorbe al pasar el mouse
    ))

# Resaltar la trayectoria promedio o la última con un blanco sólido
fig.add_trace(go.Scatter(
    y=precios.mean(axis=1),
    mode='lines',
    line=dict(color='#ffffff', width=2),
    name='Tendencia Central'
))

fig.update_layout(
    title="ⱴ PROYECCIONES ESTOCÁSTICAS (MONTE CARLO)",
    xaxis_title="TIEMPO (DÍAS HÁBILES)",
    yaxis_title="VALOR DEL ACTIVO (USD)",
    template="plotly_dark",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(family="Courier New, monospace", color="#ffffff"),
    xaxis=dict(showgrid=False, zeroline=True, zerolinecolor='#444444'),
    yaxis=dict(showgrid=False, zeroline=True, zerolinecolor='#444444'),
    margin=dict(l=10, r=10, t=50, b=10)
)

# Análisis Estadístico
st.subheader("📊 Análisis de Riesgo")
final_prices = precios[-1, :]
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Precio Promedio Final", f"${final_prices.mean():.2f}")
with col2:
    prob_ganar = (final_prices > S0).sum() / n_sim * 100
    st.metric("Probabilidad de Ganancia", f"{prob_ganar:.1f}%")
with col3:
    var_95 = np.percentile(final_prices, 5)
    st.metric("Valor en Riesgo (VaR 95%)", f"${var_95:.2f}")

st.info(f"El VaR 95% significa que hay solo un 5% de probabilidad de que el precio caiga por debajo de ${var_95:.2f}")
