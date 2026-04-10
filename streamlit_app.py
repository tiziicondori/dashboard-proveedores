import pandas as pd
import streamlit as st

st.title("Dashboard de Proveedores")

# Cargar datos (después lo conectamos a Drive)
df = pd.read_csv("datos.csv")

# Crear diferencia
df["diferencia"] = df["precio_inicial"] - df["precio_final"]

# Filtro por secretaría
secretaria = st.selectbox("Seleccionar Secretaría", df["secretaria"].unique())
df_filtrado = df[df["secretaria"] == secretaria]

# Agrupar (tipo tabla dinámica)
resumen = df_filtrado.groupby("proveedor").sum(numeric_only=True)

st.dataframe(resumen)

st.bar_chart(resumen["diferencia"])
