import streamlit as st
from agente_v0_2 import conversar_com_agente

st.set_page_config(page_title="Agente de Requisitos", layout="centered")

st.title("🧠 Agente de Requisitos")
st.markdown("Descreva sua ideia de projeto e receba sugestões de requisitos e tecnologias.")

# Campo de entrada
pergunta = st.text_area("💬 Sua ideia de projeto:", height=150)

# Botão para gerar resposta
if st.button("Gerar Requisitos"):
    if pergunta.strip() == "":
        st.warning("Por favor, descreva sua ideia antes de continuar.")
    else:
        with st.spinner("Consultando o agente..."):
            resposta = conversar_com_agente(pergunta)
        st.success("✅ Requisitos gerados com sucesso!")
        st.markdown("### 📄 Resposta do Agente:")
        st.write(resposta)