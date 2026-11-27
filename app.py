import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv("numero_veiculos.csv")
cidade = df[df["id_municipio_nome"].isin(["Belo Horizonte", "Contagem", "Betim"])]
cidade = cidade[cidade["ano"] == 2025]
cidade = cidade[cidade["mes"] == 12]
cidade = cidade[cidade["quantidade"] > 0]
tabela = cidade[["tipo_veiculo", "quantidade", "id_municipio_nome"]]

grafico = df[df["id_municipio_nome"].isin(["Belo Horizonte"])]
grafico = grafico[grafico["ano"] == 2025]
grafico = grafico[grafico["mes"] == 12]
grafico = grafico[grafico["quantidade"] > 0]

tabela2 = cidade[["tipo_veiculo", "quantidade", "id_municipio_nome"]]



st.set_page_config(page_title="Prova Python", layout="wide")

st.title("Veículos BH Betim e Contagem")
st.write("Fonte: https://basedosdados.org/")
escolha = st.sidebar.radio(
    "O que você quer ver?",
    ["Tabela", "Gráfico - BH",  "Gráfico - Contagem",  "Gráfico - Betim"]
)
if escolha == "Tabela":
    st.header("Tabela")
    st.dataframe(cidade)
else:
    st.header("Gráfico de pizza - BH")
    grafico = px.pie(tabela, names="tipo_veiculo", values="quantidade")
    st.plotly_chart(grafico)