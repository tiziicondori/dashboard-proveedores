import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dashboard de Proveedores", layout="wide")

st.title("📊 Dashboard de Comparativa de Precios")

# Cargar archivo
df = pd.read_excel("comparativa de precios.xlsx")

# Limpiar nombres de columnas
df.columns = df.columns.str.strip().str.lower()

def limpiar_numero(col):
    return pd.to_numeric(
        col.astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .str.replace("-", "", regex=False)
        .str.strip(),
        errors="coerce"  # 🔥 esto evita que rompa
    )

df["precio inicial"] = limpiar_numero(df["precio inicial"])
df["precio final"] = limpiar_numero(df["precio final"])

# Crear diferencia
df["diferencia"] = df["precio inicial"] - df["precio final"]

# FILTROS
st.sidebar.header("Filtros")

secretaria = st.sidebar.selectbox(
    "Secretaría",
    ["todas"] + list(df["secretaria"].dropna().unique())
)

direccion = st.sidebar.selectbox(
    "Dirección / Subsecretaría",
    ["todas"] + list(df["dir. o sub. sec."].dropna().unique())
)

# Aplicar filtros
df_filtrado = df.copy()

if secretaria != "todas":
    df_filtrado = df_filtrado[df_filtrado["secretaria"] == secretaria]

if direccion != "todas":
    df_filtrado = df_filtrado[df_filtrado["dir. o sub. sec."] == direccion]

# AGRUPACIÓN
resumen = df_filtrado.groupby("proveedores").agg({
    "precio inicial": "sum",
    "precio final": "sum",
    "diferencia": "sum"
}).reset_index()

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Inicial", f"${resumen['precio inicial'].sum():,.0f}")
col2.metric("💸 Total Final", f"${resumen['precio final'].sum():,.0f}")
col3.metric("📉 Ahorro Total", f"${resumen['diferencia'].sum():,.0f}")

st.divider()

# TABLA
st.subheader("📋 Resumen por Proveedor")
st.dataframe(resumen, use_container_width=True)

# GRÁFICO
st.subheader("📊 Diferencia por Proveedor")
st.bar_chart(resumen.set_index("proveedores")["diferencia"])
