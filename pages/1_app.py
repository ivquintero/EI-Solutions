import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(page_title="Ingeniería Física - Simulador Pro", layout="wide")

st.title("🚀 Simulador de Trayectorias de Alta Precisión")
st.markdown("---")

# --- BARRA LATERAL PARA PARÁMETROS ---
st.sidebar.header("Parámetros Físicos")
v0 = st.sidebar.slider("Velocidad Inicial (m/s)", 10.0, 500.0, 150.0)
angle = st.sidebar.slider("Ángulo de Lanzamiento (°)", 0.0, 90.0, 45.0)
m = st.sidebar.number_input("Masa del Objeto (kg)", value=1.0)
c_d = st.sidebar.slider("Coeficiente de Arrastre (Cd)", 0.0, 1.0, 0.47) # 0.47 es una esfera
rho = 1.225  # Densidad del aire (kg/m^3)
g = 9.81     # Gravedad

# --- CÁLCULO NUMÉRICO (Método de Euler) ---
dt = 0.01  # Paso de tiempo
x, y = [0.0], [0.0]
vx = v0 * np.cos(np.radians(angle))
vy = v0 * np.sin(np.radians(angle))

while y[-1] >= 0:
    v = np.sqrt(vx**2 + vy**2)
    # Fuerza de arrastre: Fd = 1/2 * rho * v^2 * Cd * Area (asumiendo Area=0.01m2)
    fd = 0.5 * rho * v**2 * c_d * 0.01
    
    ax = -(fd * (vx / v)) / m
    ay = -g - (fd * (vy / v)) / m
    
    vx += ax * dt
    vy += ay * dt
    x.append(x[-1] + vx * dt)
    y.append(y[-1] + vy * dt)

# --- VISUALIZACIÓN ---
fig = go.Figure()

# Línea blanca pura para un contraste gótico sobre fondo negro
fig.add_trace(go.Scatter(
    x=x, 
    y=y, 
    mode='lines', 
    name='Trayectoria', 
    line=dict(color='#ffffff', width=2) # Blanco puro y fino
))

fig.update_layout(
    title="⌖ ANÁLISIS DE TRAYECTORIA",
    xaxis_title="DISTANCIA (m)",
    yaxis_title="ALTURA (m)",
    template="plotly_dark",
    paper_bgcolor='rgba(0,0,0,0)', # Fondo transparente para que use el negro de la app
    plot_bgcolor='rgba(0,0,0,0)',  # Fondo del gráfico transparente
    font=dict(family="Courier New, monospace", color="#ffffff"), # Fuente de terminal
    xaxis=dict(showgrid=False, zeroline=True, zerolinewidth=1, zerolinecolor='#333333'), # Sin rejilla, solo ejes
    yaxis=dict(showgrid=False, zeroline=True, zerolinewidth=1, zerolinecolor='#333333'),
    margin=dict(l=20, r=20, t=50, b=20)
)

col1, col2 = st.columns([2, 1])
with col1:
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.metric("Alcance Máximo", f"{max(x):.2f} m")
    st.metric("Altura Máxima", f"{max(y):.2f} m")
    st.write("**Análisis Técnico:** El modelo utiliza integración numérica para resolver las ecuaciones de movimiento con arrastre cuadrático.")

st.success("App funcional lista para portafolio.")

