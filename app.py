import streamlit as st
from agente_v0_2 import conversar_com_agente

st.set_page_config(page_title="Agente de Requisitos", layout="centered")

st.title("🧠 Agente de Requisitos de Software")
st.markdown("Descreva sua ideia de projeto e receba sugestões de requisitos e tecnologias.")

# Inicializa histórico
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# 🔽 Formulário: Enter envia e limpa automaticamente
with st.form(key="chat_form", clear_on_submit=True):
    pergunta = st.text_area("💬 Sua ideia de projeto:", height=150)
    submitted = st.form_submit_button("Enviar")
    if submitted:
        if pergunta.strip() == "":
            st.warning("Por favor, descreva sua ideia antes de continuar.")
        else:
            # Adiciona pergunta ao histórico
            st.session_state.mensagens.append({"role": "user", "content": pergunta})

            with st.spinner("Consultando o agente..."):
                resposta = conversar_com_agente(pergunta, contexto=st.session_state.mensagens)

            # Adiciona resposta ao histórico
            st.session_state.mensagens.append({"role": "assistant", "content": resposta})

            st.success("✅ Requisitos gerados com sucesso!")
            st.markdown("### 📄 Resposta do Agente:")
            st.write(resposta)

# Histórico retraído
with st.expander("📜 Histórico da Conversa", expanded=False):
    for msg in st.session_state.mensagens:
        if msg["role"] == "user":
            st.markdown(f"**Você:** {msg['content']}")
        else:
            st.markdown(f"**Agente:** {msg['content']}")

# Botão para reiniciar sessão
if st.button("🔄 Reiniciar conversa"):
    st.session_state.mensagens = []
    st.rerun()
