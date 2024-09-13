import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Cadastro Cliente", page_icon="✍")
st.title("Cadastro de clientes")
st.divider()

nome = st.text_input("Digite seu nome", key="nome_cliente")
dt_nasc = st.date_input("Data de nascimento", format="DD/MM/YYYY")
tipo = st.selectbox("Tipo do cliente", ["Pessoa jurídica", "Pessoa física"])

def gravar_dados(nome, dt_nasc, tipo):
    if nome and dt_nasc <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome}, {dt_nasc}, {tipo}\n")

        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

botao_cadastrar = st.button("Cadastar", on_click=gravar_dados, args=[nome, dt_nasc, tipo])

if botao_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastardo com sucesso", icon="✔")
    else:
        st.error("Verifique o cadastro", icon="⚠")
        
