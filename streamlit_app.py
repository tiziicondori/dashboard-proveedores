import pandas as pd
import streamlit as st

st.title("Dashboard de Proveedores")

# Cargar datos (después lo conectamos a Drive)
# Limpiar nombres de columnas
df.columns = df.columns.str.strip()

# Mostrar columnas para debug
st.write("Columnas detectadas:", df.columns)

# Crear diferencia
df["Diferencia"] = df["Precio Inicial"] - df["Precio Final"]

# Filtro por secretaría
secretaria = st.selectbox("Seleccionar Secretaría", df["secretaria"].unique())
df_filtrado = df[df["secretaria"] == secretaria]

# Agrupar (tipo tabla dinámica)
resumen = df_filtrado.groupby("proveedor").sum(numeric_only=True)

st.dataframe(resumen)

st.bar_chart(resumen["diferencia"])
