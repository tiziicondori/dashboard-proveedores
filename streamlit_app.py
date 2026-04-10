import pandas as pd
import streamlit as st

st.title("Dashboard de Proveedores")

# 1️⃣ PRIMERO cargar el archivo
df = pd.read_excel("comparativa de precios.xlsx")

# 2️⃣ DESPUÉS limpiar columnas
df.columns = df.columns.str.strip()

# 3️⃣ Mostrar columnas (debug)
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
