import streamlit as st
import pandas as pd
from streamlit.source_util import page_icon_and_name

st.set_page_config(page_title="Mi app",  page_icon="💊", layout="wide")
archivo = "Tabla_Preparacion_Antimicrobianos_HNGAI-VERSION 3.xlsx"

df = pd.read_excel(
    archivo,
    sheet_name="Registro x Laboratorio y Lote"
)

st.title("Consulta Rápida de Antimicrobianos")
st.title("FARMACIA - HNGAI")

# Antimicrobiano
antimicrobiano = st.selectbox(
    "Seleccione Antimicrobiano",
    sorted(df["Antimicrobiano"].dropna().unique())
)

df_filtrado = df[
    df["Antimicrobiano"] == antimicrobiano
]

# Laboratorio
laboratorio = st.selectbox(
    "Seleccione Laboratorio",
    sorted(df_filtrado["Laboratorio / Marca Fabricante"].dropna().unique())
)

resultado = df_filtrado[
    df_filtrado["Laboratorio / Marca Fabricante"] == laboratorio
]

if not resultado.empty:

    fila = resultado.iloc[0]

    col1, col2 = st.columns([3,2])

    with col1:

        st.metric(
            "Sueros Compatibles",
            str(fila["Sueros compatibles"])
        )

        st.metric(
            "Tiempo de Infusión",
            str(fila["Tiempo de infusión"])
        )

    with col2:

        st.metric(
            "Parámetro PK/PD",
            str(fila["Parámetro PK/PD"])
        )

        st.metric(
            "Estado",
            str(fila["Estado del Lote"])
        )

    st.subheader("Estabilidad")

    st.write(
        "Reconstituido T° ambiente:",
        fila["Estabilidad Reconst (T° Amb)"]
    )

    st.write(
        "Reconstituido refrigerado:",
        fila["Estabilidad Reconst (Refrig 2-8°C)"]
    )
    st.write(
        "Diluido T° ambiente:",
        fila["Estabilidad Diluido (T° Amb)"]
    )

    st.write(
        "Diluido refrigerado:",
        fila["Estabilidad Diluido (Refrig 2-8°C)"]
    )

    st.subheader("Observaciones")

    st.info(
        str(fila["Observaciones de Ficha Técnica del Fabricante"])
    )
